# frontend/Dockerfile
FROM node:18 AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Финальный образ для копирования файлов (как в Taski)
FROM alpine:latest

# Копируем собранные файлы
COPY --from=builder /app/build /usr/share/nginx/html

# Простая команда для копирования в volume
CMD ["cp", "-r", "/usr/share/nginx/html/.", "/frontend_static/"]