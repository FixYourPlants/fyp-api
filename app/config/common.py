import os
from distutils.util import strtobool
from os.path import join

from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    INSTALLED_APPS = (
        'jazzmin',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',  # utilities for rest apis
        'drf_yasg',  # swagger
        'rest_framework.authtoken',  # token authentication
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth',
        'dj_rest_auth.registration',
        'django_filters',  # for filtering rest endpoints

        # Your apps
        'app.users',
        'app.plants',
        'app.sickness',
        'app.diary',
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'allauth.account.middleware.AccountMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # Allauth configuration
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    SITE_ID = 1

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = 'app.urls'
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'app.wsgi.application'

    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_USERNAME_REQUIRED = False

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    ADMINS = (
        ('Author', 'alesanfel@us.es'),
    )

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
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

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
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

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Custom user app
    AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
    }

    # Jazzmin admin settings
    JAZZMIN_SETTINGS = {
        # title of the window (Will default to current_admin_site.site_title if absent or None)
        "site_title": "FixYourPlants Admin",

        # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
        "site_header": "FixYOurPlants",

        # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
        "site_brand": "FixYourPlants",

        # Logo to use for your site, must be present in static files, used for brand on top left
        "site_logo": None,

        # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
        "login_logo": None,

        # Logo to use for login form in dark themes (defaults to login_logo)
        "login_logo_dark": None,

        # CSS classes that are applied to the logo above
        "site_logo_classes": "img-circle",

        # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
        "site_icon": None,

        # Welcome text on the login screen
        "welcome_sign": "Welcome to FixYourPlants",

        # Copyright on the footer
        "copyright": "FixYourPlants Ltd",

        # List of model admins to search from the search bar, search bar omitted if excluded
        # If you want to use a single search field you dont need to use a list, you can use a simple string
        "search_model": ["users.User", "plant.Plant"],

        # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
        "user_avatar": None,

        ############
        # Top Menu #
        ############

        # Links to put along the top menu
        "topmenu_links": [

            # Url that gets reversed (Permissions can be added)
            {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

            # external url that opens in a new window (Permissions can be added)
            {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

            # model admin to link to (Permissions checked against model)
            {"model": "auth.User"},
        ],

        #############
        # User Menu #
        #############

        # Additional links to include in the user menu on the top right ("app" url type is not allowed)
        "usermenu_links": [
            {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
            {"model": "auth.user"}
        ],

        #############
        # Side Menu #
        #############

        # Whether to display the side menu
        "show_sidebar": True,

        # Whether to aut expand the menu
        "navigation_expanded": True,

        # Hide these apps when generating side menu e.g (auth)
        "hide_apps": [],

        # Hide these models when generating side menu (e.g auth.user)
        "hide_models": [],

        # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
        "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

        # Custom links to append to app groups, keyed on app name
       '''
        "custom_links": {
            "books": [{
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"]
            }]
        },
        '''

        # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
        # for the full list of 5.13.0 free icon classes
        '''
        "icons": {
            "auth": "fas fa-users-cog",
            "auth.user": "fas fa-user",
            "auth.Group": "fas fa-users",
        },
        '''
        
        # Icons that are used when one is not manually specified
        "default_icon_parents": "fas fa-chevron-circle-right",
        "default_icon_children": "fas fa-circle",

        #################
        # Related Modal #
        #################
        # Use modals instead of popups
        "related_modal_active": False,

        #############
        # UI Tweaks #
        #############
        # Relative paths to custom CSS/JS scripts (must be present in static files)
        "custom_css": None,
        "custom_js": None,
        # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
        "use_google_fonts_cdn": True,
        # Whether to show the UI customizer on the sidebar
        "show_ui_builder": False,

        ###############
        # Change view #
        ###############
        # Render out the change view as a single form, or in tabs, current options are
        # - single
        # - horizontal_tabs (default)
        # - vertical_tabs
        # - collapsible
        # - carousel
        "changeform_format": "horizontal_tabs",
        # override change forms on a per modeladmin basis
        # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
        # Add a language dropdown into the admin
        "language_chooser": False,
    }