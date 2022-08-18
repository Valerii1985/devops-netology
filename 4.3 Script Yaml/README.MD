# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
import socket
import time
import json
import yaml

web_adr = {
    'drive.google.com':'0.0.0.0',
    'mail.google.com':'0.0.0.0',
    'google.com':'0.0.0.0'
}

for item in web_adr:
    back_adr = socket.gethostbyname(item)
    web_adr[item] = back_adr
    # json
    with open(item + ".json", 'w') as jsn:
        jsn_data= json.dumps({item: web_adr[item]})
        jsn.write(jsn_data) 
    # yaml
    with open(item + ".yaml", 'w') as yml:
        yml_data= yaml.dump({item: web_adr[item]})
        yml.write(yml_data)

while True:
    for item in web_adr:
        old_ip = web_adr[item]
        new_ip = socket.gethostbyname(item)
        if new_ip != old_ip:
            web_adr[item] = new_ip
            
            with open(item + '.json', 'w') as jsn:
                jsn_data = json.dumps({item: web_adr[item]})
                jsn.write(jsn_data)

            with open(item + '.yaml', 'w') as yml:
                yml_data = yaml.dump({item: web_adr[item]})
                yml.write(yml_data)
            print("[ERROR] " + item + " IP mismatch: old IP " + old_ip + ", new IP " + new_ip)
        print(item + " - " + web_adr[item])
    print(2*"\n------------------------------------")
    time.sleep(10)
```

### Вывод скрипта при запуске при тестировании:
```
valeriikiselev@Valeriis-MacBook-Pro devops_netology % python3 pytest3.py
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100

------------------------------------
------------------------------------
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100

------------------------------------
------------------------------------
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100

------------------------------------
------------------------------------
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100

------------------------------------
------------------------------------
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100

------------------------------------
------------------------------------
drive.google.com - 64.233.162.194
mail.google.com - 108.177.14.83
google.com - 74.125.131.100
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
cat drive.google.com.json
{"drive.google.com": "64.233.162.194"}%

cat google.com.json
{"google.com": "74.125.131.100"}%

cat mail.google.com.json
{"mail.google.com": "108.177.14.83"}%
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
cat drive.google.com.yaml
drive.google.com: 64.233.162.194

cat google.com.yaml
google.com: 74.125.131.100

cat mail.google.com.yaml
mail.google.com: 108.177.14.83
```