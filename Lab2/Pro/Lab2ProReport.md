# Лабораторная работа №2
«Кубернетес с собачкой с ошейником»

### Команда
* Безкоровайный Павел • K34211
* Долматов Дмитрий • K34212
* Коряков Сергей • K34201
* Кубашин Илья • K34211

## Задание

Развернуть кластер K8S с несколькими ресурсами с HTTPS.

## Ход работы
Поскольку развернуть HTTPS на драйвере Docker в виде контейнера не представляется возможным на Windows 11, то было принято решение создать образ ВМ через Hyper-V Manager.

Образ:


<img src='./images/Hyper-v.png' width='500px'/>

Далее, был установлен установщик пакетов Chocolatey

<img src='./images/Chocolatey.png' width='500px'/>

Через Chocolatey был установлен плагин, который позволяет создавать самоподписанные (self-signed) сертификаты

<img src='./images/Helm для сертификатов.png' width='500px'/>

Успешная установка показана ниже.

<img src='./images/Успеш helm.png' width='500px'/>

Для того, чтобы создать секрет - необходимо наличие приватного ключа и сертификата. Сделаем их

<img src='./images/Создание ключа и сертификата.png' width='500px'/>

Далее, необходимо проверить сертификат

<img src='./images/Просмотр сертификата.png' width='500px'/>

Заранее проверим FireWall на HTTPS соединение.

<img src='./images/Проверка работы фаервола.png' width='500px'/>

Необходимо добавить в /etc/hosts информацию по поводу DNS псевдо-домена трансляции адресов

<img src='./images/Добавление название псевдо-домена в hosts для трансляции в ip.png' width='500px'/>

Зачем нам это? Для того чтобы по названию переходить на ip адрес (не localhost).

Создадим секрет на основе приватного ключа и сертификата

<img src='./images/Создание секрета.png' width='500px'/>


После необходимо выполнить самую главную часть - добавление ingress в конфигурационный файл.
Он необходим, поскольку является первой структурой на пути к запросу, который распределяет их по services


```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-service
spec:
  tls:
    - hosts:
        - ingress.minikube
      secretName: my-service-tls
  rules:
    - host: ingress.minikube
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: webapp-service
                port:
                  number: 3000
```

Укажем в ingress.minikube адрес, который соответствует записи в hosts, на адресе которого будет использоваться созданный нами секрет
Порт выставлен по порту webapp-service, который получает запрос.


При запросе по этому же адресу с использованием псевдо-доменного имени браузер жалуется на самоподписанный сертификат, который является нашим.

<img src='./images/Сертификат не тот.png' width='500px'/>

Самоподписанные сертификаты не являются доверенными центрами сертификации (Certificate Authorities - CAs). Браузеры обычно ожидают, что сертификаты будут подписаны доверенным CA, иначе они выдают предупреждение.

## Вывод
В ходе выполнения лабораторной работы был создан кластер на одной ноде K8S для развёртывания node.js с mongodb приложения, находящего в общем network.
Более того, мы можем создавать самоподписанные сертификаты, используя их как дополнительную защиту в случае несанкционированного подключения, однако на такие сертификаты жалуются браузеры, поэтому при деплое не стоит использовать неавторизованные сертификаты.