# Лабораторная работа №2
«Кубернетес с собачкой без ошейника»

### Команда
* Безкоровайный Павел • K34211
* Долматов Дмитрий • K34212
* Коряков Сергей • K34201
* Кубашин Илья • K34211

## Задание

Развернуть кластер K8S с несколькими ресурсами без HTTPS.

## Ход работы

Первым делом установим minikube. Если коротко, это такой докер-контейнер, который позволяет создавать песочницу из K8S кластера.  

Более того, в нём можно создавать поднимать докер-контейнеры тоже (контейнер в контейнер. "Чтобы открыть матрешку - надо открыть матрешку").

Отличие в том, что в K8S минимальной единицей является pod (обёртка вокруг контейнера).

Наше приложение будет состоять из нескольких podoв внутри одной ноды. Кстати, распределяет ресурсы, выделенные на ноду - kubelet. Поскольку мы создаем одну ноду, чтобы не перегружать систему, то всю досталось одной ноде.

<img src='./images/Установка minikube.png' width='500px'/>

Kubectl установлен по умолчанию

### Проектирование конфигурации
Стоит упомянуть, что наша структура будет иметь следующий вид: в ConfigMap будет находиться url на БД, в секретах - зашифрованные логины и пароли от БД, а также 2 файла для деплоя и сервисов как БД, так и самого приложения

Писать одновременно в одном файле и деплой, и сервис - хорошая практика. Вдобавок, отметитим, что все конфигурационные части будут находиться в одном файле по требованию к работе.
Сервис отвечает за маршрутизацию запросов, деплой - за создание **blueprint**  - количества реплик данного pod.

Поскольку базы данных не рекомендуется реплицировать через K8S blueprint, то создадим лишь одну реплику-оригинал.

Проверим minikube ip, по которому в итоге будет подключаться (не по localhost, хотя он тоже работает)

<img src='./images/Просмотр ip minikube.png' width='500px'/>

Шифрование пароля через base64 представлено ниже.


<img src='./images/Шифрование логина и пароля для бд.png' width='500px'/>

Введем зашифрованный логин и пароль в секрет.

<img src='./images/Ввод зашифрованного пароля в секрет.png' width='500px'/>


Далее, напишем скрипты для создания каждого конфигурационного элемента. Данные приложены ниже.

ConfigMap для БД:


<img src='./images/Конфиг-мап для бд.png' width='500px'/>

Деплой для БД:


<img src='./images/Деплой БД.png' width='500px'/>

Сервис для БД:


<img src='./images/Сервис бд.png' width='500px'/>

Деплой для приложения (был взят образ с DockerHub как приложения, так и БД)


<img src='./images/Деплой приложения.png' width='500px'/>

Сервис для приложения:


<img src='./images/Сервис приложения.png' width='500px'/>

P.S. Как вы могли заметить, хорошей практикой является зеркалирование внутреннего и внешнего порта.
Более того, на NodePort, отвечающий за внешние соединения, должен быть в промежутке от 30000-32760.


## Оценим работу конфигурационного файла
Работает одна нода, что соответствует ожиданиям.

<img src='./images/Проверка работы одной ноды.png' width='500px'/>

Описание сервиса приложение представлено ниже:


<img src='./images/Описание сервиса.png' width='500px'/>

Полная конфигурация без учета ConfigMap и Secret представлено ниже:


<img src='./images/Полный конфиг.png' width='500px'/>

Конфиг-мапа и секрет представлены ниже (они не показываются в общей конфигурации)

<img src='./images/Конфигмапы и секреты.png' width='500px'/>

В итоге, после запуска работы нашего приложения, видим, что оно работает:


<img src='./images/Работает).png' width='500px'/>


## Вывод
В ходе выполнения лабораторной работы был создан кластер на одной ноде K8S для развёртывания node.js с mongodb приложения, находящего в общем network
Более того, реплик БД - 1 для обеспечения констистентности данных внутри ноды.