# backend/kittygram_backend/test_settings.py
from .settings import *
import os

# Используем SQLite для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Ускоряем тесты
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Отключаем для тестов
DEBUG = True
SECRET_KEY = 'test-secret-key-for-ci'