# frontend/Dockerfile
FROM node:18 AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Финальный образ с nginx
FROM nginx:alpine

# Копируем собранные файлы
COPY --from=builder /app/build /usr/share/nginx/html

# Копируем конфиг nginx - исправьте путь если нужно!
COPY nginx.conf /etc/nginx/nginx.conf

# Если файл в той же папке что и Dockerfile, оставьте как есть
# Если nginx.conf в подпапке, укажите путь, например:
# COPY ./config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]