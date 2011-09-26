

FIXTURE_DIRS = (
   '/home/maksim/Documents/Develop/rumbabogota/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldbogota/processed'

OLDDATABOGOTA_PHOTO_PATH = '/mnt/rumbacaracas/www/vhosts/rumbacaracas.com/httpdocs/'
FAKE_IMPORT_IMAGE = '/home/maksim/test_images/tst_imgs/1.jpg'


FULL_BASE_URL = 'http://localhost.td'

MEDIA_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

STATIC_DOC_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

LOCALE_PATHS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/locale/',
 )



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oldcaracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
    }
}

DEBUG=True
#LANGUAGE_CODE = 'es'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'storage': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'caracas'
    }
}


FACEBOOK_APP_ID = '237180929639489'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '68e652ad4024ba1c2a563e7ff833f856'


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
CUDDLYBUDDLY_STORAGE_S3_CACHE_BACKEND = 'storage'
CUDDLYBUDDLY_STORAGE_S3_CACHE_TIMEOUT = 31556926

MEDIA_URL = 'https://s3.amazonaws.com/rumba_test/'