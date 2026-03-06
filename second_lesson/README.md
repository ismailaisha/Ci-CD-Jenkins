# Jenkins Python Demo (Password Checker)

Небольшой учебный проект для практики Jenkins Pipeline.

## Структура
- `app.py` — функции проверки пароля:
  - `password_errors(password)` возвращает список ошибок
  - `check_password(password)` возвращает `weak / medium / strong`
- `tests/test_app.py` — тесты на pytest
- `requirements.txt` — зависимости для тестов
- `Jenkinsfile` — CI pipeline (build/test/deploy)

## Локальный запуск
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q


Jenkins Pipeline Homework

Этапы Pipeline

Build
Устанавливаются зависимости проекта:

python3 -m pip install -r requirements.txt

Test
Запускаются автоматические тесты:

python3 -m pytest -q tests

Deploy
Этап выполняется только если параметр DO_DEPLOY=true.
Deploy имитируется созданием файла с информацией о развертывании.

Параметры

ENV – окружение для deploy (dev, stage, prod)
DO_DEPLOY – включает или отключает этап Deploy

Запуск

Pipeline запускается в Jenkins через Build with Parameters и выполняется на Jenkins-агенте.