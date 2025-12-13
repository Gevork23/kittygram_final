from pathlib import Path
from .settings import *

BASE_DIR = Path(__file__).resolve().parent.parent

# Use sqlite for tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Disable password hashing for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Test secret key
SECRET_KEY = 'test-secret-key'

# Disable debug for tests
DEBUG = False

# Disable allowed hosts check
ALLOWED_HOSTS = ['testserver']

# Use console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'