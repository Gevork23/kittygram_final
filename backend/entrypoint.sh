# backend/entrypoint.sh должен быть:
#!/bin/bash

# Миграции
python manage.py migrate --noinput

# Сбор статики
python manage.py collectstatic --noinput

# Запуск Gunicorn
exec gunicorn kittygram_backend.wsgi:application --bind 0.0.0.0:8000