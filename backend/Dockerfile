# Базовый образ с Python
FROM python:3.9

# Чтобы питоновские выводы логов не буферизовались
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория в контейнере
WORKDIR /app

# Обновим pip
RUN pip install --upgrade pip

# Сначала только зависимости — чтобы кешировалось
COPY requirements.txt .

# Ставим зависимости проекта + gunicorn + драйвер PostgreSQL
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn==20.1.0 psycopg2-binary==2.9.3

# Копируем весь backend в контейнер
COPY . .

# Статические/медийные пути внутри контейнера
ENV DJANGO_SETTINGS_MODULE=kittygram_backend.settings

# Команда запуска: gunicorn слушает порт 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi:application"]
