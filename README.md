# Game Blog

Simple Django project scaffold.

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
./.venv/Scripts/python.exe -m pip install -r requirements.txt
```

3. Create `env.py` and set `SECRET_KEY` (and `DATABASE_URL` if using Postgres).
4. Apply migrations:

```bash
./.venv/Scripts/python.exe manage.py migrate
```

5. Run the dev server:

```bash
./.venv/Scripts/python.exe manage.py runserver
```

Visit http://127.0.0.1:8000/blog/

## Getting started (quick)

```bash
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe manage.py migrate
./.venv/Scripts/python.exe manage.py runserver
```

## Deployment

The Procfile uses Gunicorn. Make sure `gunicorn` is in `requirements.txt` before deploying.
