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

val@val:~$ vault write -format=json pki_int/intermediate/generate/internal      common_name="example.com Intermediate Authority"      issuer_name="example-dot-com-intermediate"      | jq -r '.data.csr' > pki_intermediate.csr

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

val@val:~$ vault write pki_int/issue/example-dot-com common_name="test.example.com" ttl="24h"
Key                 Value
---                 -----
ca_chain            [-----BEGIN CERTIFICATE-----
MIIDpjCCAo6gAwIBAgIUfZGkqrMn8C10PLMdt+w5o6aAvcQwDQYJKoZIhvcNAQEL
BQAwFjEUMBIGA1UEAxMLZXhhbXBsZS5jb20wHhcNMjIwODI5MTcxNTE5WhcNMjcw
ODI4MTcxNTQ5WjAtMSswKQYDVQQDEyJleGFtcGxlLmNvbSBJbnRlcm1lZGlhdGUg
QXV0aG9yaXR5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu3omwpp5
gh+r4BUo6XRl4gWSorxmjkEg3GgyF3XaCYID+kxMqpTZ2Tukcv1uRxMojuG8RDys
9Jh93WsLDxZQtJsWwOoTOwIglj/DVDGBrph5StsU3s+WytVukFIkWAumifV+56CT
a/BmBcFlIKYuIYE1qjEpEMzQU0dQB0/d21tOIk4yr6nHyO9ZaMDycFkDXpUq4FLq
1RSqLPocpa0SN1ecCnvaee6BNnfgSBCIEtCeXnH/6nlb4IhtLzKEfmyU+l3jPnPl
SnkoKXgm8KiQoQuZGWqPGwzF8w1NeKgNbVBmU7Wa+RPFp9kfKSx/twCb1zqRLcCF
yWMMecgY+FTszwIDAQABo4HUMIHRMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E
BTADAQH/MB0GA1UdDgQWBBRKLutrilC8xAmRdR9VQsdPRoL26DAfBgNVHSMEGDAW
gBQ5JCZylSDX4QRrbheJX4FfD9oE9jA7BggrBgEFBQcBAQQvMC0wKwYIKwYBBQUH
MAKGH2h0dHA6Ly8xMjcuMC4wLjE6ODIwMC92MS9wa2kvY2EwMQYDVR0fBCowKDAm
oCSgIoYgaHR0cDovLzEyNy4wLjAuMTo4MjAwL3YxL3BraS9jcmwwDQYJKoZIhvcN
AQELBQADggEBAGpQNu8oPnTREOe49ATVs8VGLt2ZSqeKJ9ucgNYfRi+jteKPfdn6
QwRzyQu3B21SB6tXhg4Z15+Y8l5KlNDBhP24og2/ao8VZ0XUWFhzNEKQBS/tJBaW
2O+fnqxEdQXHDvNtx6OWLhIUrIbMfP9WGX+uUKTAnj1G9vQtreaGVyVv5ahcUYCF
dcJL/klKUxPw4DLQq9ufjhx0xNe/fAtUda9ke6HDptnTX8l0ufttEUQm0PP9a6Cd
XugGzUaRzvnsBV1qG8v6o8kS3n1x5awGHuFCWaog/aqXxm5ZdvozrGV8NroJrIGr
akZoipiZJ6DzyAbtg9ntpRSyayKtvPeCYGc=
-----END CERTIFICATE-----]

....

private_key_type    rsa
serial_number       79:cb:28:b1:77:ec:b2:95:f1:b0:29:13:a8:4c:23:8a:74:63:de:15

```
- Процесс установки и настройки сервера nginx
```
val@val:~$ sudo apt install nginx
```
- Страница сервера nginx в браузере хоста не содержит предупреждений 
- Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")
- Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)
