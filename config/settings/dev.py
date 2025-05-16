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
    'default': env.db(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}
