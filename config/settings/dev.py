import environ
from .base import *

env = environ.Env(
    DEBUG=(bool, True)
)

environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY', default='your-default-secret-key')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME', default='workfluent_db'),
        'USER': env('DATABASE_USER', default='workfluent_user'),
        'PASSWORD': env('DATABASE_PASSWORD', default='secure_password'),
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'fallback': env.db(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')  # Fetch from environment
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')  # Fetch from environment
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
