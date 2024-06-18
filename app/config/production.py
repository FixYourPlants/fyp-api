import os

import dj_database_url
from decouple import config

from .common import Common


class Production(Common):
    DEBUG = False
    ALLOWED_HOSTS = [config('DJANGO_ALLOWED_HOSTS', default='*')]
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL', default='postgres://localhost'))
    }
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.sendgrid.net')
    EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)

    # CORS settings
    CORS_ORIGIN_ALLOW_ALL = True

    # Render specific settings
    RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

