# Django settings for refcollections project.

import sys
from os.path import abspath, basename, dirname, join, normpath

from helpers import gen_secret_key

########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory
DJANGO_ROOT = dirname(dirname(dirname(abspath(__file__))))

# Template Directory
TEMPLATE_DIRS = (
    DJANGO_ROOT + '/templates',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = normpath(join(DJANGO_ROOT, '../public/media'))

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = normpath(join(DJANGO_ROOT, '../public/static'))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
SECRET_FILE = normpath(join(DJANGO_ROOT, 'deploy', 'SECRET'))


########## END PATH CONFIGURATION


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'shells',                      # Or path to database file if using sqlite3.
        'USER': 'shells',                      # Not used with sqlite3.
        'PASSWORD': 'shells',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Brisbane'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

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

ROOT_URLCONF = 'refcollections.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'refcollections.wsgi.application'


INSTALLED_APPS = (
### Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',


### Third party apps
    'haystack',
    'easy_thumbnails',


### Parts of this app
    'shells',
    'bulkimport',
    'mediaman',
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


########## KEY CONFIGURATION
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        SECRET_KEY = gen_secret_key(50)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
########## END KEY CONFIGURATION


##### HAYSTACK CONFIGURATION
HAYSTACK_SITECONF = 'refcollections.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = join(DJANGO_ROOT, 'deploy', 'search_index')


# This normally protects against XSS attacks, which shouldn't be a problem here.
# If enabled, it interrupts the bulk upload functionality.
SESSION_COOKIE_HTTPONLY = False


THUMBNAIL_ALIASES = {
    '': {
        'large_display': {
            'size': (1024, 768),
            'watermark_image': 'watermark-large.png',
            'wm_margin': 15,
        },
        'item_display': {
            'size': (384, 256),
            'watermark_image': 'watermark-small.png',
            'wm_margin': 5,

        },
        'small_thumb': {
            'size': (105, 70),
            'expand': True,
        },
        'large_thumb': {
            'size': (180, 120),
            'expand': True,
        }
    }
}