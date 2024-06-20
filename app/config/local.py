import os

import dj_database_url

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    SECRET_KEY = 'TuClaveSecretaGeneradaAleatoriamenteAquí'
    ALLOWED_HOSTS = ["*"]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=app'
    ]

    # Database
    DATABASES = {
        'default': dj_database_url.config(default=f"sqlite:///{os.path.join(BASE_DIR, 'app.sqlite3')}")
    }
