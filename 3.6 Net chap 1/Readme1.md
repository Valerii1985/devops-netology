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
<pre>
URL запроса: http://stackoverflow.com/
Метод запроса: GET
Код статуса: 307 Internal Redirect
Правило для URL перехода: strict-origin-when-cross-origin
</pre>
HTTP код перенаправления 307 Temporary Redirect означает, что запрошенный ресурс был временно перемещён в URL-адрес, указанный в заголовке Location. Метод и тело исходного запроса повторно используются для выполнения перенаправленного запроса.
### проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
Общая загрузка сайта 1600Мс. самый долгий запрос 482мс - https://stackoverflow.com/ 
### приложите скриншот консоли браузера в ответ.

<img src="/Users/valeriikiselev/Desktop/Снимок экрана 2022-07-09 в 11.41.33.jpg"/>(Снимок экрана 2022-07-09 в 11.41.33.jpg)

# 3. Какой IP адрес у вас в интернете?
78.36.203.160
# 4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois
Rostelecom, AS12389
<pre>
whois -h whois.radb.net 78.36.203.160
route:          78.36.200.0/21
descr:          Rostelecom networks
origin:         AS12389
notify:         ripe@rt.ru
mnt-by:         ROSTELECOM-MNT
created:        2018-10-25T14:21:59Z
last-modified:  2018-10-25T14:21:59Z
source:         RIPE
remarks:        ****************************
remarks:        * THIS OBJECT IS MODIFIED
remarks:        * Please note that all data that is generally regarded as personal
remarks:        * data has been removed from this object.
remarks:        * To view the original object, please query the RIPE Database at:
remarks:        * http://www.ripe.net/whois
remarks:        ****************************
</pre>
# 5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute
<pre>
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
 1  router.lan (192.168.27.1)  6.184 ms  6.242 ms  2.201 ms
 2  klng-bras4.sz.ip.rostelecom.ru (212.48.195.247)  4.960 ms  14.646 ms  3.662 ms
 3  e120-1-vinco.nwtelecom.ru (212.48.198.234)  3.554 ms
    212.48.198.232 (212.48.198.232)  4.034 ms  4.495 ms
 4  * 188.254.2.4 (188.254.2.4)  37.883 ms *
 5  72.14.209.89 (72.14.209.89)  29.900 ms
    87.226.194.47 (87.226.194.47)  23.204 ms
    72.14.209.89 (72.14.209.89)  39.576 ms
 6  * * 74.125.244.132 (74.125.244.132)  22.144 ms
 7  108.170.250.33 (108.170.250.33)  32.240 ms  31.195 ms
    72.14.232.85 (72.14.232.85)  27.442 ms
 8  142.251.61.221 (142.251.61.221)  29.702 ms  25.403 ms  30.635 ms
 9  142.250.238.138 (142.250.238.138)  31.650 ms
    142.251.78.106 (142.251.78.106)  32.253 ms
    142.251.238.82 (142.251.238.82)  34.576 ms
10  142.251.238.68 (142.251.238.68)  39.527 ms *
    72.14.232.76 (72.14.232.76)  36.653 ms
11  * 142.250.56.13 (142.250.56.13)  38.811 ms *
12  * * *
13  * * *
14  * * *
</pre>
# 6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?
<pre>
8.8.8.8 2022-07-10T15:08:38+0200
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                       Packets               Pings
 Host                                Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. AS???    192.168.27.1             0.0%    30    3.3   5.3   3.1  27.2   4.8
 2. AS12389  212.48.195.247           0.0%    30    4.1  16.1   3.0 107.5  24.7
 3. AS12389  212.48.198.234           0.0%    30    4.0   8.7   3.7  35.7   7.8
 4. AS12389  185.140.148.153         78.6%    29   29.8  31.8  29.8  36.3   2.5
 5. AS15169  72.14.209.89             0.0%    29   31.1  33.0  30.0  44.0   3.7
 6. AS15169  108.170.250.129          0.0%    29   32.0  36.2  30.8  63.9   6.8
 7. AS15169  108.170.250.130          0.0%    29   31.0  35.0  30.3  60.2   7.0
 8. AS15169  142.250.238.214          0.0%    29   38.8  42.0  38.3  54.7   5.1
 9. AS15169  142.250.235.74           0.0%    29   39.1  41.5  38.2  63.2   5.3
10. AS15169  216.239.42.23            0.0%    29   37.2  38.3  37.0  42.6   1.5
11. (waiting for reply)
</pre>
Наибольшая задержка по среднему значению (AVG) - AS15169  142.250.238.214
# 7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig
<pre>
% dig +short NS dns.google
ns3.zdns.google.
ns2.zdns.google.
ns4.zdns.google.
ns1.zdns.google.
</pre>
# 8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig
<pre>
 % dig +noall +answer -x 8.8.8.8
8.8.8.8.in-addr.arpa.	14400	IN	PTR	dns.google.
% dig +noall +answer -x 8.8.4.4
4.4.8.8.in-addr.arpa.	14400	IN	PTR	dns.google.
</pre>