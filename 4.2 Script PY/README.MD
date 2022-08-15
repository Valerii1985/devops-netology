# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач."

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?  | unsupported operand type(s) for +: 'int' and 'str'  |
| Как получить для переменной `c` значение 12?  | Перевести переменную А в строковое значение при помощи str(a) и сложить с переменной b  |
| Как получить для переменной `c` значение 3?  | Перевести переменную B в числовое значение при помощи int(b) и сложить с переменной a   |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/devops_netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/devops_netology", "pwd", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('/Users') != -1:
        git_path = result
    elif result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:     ', '')
        print(git_path, prepare_result)
```

### Вывод скрипта при запуске при тестировании:
```
/Users/valeriikiselev/devops_netology  4.2 Script PY/README.MD
/Users/valeriikiselev/devops_netology  pytest
```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os
import sys

git_path = os.getcwd()

if len(sys.argv) >= 2:
    git_path = sys.argv[1]

bash_command = ["cd "+ git_path, "git status 2>&1"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('fatal:') != -1:
        print("Git репозиторий в " + git_path + " не обнаружен :(")    
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено: ', '') 
        print(git_path + prepare_result)

```

### Вывод скрипта при запуске при тестировании:
```
valeriikiselev@Valeriis-MacBook-Pro ~ % python3 ~/devops_netology/pytest1.py ~/devops_netology
/Users/valeriikiselev/devops_netology     pytest.py
/Users/valeriikiselev/devops_netology     pytest1.py

valeriikiselev@Valeriis-MacBook-Pro ~ % python3 ~/devops_netology/pytest1.py ~/parallels
Git репозиторий в /Users/valeriikiselev/parallels не обнаружен :(
vale
```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
import socket
import time

web_adr = {
    'drive.google.com':'0.0.0.0',
    'mail.google.com':'0.0.0.0',
    'google.com':'0.0.0.0'
}

for item in web_adr:
    back_adr = socket.gethostbyname(item)
    web_adr[item] = back_adr


while True:
    for item in web_adr:
        old_ip = web_adr[item]
        new_ip = socket.gethostbyname(item)
        if new_ip != old_ip:
            web_adr[item] = new_ip
            print("[ERROR] " + item + " IP mismatch: old IP " + old_ip + ", new IP " + new_ip)
        print(item + " - " + web_adr[item])
    print(2*"\n------------------------------------")
    time.sleep(10)
```

### Вывод скрипта при запуске при тестировании:
```
python3 ~/devops_netology/pytest2.py
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.17
google.com - 142.251.1.139

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.17
google.com - 142.251.1.139

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.17
google.com - 142.251.1.139

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.17
google.com - 142.251.1.139

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
[ERROR] mail.google.com IP mismatch: old IP 64.233.165.17, new IP 64.233.165.18
mail.google.com - 64.233.165.18
[ERROR] google.com IP mismatch: old IP 142.251.1.139, new IP 142.251.1.113
google.com - 142.251.1.113

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.18
google.com - 142.251.1.113

------------------------------------
------------------------------------
drive.google.com - 173.194.73.194
mail.google.com - 64.233.165.18
google.com - 142.251.1.113
```
