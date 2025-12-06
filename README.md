# User Service API

Мини-сервис пользователей на FastAPI — регистрация, логин, профиль, JWT.

## Стек
- FastAPI
- PostgreSQL (asyncpg)
- SQLAlchemy (async)
- JWT (PyJWT)
- passlib (bcrypt)
- Docker / docker-compose

## Быстрый запуск (Docker)
1. Скопируйте `.env.example` в `.env`.
2. Запустите:
```
docker-compose up --build
```
3. Создайте таблицы (в контейнере приложения):
```
docker exec -it user-service-app bash
python -m app.db.init_db
```
4. Откройте Swagger: `http://localhost:8000/docs`

## Основные endpoints
- `POST /api/auth/register` — регистрация
- `POST /api/auth/login` — логин, возвращает access_token
- `GET /api/users/me` — профиль (Bearer token)
- `PATCH /api/users/me` — обновление профиля
- `GET /api/users` — список пользователей (только admin)

## Примечания
- Для простоты реализованы базовые функции без Alembic. Рекомендуется добавить миграции.
- Токены — JWT. Для production смените SECRET_KEY и настройте HTTPS.
