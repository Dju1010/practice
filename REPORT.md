# Отчёт по практике

**Студент:** Александров Дьулус Александрович  
**Группа:** ММПМИ-24

## 1. Цель практики

Изучить основы веб-разработки на Python, освоить создание REST API,
работу с базами данных, тестирование и деплой приложений.

## 2. Задачи

1. Установить и настроить рабочее окружение (VS Code, Git, Python).
2. Освоить работу с виртуальным окружением и pip.
3. Изучить основы Git и GitHub.
4. Повторить Python: функции, структуры данных, файлы.
5. Изучить HTTP, REST API, CORS.
6. Освоить Flask и SQLAlchemy.
7. Создать CRUD API для управления заметками.
8. Написать unit-тесты (pytest).
9. Задеплоить проект.

## 3. Используемые технологии

- Язык: Python 3.12
- Фреймворк: Flask
- ORM: Flask-SQLAlchemy
- БД: PostgreSQL (локально), SQLite (на Render)
- Тесты: pytest
- Контроль версий: Git, GitHub
- Контейнеризация: Docker
- IDE: VS Code

## 4. Ход работы

### 4.1. Настройка окружения

Установил Python 3.12, Git, VS Code. Создал папку проекта,
инициализировал виртуальное окружение:

python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask flask-sqlalchemy pytest

Список зависимостей сохранён в requirements.txt через pip freeze.

### 4.2. Обработчик логов

Написал скрипт logs_processor.py, который читает app.log
и подсчитывает количество записей по уровням логирования
двумя способами:
- вложенными циклами (O(n*m));
- через Counter за один проход (O(n)).

Второй вариант работает быстрее на больших файлах.

### 4.3. REST API для заметок

Создал модель Note (id, title, body, created_at).
Реализовал CRUD-эндпоинты во Flask:

| Метод  | URL         | Описание              |
|--------|-------------|-----------------------|
| GET    | /notes      | Список всех заметок   |
| POST   | /notes      | Создать заметку       |
| GET    | /notes/<id> | Получить одну заметку |
| PUT    | /notes/<id> | Обновить заметку      |
| DELETE | /notes/<id> | Удалить заметку       |

Дополнительно добавлены:
- пагинация (GET /notes?page=1&size=10);
- поиск по названию (GET /notes?search=...);
- вторая таблица Tag со связью к Note (теги).

### 4.4. Работа с PostgreSQL

Для локальной разработки использован PostgreSQL 16.
Подключение настроено через DBeaver — в базе notes_db
созданы таблицы note и tag (автоматически через SQLAlchemy).

Подключение вынесено в переменную окружения DATABASE_URL:
- локально: postgresql://postgres@localhost:5432/notes_db
- на Render: переменная не задана, используется SQLite

Это позволяет одному и тому же коду работать с разными БД.

В файле sql_queries.py показаны прямые SQL-запросы:
SELECT, INSERT, UPDATE, DELETE, JOIN.

### 4.5. Тестирование

Написал 9 unit-тестов с pytest:
- пустой список;
- создание заметки;
- получение заметки по id;
- обновление;
- удаление;
- обработка 404;
- создание заметки с тегами;
- пагинация;
- поиск.

Все тесты проходят (9 passed).

### 4.6. Git и GitHub

Инициализировал репозиторий, настроил .gitignore,
запушил код на GitHub:
https://github.com/Dju1010/practice

### 4.7. Docker

Написал Dockerfile на базе python:3.12-slim.
Сборка и запуск:

docker build -t notes-api .
docker run -e PORT=8000 -p 8000:8000 notes-api

### 4.8. Деплой на Render

Задеплоил проект на Render (free tier) через GitHub.

Настройки:
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
- Runtime: Python 3.12
- Region: Frankfurt

Демо-ссылка: https://practice-dpv9.onrender.com/notes

## 5. Результат

- Работающее REST API с 5 эндпоинтами.
- 9 unit-тестов (pytest).
- Скрипт обработки логов.
- Работа с PostgreSQL через DBeaver (2 таблицы: note, tag).
- Docker-образ собирается и запускается.
- Деплой на Render (free tier).
- Репозиторий на GitHub.
- Документация (README.md, REPORT.md).

Демо: https://practice-dpv9.onrender.com/notes

## Приложение

Ссылка на репозиторий: https://github.com/Dju1010/practice