# Лабораторная работа №4
«Мониторинг сервиса из кубер кластера»

### Команда
* Безкоровайный Павел • K34211
* Долматов Дмитрий • K34212
* Коряков Сергей • K34201
* Кубашин Илья • K34211

## Задание

Сделать мониторинг сервиса, поднятого в кубере (использовать, например, prometheus и grafana). Показать хотя бы два рабочих графика, которые будут отражать состояние системы.

## Что будем делать

Добавлять в кубер кластер прометеус и графана для мониторинга метрик сервиса.

### Начальные настройки
Создание minikube.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/9d38d7fc-071e-4827-bb77-6e9202baf966)

Разворачивание кластера.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/09f641ee-60bb-4690-8fcc-08f8e99644dc)

Просмотр содержимого кубер кластера.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/88a6d03c-e6ef-4db6-ae97-db1e85248f6a)

### Просмотр интерфейса веб-приложения из кубер кластера.

Команда minikube для просмотра веб-интерфейса в браузере.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/8c1644e0-ad96-46d1-9f0c-d0a334c9ec99)

Сам веб-интерфейс приложения из кластера.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/c2a65d63-c180-4d3d-a2be-5b45598f559b)



### Добавление Grafana

Создание namespace для grafana и просмотр информации о нем. Создание файла для конфигов.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/994a6323-b6ae-4690-8124-b680f8f8c561)

![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/5ca4cf78-6f8b-4ec2-9d62-1ad6cb5be129)

![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/7a5b0e93-6888-4947-9169-173bfa48241f)

Выполнение команды port-forward, чтобы получить доступ к веб-интерфейсу.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/f2acd44f-c939-443c-a26a-3ae048b3fe03)

Веб-интерфейс grafana.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/43559874-cdbd-4462-af18-c14415b9efda)

### Добавление prometheus.
Добавляем prometheus в кластер.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/a2bc19f0-aed3-4818-b1a7-43e22897ee46)

Создаем namespace.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/7c941b86-3ede-43c5-85d3-bc161fe98a94)

Получаем информацию о нем.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/8f1de6ec-5c5c-4a18-9cdc-14a0032dae34)

Веб-интерфейс prometheus.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/983b7596-92a4-4db1-82c9-8648a7786466)


### Получение графиков

Далее в grafana создали соединение с prometheus и получили метрики системы, которые визуализировали.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/60f97dcb-df83-4277-8f46-bc2c943bb86b)

Графики в Grafana, которые показывают метрики работы системы.
![image](https://github.com/pashabezk/ITMO_clouds/assets/71008986/df7d8499-99f2-45ca-bfd9-6266200081d7)

## Вывод
В ходе выполнения лабораторной работы был проведен мониторинг сервиса, поднятого в кубер-кластере. Были использованы такие инструменты, как prometheus и grafana.
