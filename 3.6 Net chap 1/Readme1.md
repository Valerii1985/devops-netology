# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"
# 1. Работа c HTTP через телнет.

### Подключитесь утилитой телнет к сайту stackoverflow.com telnet stackoverflow.com 80

### отправьте HTTP запрос
<pre>GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]</pre>
### В ответе укажите полученный HTTP код, что он означает?
<pre>
HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: d9e4c61b-4907-49db-8aeb-287786701355
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Wed, 06 Jul 2022 18:17:13 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-hhn4078-HHN
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1657131433.874058,VS0,VE171
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=ac072580-d943-b873-041a-9db87ddb8b15; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.
</pre>

 стандартный код ответа HTTP, получаемый в ответ от сервера в ситуации, когда запрошенный ресурс был на постоянной основе перемещён в новое месторасположение, и указывающий на то, что текущие ссылки, использующие данный URL, должны быть обновлены. 

# 2. Повторите задание 1 в браузере, используя консоль разработчика F12.

### откройте вкладку Network

### отправьте запрос http://stackoverflow.com

### найдите первый ответ HTTP сервера, откройте вкладку Headers

### укажите в ответе полученный HTTP код.

### проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?

### приложите скриншот консоли браузера в ответ.

![Screenshot](/Users/valeriikiselev/Desktop/Снимок экрана 2022-07-09 в 11.41.33.jpg)

#3. Какой IP адрес у вас в интернете?
Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois
Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute
Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?
Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig
Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig
В качестве ответов на вопросы можно приложите лог выполнения команд в консоли или скриншот полученных результатов.