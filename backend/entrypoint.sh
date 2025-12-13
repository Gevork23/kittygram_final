#!/bin/sh

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 kittygram_backend.wsgi