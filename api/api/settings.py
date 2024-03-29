# -*- coding: utf-8 -*-
import environ
from django.utils.translation import ugettext_lazy as _

root = environ.Path(__file__) - 3
env = environ.Env()

BASE_DIR = root()
public_root = root.path('public/')
ADMINS = (
    ('Admin', env('ADMIN_EMAIL')),
)
MANAGERS = ADMINS

DEBUG = env.bool('DEBUG')
DOCS = env.bool('DOCS')
SECRET_KEY = env('SECRET_KEY')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CSRF_COOKIE_DOMAIN = env('COOKIE_DOMAIN')
SESSION_COOKIE_DOMAIN = env('COOKIE_DOMAIN')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Email

EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'sorl.thumbnail',
    'colorful',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    # Apps
    'sw_users',
    'sw_payments',
    'sw_shipments',
    'sw_vehicles',

    # Utils
    'utils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.DisableCSRF',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [public_root('templates')],
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

WSGI_APPLICATION = 'api.wsgi.application'

# SSL
if env.bool('SSL'):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL')
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Celery
TEST = env.bool('TEST')
if TEST:
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

BROKER_URL = env('BROKER_URL')
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env('CACHE'),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'sw_users.UserAccount'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (public_root('locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = (public_root('static'),)
STATIC_ROOT = public_root('staticfiles')
STATIC_URL = env('STATIC_URL')
MEDIA_ROOT = public_root('media')
MEDIA_URL = env('MEDIA_URL')

# Config DRF
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'create_account': env('THROTTLE_RATE_TIME'),
    }
}

if not DOCS:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )

LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'

MAPS_GOOGLE_MAPS_API_KEY = env('MAPS_GOOGLE_MAPS_API_KEY')

STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
