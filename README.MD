# Курсовая работа по итогам модуля "DevOps и системное администрирование"

Курсовая работа необходима для проверки практических навыков, полученных в ходе прохождения курса "DevOps и системное администрирование".

Мы создадим и настроим виртуальное рабочее место. Позже вы сможете использовать эту систему для выполнения домашних заданий по курсу

## Задание

1. Создайте виртуальную машину Linux.
2. Установите ufw и разрешите к этой машине сессии на порты 22 и 443, при этом трафик на интерфейсе localhost (lo) должен ходить свободно на все порты.
3. Установите hashicorp vault ([инструкция по ссылке](https://learn.hashicorp.com/tutorials/vault/getting-started-install?in=vault/getting-started#install-vault)).
4. Cоздайте центр сертификации по инструкции ([ссылка](https://learn.hashicorp.com/tutorials/vault/pki-engine?in=vault/secrets-management)) и выпустите сертификат для использования его в настройке веб-сервера nginx (срок жизни сертификата - месяц).
5. Установите корневой сертификат созданного центра сертификации в доверенные в хостовой системе.
6. Установите nginx.
7. По инструкции ([ссылка](https://nginx.org/en/docs/http/configuring_https_servers.html)) настройте nginx на https, используя ранее подготовленный сертификат:
  - можно использовать стандартную стартовую страницу nginx для демонстрации работы сервера;
  - можно использовать и другой html файл, сделанный вами;
8. Откройте в браузере на хосте https адрес страницы, которую обслуживает сервер nginx.
9. Создайте скрипт, который будет генерировать новый сертификат в vault:
  - генерируем новый сертификат так, чтобы не переписывать конфиг nginx;
  - перезапускаем nginx для применения нового сертификата.
10. Поместите скрипт в crontab, чтобы сертификат обновлялся какого-то числа каждого месяца в удобное для вас время.

## Результат

Результатом курсовой работы должны быть снимки экрана или текст:

- Процесс установки и настройки ufw
####Предустановлен в Ubuntu 20.04
```
val@val:~$ ufw version
ufw 0.36
Copyright 2008-2015 Canonical Ltd.

val@val:~$ sudo ufw allow 22
Rule added
Rule added (v6)

val@val:~$ sudo ufw allow 443
Skipping adding existing rule
Skipping adding existing rule (v6)

val@val:~$ sudo ufw allow in on lo
Rule added
Rule added (v6)

val@val:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Apache Full                ALLOW       Anywhere                  
443                        ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
22                         ALLOW       Anywhere                  
Anywhere on lo             ALLOW       Anywhere                  
Apache Full (v6)           ALLOW       Anywhere (v6)             
443 (v6)                   ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
22 (v6)                    ALLOW       Anywhere (v6)             
Anywhere (v6) on lo        ALLOW       Anywhere (v6)             


```
- Процесс установки и выпуска сертификата с помощью hashicorp vault
```
val@val:~$ wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null

val@val:~$ gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint

val@val:~$ echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

val@val:~$ sudo apt update && sudo apt install vault

val@val:~$ vault server -dev

val@val:~$ export VAULT_ADDR='http://127.0.0.1:8200'

val@val:~$ export VAULT_TOKEN="s.FrwwqFkRqkNzpt0QbdjnzUuB"

val@val:~$ vault status
Key             Value
---             -----
Seal Type       shamir
Initialized     true
Sealed          false
Total Shares    1
Threshold       1
Version         1.5.9
Cluster Name    vault-cluster-163ef302
Cluster ID      11cd16be-aaab-5c9c-fccc-4bbaa227c9ee
HA Enabled      false

val@val:~$ vault server -dev -dev-root-token-id root

val@val:~$ export VAULT_ADDR=http://127.0.0.1:8200

val@val:~$ export VAULT_TOKEN=root

val@val:~$ vault secrets enable pki
Success! Enabled the pki secrets engine at: pki/

val@val:~$ vault secrets tune -max-lease-ttl=87600h pki
Success! Tuned the secrets engine at: pki/

val@val:~$ vault write -field=certificate pki/root/generate/internal \
     common_name="example.com" \
     issuer_name="root-2022" \
     ttl=87600h > root_2022_ca.crt
     
val@val:~$ vault write pki/roles/2022-servers allow_any_name=true
Success! Data written to: pki/roles/2022-servers

val@val:~$ vault write pki/config/urls \
     issuing_certificates="$VAULT_ADDR/v1/pki/ca" \
     crl_distribution_points="$VAULT_ADDR/v1/pki/crl"

Success! Data written to: pki/config/urls

val@val:~$ vault secrets enable -path=pki_int pki
Success! Enabled the pki secrets engine at: pki_int/

val@val:~$ vault secrets tune -max-lease-ttl=43800h pki_int
Success! Tuned the secrets engine at: pki_int/

val@val:~$ vault write -format=json pki_int/intermediate/generate/internal \
     common_name="example.com Intermediate Authority" \
     issuer_name="example-dot-com-intermediate" \
     | jq -r '.data.csr' > pki_intermediate.csr

Command 'jq' not found, but can be installed with:
sudo snap install jq  # version 1.5+dfsg-1, or
sudo apt  install jq  # version 1.6-2.1ubuntu3
See 'snap info jq' for additional versions.

val@val:~$ sudo snap install jq
jq 1.5+dfsg-1 from Michael Vogt (mvo\u272a) installed

val@val:~$ vault write -format=json pki_int/intermediate/generate/internal \
     common_name="example.com Intermediate Authority" \
     issuer_name="example-dot-com-intermediate" \
     | jq -r '.data.csr' > pki_intermediate.csr
     
val@val:~$ vault write -format=json pki/root/sign-intermediate \
     issuer_ref="root-2022" \
     csr=@pki_intermediate.csr \
     format=pem_bundle ttl="43800h" \
     | jq -r '.data.certificate' > intermediate.cert.pem

val@val:~$ vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem
Success! Data written to: pki_int/intermediate/set-signed

val@val:~$ vault write pki_int/roles/example-dot-com \
     issuer_ref="$(vault read -field=default pki_int/config/issuers)" \
     allowed_domains="example.com" \
     allow_subdomains=true \
     max_ttl="720h"

Success! Data written to: pki_int/roles/example-dot-com

val@val:~$ vault write -format=json pki_int/issue/example-dot-com common_name="test.example.com" ttl="720h" > test.example.com.crt
val@val:~$ cat test.example.com.crt | jq -r .data.certificate > test.example.com.crt.pem
val@val:~$ cat test.example.com.crt | jq -r .data.issuing_ca >> test.example.com.crt.pem
val@val:~$ cat test.example.com.crt | jq -r .data.private_key > test.example.com.crt.key
```
- Процесс установки и настройки сервера nginx
```
val@val:~$ sudo apt install nginx

val@val:~$ sudo mkdir -p /var/www/test.example.com/html

val@val:~$ sudo chmod -R 755 /var/www/test.example.com/

val@val:~$ sudo nano /etc/nginx/sites-available/test.example.com

val@val:~$ sudo mv test.example.com.crt.key /etc/ssl

val@val:~$ sudo mv test.example.com.crt.pem /etc/ssl

val@val:~$ sudo nano /etc/nginx/nginx.conf
server {
        listen              443 ssl;
        server_name test.example.com www.test.example.com;

        ssl_certificate     "/etc/ssl/test.example.com.crt.pem";
        ssl_certificate_key "/etc/ssl/test.example.com.crt.key";

        ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers         HIGH:!aNULL:!MD5;

        root /var/www/test.example.com/html;
        index index.html index.htm index.nginx-debian.html;



        location / {
                try_files $uri $uri/ =404;
        }
}

val@val:~$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

val@val:~$ sudo systemctl restart nginx
```
- Страница сервера nginx в браузере хоста не содержит предупреждений
  ![](https://github.com/Valerii1985/devops-netology/blob/main/ssl.jpg)
- Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")
```
val@val:~$ sudo nano sertgenerator
#!/usr/bin/env bash

vault write -format=json pki_int/issue/example-dot-com common_name="test.example.com" ttl="720h" > /home/val/test.example.com.crt

cat /home/val/test.example.com.crt | jq -r .data.certificate > /etc/ssl/test.example.com.crt.pem
cat /home/val/test.example.com.crt | jq -r .data.issuing_ca >> /etc/ssl/test.example.com.crt.pem
cat /home/val/test.example.com.crt | jq -r .data.private_key > /etc/ssl/test.example.com.crt.key

systemctl restart nginx.service
```
- Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)
```
sudo crontab -e

00 10 01 * * /home/val/sertgenerate
```