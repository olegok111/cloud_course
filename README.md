### Сборка контейнеров

- `docker build . -f app.Dockerfile -t todoapp-app`
- `docker build . -f db.Dockerfile -t todoapp-db`

### Запуск на minikube

- `kubectl apply -f deployment-todoapp-app.yaml`
- `kubectl expose pod todoapp-app-pod --name=todoapp --port=5000 --target-port=5000`

### Открытие порта сервиса для доступа по localhost:5000

- `kubectl port-forward service/todoapp 5000:5000`
