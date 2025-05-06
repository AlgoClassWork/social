# Главные настройки сайта. Здесь указываем, как работает наш проект

import os
from pathlib import Path

# Папка, где лежит проект
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для безопасности (в продакшене храним в переменной окружения)
SECRET_KEY = 'django-insecure-verysecretkey123'

# Режим разработки (True — для тестов)
DEBUG = True

# Какие домены могут обращаться к сайту
ALLOWED_HOSTS = []

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',      # Админ-панель
    'django.contrib.auth',       # Система пользователей
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Сессии
    'django.contrib.messages',   # Сообщения
    'django.contrib.staticfiles', # Статические файлы (CSS, JS)
    'account',                   # Приложение для пользователей
    'images',                    # Приложение для изображений
]

# Программы, которые обрабатывают запросы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный файл маршрутов
ROOT_URLCONF = 'social_website.urls'

# Настройки шаблонов (где искать HTML-файлы)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Папка для общих шаблонов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Для запуска сервера
WSGI_APPLICATION = 'social_website.wsgi.application'

# База данных (SQLite — простая база, файл на компьютере)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Проверка паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Язык и часовой пояс
LANGUAGE_CODE = 'ru-ru'  # Русский язык
TIME_ZONE = 'UTC'        # Универсальное время
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Медиа-файлы (загруженные изображения)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Какой тип первичного ключа использовать
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки авторизации
LOGIN_REDIRECT_URL = 'dashboard'  # Куда идти после входа
LOGOUT_REDIRECT_URL = 'login'    # Куда идти после выхода
LOGIN_URL = 'login'              # Страница входа