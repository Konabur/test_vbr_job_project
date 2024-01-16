# Event Management API

Проект представляет собой API для управления организациями и мероприятиями.

<<<<<<< HEAD
## Документация

Документация API доступна в формате Swagger и ReDoc:

- [Swagger (интерактивная)](http://localhost:8000/core/swagger/)
- [ReDoc (простой)](http://localhost:8000/core/redoc/)


=======
>>>>>>> 1cd1998729f21a30cfae744be7a60ee07fb1bac0
## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/your_username/event-management-api.git
    cd event-management-api
    ```

2. Установить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Выполнить миграции:

    ```bash
    python manage.py migrate
    ```

4. Запустить сервер:

    ```bash
    python manage.py runserver
    ```

## Использование

### Регистрация пользователя

Отправить POST-запрос на `/core/api/create_user/` с данными пользователя в формате JSON.

Пример:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"example_user","email":"user@example.com","phone_number":"1234567890","password":"secure_password"}' http://localhost:8000/core/api/create_user/
```

### Аутентификация пользователя

Для аутентификации пользователя и получения токена, реализовано использование Refresh Token. После успешной регистрации, вы можете использовать следующий запрос для получения Access Token:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"example_user","password":"secure_password"}' http://localhost:8000/token/refresh/
```
<<<<<<< HEAD

=======
>>>>>>> 1cd1998729f21a30cfae744be7a60ee07fb1bac0
