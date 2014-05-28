# Django settings for example project.

import os

LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@polling.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'altauth_test.sqlite3db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-Ru'


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://polling.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), '../static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h32z)k0^nx9b+s(ec9*u05=%esmk!+r_%nz_*034iep@@b5+2k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'polling.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'polling.wsgi.application'

TEMPLATE_DIRS = (
    'polling/templates',
    'altauth/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'altauth',
    'polling',
    'django.contrib.admin',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'altauth.auth_backends.AlternativePasswordBackend',
                           'altauth.auth_backends.PublicKeyBackend',
                            )



ALTAUTH_RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2T48dI0Cp5YpMyev4b/zjm+GL
Vm10xXOEaBf+wZAJPFgvWp6dpUsEyDB84KIS89DvMQkC/2edv0ejOHVhlvNnlTYa
BgoJ6PaQnhpdvgJYEIJIAJAhoIl19VTUrJ1XFcYFE1hEtqNo8NPymNnTV+IzBR7J
nE2rkdUITGZX88qIIQIDAQAB
-----END PUBLIC KEY-----
"""

ALTAUTH_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQC2T48dI0Cp5YpMyev4b/zjm+GLVm10xXOEaBf+wZAJPFgvWp6d
pUsEyDB84KIS89DvMQkC/2edv0ejOHVhlvNnlTYaBgoJ6PaQnhpdvgJYEIJIAJAh
oIl19VTUrJ1XFcYFE1hEtqNo8NPymNnTV+IzBR7JnE2rkdUITGZX88qIIQIDAQAB
AoGAZK83mJ35flr4sEPsAD7I6WMTgwJuXMkXbQ6YAegghhk/kpd3dhTtg2yT6sOc
ft8Miq0IDxHCxcn35Fqv6P+W2LLbSIwpYDId5PUdPTSe8rycwj0S3v4yNPf1LGBU
B/jypI3japLZEY/PnDvzBIBrb6l9uAoM4afe18e3H931zYECQQD5uFKTTdIkshc9
UaK6RAn+B3cfT52+jO2NWTR5SAGIzg1GLxeg2prC/G2z/I1q95Sa0hxN0BNoE92J
47LmOjnZAkEAuuVC4DnKDc/VNOp+p5hl9CeBEcPRWlFi6wtlbW2UCmzRP/StVK4U
qY3ubRwUAhuMmU+fZxkeE/AbHEKfeMdLiQJAY4fU2cNVs6yL2LPWARmnRemh0AgC
nnU7JXBdms1ZVzaRUdzpNQKMVpUYAHnzv6OoRkDiaR067uukDBaGMn8YmQJAPawN
h2RKcohUeKOwq6k0a37lrnEJkl4s4Bbgn117bn0+B3a8A6d2FgVJ2iNbzt48ZRLL
LQAy1q1ypL6vVPGe0QJAPcYC8dEJsuSxCW+0MTN3npNA74qIGCzj8umPQasJu6+r
ZSQl4f5GZTZDlwPm4zs8ztHXWRWABBbthMJH8jNb4A==
-----END RSA PRIVATE KEY-----"""

# Alternatively, you can simply use: open(os.path.expanduser('~') + '.ssh/id_rsa').read()

#ALTAUTH_RSA_PUBLIC_KEY = open(os.path.expanduser('~') + '/.ssh/id_rsa.pub').read()
#ALTAUTH_RSA_PRIVATE_KEY = open(os.path.expanduser('~') + '/.ssh/id_rsa').read()
