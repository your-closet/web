"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, base64, json
from cryptography.fernet import Fernet

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hc-v2@p7orgf(fqlv$%fs4b^@0s4nmfi0tvxs(6fz43*2i@)*&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

WRITE_KEYS = False
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    DEBUG = True
    try:
        with open("keys.json") as f:
            SECRET_KEY = json.loads(f.read()).get("SECRET_KEY")
    except FileNotFoundError:
        SECRET_KEY = Fernet.generate_key().decode()
        WRITE_KEYS = True

FERNET_KEY = os.environ.get("FERNET_KEY")
if not FERNET_KEY:
    DEBUG = True

    try:
        with open("keys.json") as f:
            SECRET_PASS_CRYPT = Fernet(json.loads(f.read()).get("FERNET_KEY").encode())
    except FileNotFoundError:
        FERNET_KEY = Fernet.generate_key().decode()
        SECRET_PASS_CRYPT = Fernet(FERNET_KEY.encode())
        WRITE_KEYS = True

if WRITE_KEYS:
    with open("keys.json","w") as f:
        f.write(json.dumps({
            "SECRET_KEY": SECRET_KEY,
            "FERNET_KEY": FERNET_KEY,
        }))


ALLOWED_HOSTS = []
if not DEBUG:
    ALLOWED_HOSTS.append(os.environ.get("HOST"))

LOG_FILE = "./debug.log"
LOG_LEVEL = "DEBUG"
HANDLER = "console"
if not DEBUG:
    HANDLER = "debug"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'debug': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': [HANDLER],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}
# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'public.apps.PublicConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yc_dev' if DEBUG else 'yc',
        'USER': 'yc_user',
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staic/")
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = "/login"