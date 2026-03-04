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