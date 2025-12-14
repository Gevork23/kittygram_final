# backend/Dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x /app/entrypoint.sh

# ИСПРАВИТЬ ЭТУ СТРОКУ:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi:application"]