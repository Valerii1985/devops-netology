# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

#1. На лекции мы познакомились с node_exporter. В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter: 
Долго не получалось разобраться с запуском и работой node-exporter

Оказалось процесс по умолчанию был запущен, видимо после установки prometheus

Решил проблему удалением из автозагрузки node-exporter, чтобы запустить и настроить скачанный

1. Исполняемый файл был перенесен в /usr/local/bin

2. unit:
sudo systemctl edit --full --force node_exporter.service

[Unit]

Description=Prometheus Node Exporter

Wants=network-online.target

After=network-online.target

[Service]

User=node_exporter

Group=node_exporter

Type=simple

ExecStart=/usr/local/bin/node_exporter

[Install]

WantedBy=multi-user.target


#-поместите его в автозагрузку,
#-предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на systemctl cat cron), 
#-удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается. 

Сделано. Процесс автоматически запускается. systemctl stop/start успешно останавливает и запускает процесс. При перезагрузке виртуальной машины node_exporter работает

#2. Ознакомьтесь с опциями node_exporter и выводом /metrics по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.

Процессор:

node_cpu_seconds_total{cpu="0",mode="idle"} 3267.1

node_cpu_seconds_total{cpu="0",mode="system"} 26.37

node_cpu_seconds_total{cpu="0",mode="user"} 36.89

node_cpu_seconds_total{cpu="1",mode="idle"} 3264.3

node_cpu_seconds_total{cpu="1",mode="system"} 23.87

node_cpu_seconds_total{cpu="1",mode="user"} 35.11

Память:

node_memory_MemAvailable_bytes 6.85146112

node_memory_MemFree_bytes 7.2208384

node_memory_Mlocked 1.8972672

Диски:

node_disk_io_time_seconds_total{device="sda"} 29.944
    
node_disk_read_bytes_total{device="sda"} 4.91038

node_disk_read_time_seconds_total{device="sda"} 9.599
    
node_disk_write_time_seconds_total{device="sda"} 21.816

Сеть:

node_network_receive_errs_total{device="eth0"} 
node_network_receive_bytes_total{device="eth0"} 
node_network_transmit_bytes_total{device="eth0"}
node_network_transmit_errs_total{device="eth0"}

Установите в свою виртуальную машину Netdata. Воспользуйтесь готовыми пакетами для установки (sudo apt install -y netdata). После успешной установки:

в конфигурационном файле /etc/netdata/netdata.conf в секции [web] замените значение с localhost на bind to = 0.0.0.0,
добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте vagrant reload:
config.vm.network "forwarded_port", guest: 19999, host: 19999
После успешной перезагрузки в браузере на своем ПК (не в виртуальной машине) вы должны суметь зайти на localhost:19999. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.

Можно ли по выводу dmesg понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?

Как настроен sysctl fs.nr_open на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (ulimit --help)?

Запустите любой долгоживущий процесс (не ls, который отработает мгновенно, а, например, sleep 1h) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через nsenter. Для простоты работайте в данном задании под root (sudo -i). Под обычным пользователем требуются дополнительные опции (--map-root-user) и т.д.

Найдите информацию о том, что такое :(){ :|:& };:. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (это важно, поведение в других ОС не проверялось). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов dmesg расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?