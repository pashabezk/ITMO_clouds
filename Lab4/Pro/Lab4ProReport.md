# Четвертая со звездочкой
> Важная информация: судя по времени пуша, можно заметить что с выполнением 4* пошло что-то не так, поэтому я как исполнитель беру ответсвенность за плагиат на себя и честно прикрепляю ссылки теми ресурсами (гитами одногруппников) которыми пользовался: [Команда 9 🐣](https://github.com/LenaSpevak/2023-2024_DevOps_Kostenko_Spevak_Guseynov/blob/main/lab4/lab4star_report.md)
## Запуск всего-всего
Поднимаю миникуб, графану (описано в 4ой лабе):
```
minikube start --vm-driver=hyperv
kubectl create -f .\all-config.yaml
minikube service webapp-service
kubectl create namespace my-grafana
kubectl apply -f .\grafana.yaml --namespace=my-grafana
kubectl port-forward service/grafana 3000:3000 --namespace==my-grafana
```
Поднимаю прометеус как сервис через НодПорт
```
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
minikube service prometheus-server-ext
```

## Алертменеджер
Для алертов был создан бот + канал в тг, куда все алерты будут прилетать:


был скопирован репозиторий с базовой настройкой готового алертменеджера:
```
git clone https://github.com/bibinwilson/kubernetes-alert-manager.git
```
Единственный конфигурируемый файл - AlertManagerConfigmap.yaml в нем были указаны данные канала и токен бота (бот вместе с токеном уже удален, не было времени настраивать сикреты и енв)

Были созданы объекты кластера в поддятнутом репозитории с помощью этих комманд:
```
 kubectl create -f .\AlertManagerConfigmap.yaml
configmap/alertmanager-config created
kubectl create -f .\AlertTemplateConfigMap.yaml
configmap/alertmanager-templates created
kubectl create -f .\Deployment.yaml
deployment.apps/alertmanager created
kubectl create -f .\Service.yaml
service/alertmanager created
```
Была найдена нужнавя пода и запущен алерт-менеджер:


В телеграмм сразу же пришло типовое сообщение:

