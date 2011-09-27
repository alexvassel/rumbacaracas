FIXTURE_DIRS = ( 
   '/www/rumba/rumbacaracas/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/www/rumba/rumbacaracas/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldcaracas/processed'

OLDDATABOGOTA_PHOTO_PATH = '/www/rumba/rumbacaracas/olddata/'
FAKE_IMPORT_IMAGE = '/home/maksim/test_images/tst_imgs/1.jpg'


FULL_BASE_URL = 'http://localhost:8000/'

MEDIA_ROOT = '/www/rumba/rumbacaracas/media'

STATIC_DOC_ROOT = '/www/rumba/rumbacaracas/static/'

LOCALE_PATHS = ( 
    '/www/rumba/rumbacaracas/locale/',
 )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cydemAjD', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oldcaracasdata', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
    }
}

DEBUG=True
#LANGUAGE_CODE = 'es'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'rumbacar',
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

FACEBOOK_APP_ID = '148108908569986'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '56fa7f47fe58a05ba2659f812c11f7d4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
 )

# Amazon S3 configs
DEFAULT_FILE_STORAGE = 'cuddlybuddly.storage.s3.S3Storage'
AWS_ACCESS_KEY_ID = 'AKIAJAVN6BXUTZ3VMAVA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rumba_test'

from django.utils.http import  http_date
from time import time

AWS_HEADERS = [
    ('^private/', {
        'x-amz-acl': 'private',
        'Expires': 'Thu, 15 Apr 2000 20:00:00 GMT',
        'Cache-Control': 'private, max-age=0'
    }),
    ('.*', {
        'x-amz-acl': 'public-read',
        'Expires': http_date(time() + 31556926),
        'Cache-Control': 'public, max-age=31556926'
    })
]

from cuddlybuddly.storage.s3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.PATH

CUDDLYBUDDLY_STORAGE_S3_CACHE = 'storage_cache.DjangoCache'
CUDDLYBUDDLY_STORAGE_S3_CACHE_BACKEND = 'default'
CUDDLYBUDDLY_STORAGE_S3_CACHE_TIMEOUT = 31556926

MEDIA_URL = 'http://s3.amazonaws.com/rumba_test/'

# Config compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ROOT        = "/www/rumba/rumbacaracas/static/"
STATIC_ROOT          = COMPRESS_ROOT
COMPRESS_URL         = "http://s3.amazonaws.com/rumba_test/static/"
STATIC_URL           = COMPRESS_URL
STATICFILES_STORAGE  = DEFAULT_FILE_STORAGE
COMPRESS_OUTPUT_DIR  = 'CACHE'

COMPRESS_YUI_BINARY  = 'java -jar /www/rumba/rumbacaracas/yuicompressor-2.4.6.jar'
COMPRESS_CSS_FILTERS = ['main.compressor.filters.css_default.CustomCssAbsoluteFilter', 'compressor.filters.yui.YUICSSFilter']
COMPRESS_JS_FILTERS  = ['compressor.filters.yui.YUIJSFilter']
COMPRESS_STORAGE     = 'main.cuddlybuddly.storage.s3.storage.CustomS3Storage'
