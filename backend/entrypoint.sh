set -e

if [ "$DB_HOST" ]; then
    echo "Waiting for database..."
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    echo "Database started"
fi

python manage.py migrate --noinput

python manage.py collectstatic --noinput

if [ -d "/app/collected_static" ]; then
    cp -r /app/collected_static/. /backend_static/ 2>/dev/null || true
fi

exec gunicorn kittygram_backend.wsgi:application --bind 0.0.0.0:8000