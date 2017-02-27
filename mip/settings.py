"""
Django settings for mip project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
# import passwords

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'buu1w+mav)qme2h&hhl#q5f$^_t)gjc$3bd)))$q@7mx$)ficn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Courses',
    'People',
    'Registrations',
    'Placement'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mip.urls'

WSGI_APPLICATION = 'mip.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# You can use mip/database.json to specify details, which can be excluded
# from a git repository. The format for this is equal to the format that
# Would be put into "DATABASES: {...}"

with open('mip/database.json') as data_file:
    databaseDetails = json.load(data_file)

DATABASES = {
    'default': databaseDetails
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join('static')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = [os.path.join("all-static")]

# LOGIN / AUTH

LOGIN_URL = '/admin-django/login/'

ADMINS = (
    ('Admin Admin', 'admin@domain.com'),
)
