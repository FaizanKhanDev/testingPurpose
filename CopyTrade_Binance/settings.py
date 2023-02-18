import os
from pathlib import Path
from CopyTrade_Binance.packages.all_auth_settings import * #noqa
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w^sqx%b#86olk!p35--02!17#qk=tf)@w73p)w4-u$&&iktnt0'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

###EMAIL DETAILS###

DEFAULT_FROM_EMAIL = ''
EMAIL_USE_SSL = True
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''  
EMAIL_PORT = 465

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# Application definition

INSTALLED_APPS = [
    # Django
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    # Apps
    'Bot',
    'Users',

    # Third parties
    'widget_tweaks',
    'tinymce',
    'fontawesomefree',
    'crispy_forms',
    "allauth",
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'CopyTrade_Binance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'CopyTrade_Binance.wsgi.application'

# Database
# import dj_database_url
#
# DATABASES = {'default': dj_database_url.config()}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

SITE_ID = 2

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Users.User'

# SIMPLEUI_CONFIG = {
#     'system_keep': False,
#     'menus': [{
#         'name': 'Bot',
#         'icon': 'fab fa-android',
#         'models': [{
#             'name': 'TRADERS',
#             'url': 'Users/trader/',
#             'icon': 'fas fa-user-ninja'
#         }, {
#             'name': 'Users',
#             'icon': 'fa fa-user',
#             'url': 'Users/user/'
#         },
#             {
#                 'name': 'Orders',
#                 'url': 'Users/order/',
#                 'icon': 'fas fa-chart-line'
#             },
          
#              ],
#     },
#     {
#         'name': 'allauth',
#         'icon': 'fab fa-globe',
#         'models': [{
#             'name': 'SocialAccount',
#             'icon': 'fas fa-google',
#             'url': 'socialaccount/socialaccount/'
#         }, {
#             'name': 'SocialApp',
#             'icon': 'fa fa-user',
#             'url': 'socialaccount/socialapp/'
#         },
#            {
#                'name': 'SocialToken',
#                'url': 'socialaccount/socialtoken/',
#                'icon': 'fas fa-chart-line'
#            },
          
#              ],
#     },
    
#      {
#         'app': 'auth',
#         'name': 'Permission',
#         'icon': 'fas fa-user-shield',
#         'models': [{
#             'name': 'Group',
#             'icon': 'fas fa-users',
#             'url': 'auth/group/'
#         }]
#     }, {
#         'app': 'sites',
#         'name': 'Sites',
#         'icon': 'fas fa-globe',
#         'models': [{
#             'name': 'Sites',
#             'icon': 'fas fa-globe',
#             'url': 'sites/site/'
#         }]
#     }, {
#         'app': 'allauth',
#         'name': 'Social',
#         'icon': 'fas fa-google',
#         'models': [{
#             'name': 'SocialAccount',
#             'icon': 'fas fa-google',
#             'url': 'socialaccount/socialaccount/'
#         }]
#     }, ]
# }



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# TODO: Remove this before pushing

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]