"""
Django settings for Projecto1 project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pickle import TRUE
import dj_database_url
import django_heroku
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u!+5zh0i@8d&2(**4)6l)mk&^kh!ewg%)^)0is7gff&^3#@@hk'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

# SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['con-prueba.herokuapp.com', 'localhost']


# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['con-prueba.herokuapp.com', 'localhost']

STATS_FILE = os.path.join(BASE_DIR, 'webpack-stats.json')

# Application definition


INSTALLED_APPS = [
    'corsheaders',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist/static'),
]

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

]

LOCAL_APPS = [
    'apps.users',
    'apps.book',
    'apps.quiz',
    'apps.quizz',
]

THIRD_APPS = [
    'corsheaders',
    # 'automatic_crud',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',
    # 'rest_framework_simplejwt.token_blacklist',
    'simple_history',
    # 'drf_yasg',
    # 'bootstrap4',
    # 'book',
    # 'rest_framework',
    'knox',
    # 'accounts.apps.AccountsConfig',
    'rest_framework_swagger'

]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]


ROOT_URLCONF = 'Projecto1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'Projecto1/templates')],
        'DIRS': [os.path.join(BASE_DIR, 'dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'Projecto1.wsgi.application'

# CSRF_FAILURE_VIEW ='Projecto1.views.csrf_failure'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'chatbot',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}
DATABASE_ROUTERS = ['apps.quiz.routers.MiApp2Router', ]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False


SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'

# DEBUG = False

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# -----coregido para vue
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# ------
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DATABASE_ROUTERS = ['apps.quiz.routers.MiApp2Router', ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'  # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
# os.path.join(BASE_DIR, 'static'),
# )

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}


django_heroku.settings(locals())
