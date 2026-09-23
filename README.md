# Notes API

🔗 **Демо:** https://practice-dpv9.onrender.com/notes

REST API для управления заметками на Flask + PostgreSQL/SQLite.  
Учебный проект по практике.

## Стек технологий

- Python 3.12
- Flask
- Flask-SQLAlchemy
- PostgreSQL (локально)
- SQLite (на Render)
- pytest
- Git / GitHub
- Docker

## Структура проекта

```
practice/
├── app.py               # Flask-приложение и роуты
├── models.py            # Модели Note и Tag
├── logs_processor.py    # Скрипт-обработчик логов
├── sql_queries.py       # Примеры SQL-запросов
├── app.log              # Пример лог-файла
├── requirements.txt     # Зависимости
├── Procfile             # Команда запуска для Render
├── runtime.txt          # Версия Python для Render
├── Dockerfile           # Для локального запуска в контейнере
├── .dockerignore
├── .gitignore
├── README.md            # Документация
├── REPORT.md            # Отчёт по практике
└── tests/
    ├── __init__.py
    └── test_api.py      # Тесты API
```

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Dju1010/practice.git
cd practice
```

### 2. Создать виртуальное окружение

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить приложение

```bash
python app.py
```

Сервер запустится на `http://127.0.0.1:5000`.

```powershell
$env:DATABASE_URL = "postgresql://postgres@localhost:5432/notes_db"
python app.py
```

---

## Эндпоинты API

| Метод  | URL                          | Описание                          |
|--------|------------------------------|-----------------------------------|
| GET    | `/notes`                     | Список всех заметок               |
| GET    | `/notes?page=1&size=10`      | Пагинация                         |
| GET    | `/notes?search=bread`        | Поиск по названию                 |
| POST   | `/notes`                     | Создать заметку (с тегами)        |
| GET    | `/notes/<id>`                | Получить одну заметку             |
| PUT    | `/notes/<id>`                | Обновить заметку                  |
| DELETE | `/notes/<id>`                | Удалить заметку                   |

---

## Примеры запросов

### PowerShell

**Получить список заметок:**

```powershell
Invoke-RestMethod http://127.0.0.1:5000/notes
```

**Пагинация:**

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/notes?page=1&size=5"
```

**Поиск:**

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/notes?search=bread"
```

**Создать заметку с тегами:**

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"title":"Buy bread","body":"until 6pm","tags":["shopping","food"]}'
```

**Получить одну заметку:**

```powershell
Invoke-RestMethod http://127.0.0.1:5000/notes/1
```

**Обновить заметку:**

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes/1 `
  -Method Put `
  -ContentType "application/json" `
  -Body '{"title":"Buy milk"}'
```

**Удалить заметку:**

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes/1 -Method Delete
```

---

## Тесты

```bash
python -m pytest tests/ -v
```

Ожидаемый результат: `9 passed`.

---

## Обработчик логов

```bash
python logs_processor.py
```

Скрипт читает `app.log` и подсчитывает количество записей по уровням
(INFO, WARNING, ERROR, DEBUG) двумя способами:

- вложенными циклами (медленно);
- через `Counter` за один проход (быстро).

---

## SQL-запросы

```bash
python sql_queries.py
```

Файл `sql_queries.py` демонстрирует прямые запросы к PostgreSQL:
SELECT, INSERT, UPDATE, DELETE, JOIN.

---

## Деплой

Проект задеплоен на **Render** (free tier).

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Runtime: Python 3.12
- Region: Frankfurt

**Демо:** https://practice-dpv9.onrender.com/notes

### Docker (локально)

```bash
docker build -t notes-api .
docker run -e PORT=8000 -p 8000:8000 notes-api
```

---

## Автор

**Dju1010**  
GitHub: https://github.com/Dju1010