# Notes API

🔗 **Демо:** https://practice-dpv9.onrender.com/notes

REST API для управления заметками на Flask + SQLite.  
Учебный проект по практике.

## Стек технологий

- Python 3.12
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest
- Git / GitHub

## Структура проекта

```
practice/
├── app.py              # Flask-приложение и роуты
├── models.py           # Модель Note
├── logs_processor.py   # Скрипт-обработчик логов
├── app.log             # Пример лог-файла
├── requirements.txt    # Зависимости
├── README.md           # Документация
├── tests/
│   ├── __init__.py
│   └── test_api.py     # Тесты API
└── .gitignore
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

```
pip install -r requirements.txt
```

### 4. Запустить приложение

```
python app.py
```

Сервер запустится на `http://127.0.0.1:5000`.

---

## Эндпоинты API

| Метод  | URL              | Описание              |
|--------|------------------|-----------------------|
| GET    | `/notes`         | Список всех заметок   |
| POST   | `/notes`         | Создать заметку       |
| GET    | `/notes/<id>`    | Получить одну заметку |
| PUT    | `/notes/<id>`    | Обновить заметку      |
| DELETE | `/notes/<id>`    | Удалить заметку       |

---

## Примеры запросов

### PowerShell

**Получить список заметок:**

```powershell
Invoke-RestMethod http://127.0.0.1:5000/notes
```

**Создать заметку:**

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"title":"Buy bread","body":"until 6pm"}'
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

Ожидаемый результат: `6 passed`.

---

## Обработчик логов

```
python logs_processor.py
```

Скрипт читает `app.log` и подсчитывает количество записей по уровням
(INFO, WARNING, ERROR, DEBUG) двумя способами:

- вложенными циклами (медленно);
- через `Counter` за один проход (быстро).

---
## Деплой

Проект задеплоен на **Render** (free tier).

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Runtime: Python 3.12
- Region: Frankfurt

**Демо:** https://practice-dpv9.onrender.com/notes

### Docker (локально)

docker build -t notes-api .
docker run -p 8000:8000 notes-api

## Автор

**Dju1010**  
GitHub: https://github.com/Dju1010