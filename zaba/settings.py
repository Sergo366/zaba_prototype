"""
Django settings for zaba project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*$#z=yb+z(vegr!k(*2!!(4$1o#qb)1m5m)8@*!r$rsvq!7ddg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    'django.contrib.sites',
    'django_extensions',
    'mptt',
    'django_countries',
    'django_tables2',
    # view
    'crispy_forms',
    # Models
    'account.apps.AccountConfig',
    'adverts.apps.AdvertsConfig',
    'rents.apps.RentsConfig',
    'jobs.apps.JobsConfig',
    'items.apps.ItemsConfig',
    'gifts.apps.GiftsConfig',
    'language_flags',
    'rosetta',
    'debug_toolbar',
    #social
    'social_django',


]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
)

SITE_ID = 1

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # my
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'zaba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'zaba.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     os.path.join(BASE_DIR, "adverts/static"),
# ]

INTERNAL_IPS = ['127.0.0.1']

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('pl', 'Polish'),
    ('uk', 'Ukrainian'),

)

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

COUNTRIES_ONLY = ['UA', 'RU', 'PL', 'US']


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'pl', 'uk')

MODELTRANSLATION_TRANSLATION_FILES = (
    'gifts.translation', 'jobs.translation',)



REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0


CRISPY_TEMPLATE_PACK = 'bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "XXX" # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX' # Google Consumer Secret
SOCIAL_AUTH_TWITTER_KEY = 'XXX' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'XXX' # Twitter Consumer Secret