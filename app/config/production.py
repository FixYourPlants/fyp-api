import os

import dj_database_url
from decouple import config


from .common import Common


class Production(Common):
    DEBUG = False

    ALLOWED_HOSTS = [
        i
        for i in list(config('DJANGO_ALLOWED_HOSTS', default='*').split(','))
        if i not in ['*', '']
    ]
    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.sendgrid.net')
    EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)

    # CORS settings
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'Strict'
    CORS_ALLOWED_ORIGINS = [i for i in list(config('CORS_ALLOWED_ORIGINS', default='*').split(',')) if i not in ['*', '']]
    CSRF_TRUSTED_ORIGINS  = [i for i in list(config('CORS_ALLOWED_ORIGINS', default='*').split(',')) if i not in ['*', '']]
    if config('CRACK', default='False') == 'True':
        raise Exception(CORS_ALLOWED_ORIGINS)
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL', default='postgres://localhost'))
    }
    print(DATABASES)

