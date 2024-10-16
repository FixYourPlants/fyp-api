"""
WSGI config for app project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""
import os

from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config")
os.environ.setdefault("DJANGO_CONFIGURATION", config('DJANGO_CONFIGURATION', default='Production'))

from configurations.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()
