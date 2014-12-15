"""
Django settings for basemgd project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=m(g#+3g+un6nt97%hmzc#$!9^jc0j1h#%y=1#tf1ri&+)jl(&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'mongoengine.django.mongo_auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
)

AUTH_USER_MODEL = 'mongo_auth.MongoUser'



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djmongo.urls'

WSGI_APPLICATION = 'djmongo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Database
import mongoengine


DATABASES = {
   'default' : {
      #'ENGINE' : 'django_mongodb_engine',
      'ENGINE' : 'django.db.backends.dummy',
#      'NAME' : 'images',
#      'USER' : 'mongo',
#      'PASSWORD': 'mongo',
#      'HOST': '127.0.0.1',
#      'PORT': '27017',
#      'SUPPORTS_TRANSACTIONS': False
}
}

SESSION_ENGINE = 'mongoengine.django.sessions' # optional
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'


_MONGODB_USER = 'mongo'
_MONGODB_PASSWD = 'mongo'
_MONGODB_HOST = '127.0.0.1:27017'
_MONGODB_NAME = 'images'
_MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
#_MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

TEST_RUNNER = 'base.tests.NoSQLTestRunner'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL =  '/media/'

