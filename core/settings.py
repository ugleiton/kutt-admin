"""
Django settings for kuttadmin project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY','django-insecure-$saci2f8vy@taqi8h-88n8@p48j_ii$c5)^4nl1gx0*3px4tf-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG',False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kutt'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DATABASE_HOST','localhost'),
        'NAME': os.getenv('POSTGRES_DB','djangodb'),
        'USER': os.getenv('POSTGRES_USER','djangousr'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD','djangopw'),
        'CONN_MAX_AGE':600,
    },
    'kuttdatabase': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DATABASEKUTT_HOST','localhost'),
        'NAME': os.getenv('POSTGRESKUTT_DB','kuttdb'),
        'USER': os.getenv('POSTGRESKUTT_USER','kuttusr'),
        'PASSWORD': os.getenv('POSTGRESKUTT_PASSWORD','kuttpw'),
        'CONN_MAX_AGE':600,
    }}

DATABASE_ROUTERS = ['core.routes_db.DjangoRouter' ]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'America/Sao_Paulo'

DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'staticfiles'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Config SimpleUi
SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menus': [
        {
            'app': 'auth',
            'name': 'Acesso Admin',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': 'Administradores',
                    'icon': 'fa fa-user-cog',
                    'url': 'auth/user/'
                }]
        }, 
        {
        'name': 'Kutt',
        'icon': 'fa fa-cogs',
        'models': [
          {
            'name': 'Usuários',
            'url': 'kutt/users/',
            'icon': 'fa fa-users'
        }]
    }]
}



# SIMPLEUI_ICON = {
#     'Kutt': 'fas fa-cogs',
#     'Links': 'fa fa-link',
#     'Usuários': 'fa fa-user-tie',
# }

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_LOGO = os.getenv('SITE_LOGO','https://avatars2.githubusercontent.com/u/13655483?s=60&v=4')