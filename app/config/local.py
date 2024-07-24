import os

from decouple import config

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    SECRET_KEY = 'TuClaveSecretaGeneradaAleatoriamenteAquí'
    ALLOWED_HOSTS = ["*"]

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.sendgrid.net')
    EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'pytest_django',
    ]
    TEST_RUNNER = 'pytest_django.runner.PytestTestRunner'

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'app.sqlite3'),
        }
    }

