
## Задача 1

Сценарий выполения задачи:

- создайте свой репозиторий на https://hub.docker.com;
- выберете любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность:
запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```

Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

```
vagrant@server1:~/netology$ sudo nano index.html
...
vagrant@server1:~/netology$ sudo nano Dockerfile
---
FROM nginx:latest

COPY ./index.html /usr/share/nginx/html/index.html
...
vagrant@server1:~/netology$ docker build -t lerich1985/nginx .
...
docker run -it -d -p 8080:80 --name ng lerich1985/nginx
...
```

![](https://github.com/Valerii1985/devops-netology/blob/main/5.3%20Docker/Screenshot.jpg)

```
vagrant@server1:~$ docker tag lerich1985/nginx lerich1985/nginx:1.0.0
vagrant@server1:~$ docker images
REPOSITORY       TAG       IMAGE ID       CREATED        SIZE
lerich1985/nginx   1.0.0     15c67c09e633   22 hours ago   142MB
lerich1985/nginx   latest    15c67c09e633   22 hours ago   142MB
proga            1.0.0     9e9fb4780ef0   3 days ago     921MB
python           latest    e285995a3494   3 weeks ago    921MB
nginx            latest    2d389e545974   3 weeks ago    142MB

vagrant@server1:~$ docker push lerich1985/nginx:1.0.0
```
link: https://hub.docker.com/repository/docker/lerich1985/nginx

## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
"Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- Высоконагруженное монолитное java веб-приложение;

Виртуальная машина, т.к. в монолите все находится в одном месте
- Nodejs веб-приложение;

Точно docker. Скорость развертывания, тестирование, полная изоляция проекта.
- Мобильное приложение c версиями для Android и iOS;

Для Android подойдет docker. Для iOS нужна только MacOs, поэтому физический сервер
- Шина данных на базе Apache Kafka;

Особенность шины kafka в том, что она позволяет на ранних этапах заложить в архитектуру бэкенда структуры, которые можно беспроблемно масштабировать в будущем. А масштабируемость - это docker
- Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;

Я думаю отдельная вм, для нормальной производительности кластера
- Мониторинг-стек на базе Prometheus и Grafana;

Тут можно и docker - данный стек не требует ресурсного обеспечения.
- MongoDB, как основное хранилище данных для java-приложения;

Виртуалка или сервер - требуются ресурсы
- Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

docker - скорость развертывания, данные хранить не нужно
## Задача 3

- Запустите первый контейнер из образа ***centos*** c любым тэгом в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```;
- Добавьте еще один файл в папку ```/data``` на хостовой машине;
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера.

```
vagrant@server1:~$ docker run -it -d -v /data:/data --name centos centos
...
vagrant@server1:~$ docker run -it -d -v /data:/data --name debian debian
...
vagrant@server1:~$ docker exec -it centos bash
[root@599de42a0fb4 /]# cd data
[root@599de42a0fb4 data]# echo "here is centos" >> test1.txt
[root@599de42a0fb4 data]# exit
...
vagrant@server1:~/data$ sudo nano test2.txt
...
vagrant@server1:~$ docker exec -it debian bash
root@ee345312ca00:/# cd /data
root@ee345312ca00:/data# ls -l
total 8
-rw-r--r-- 1 root root 15 Oct  5 15:57 test1.txt
-rw-r--r-- 1 root root 13 Oct  5 16:05 test2.txt
root@ee345312ca00:/data# exit
exit
```