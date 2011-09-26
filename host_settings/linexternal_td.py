TEMPLATE_DIRS = ( 
    '/srv/vhosts/rumbacaracas/templates',
 )

FIXTURE_DIRS = ( 
   '/srv/vhosts/rumbacaracas/locations/fixtures/',
 )


OLDBOGOTA_PHOTO_PATH = '/srv/vhosts/oldbogota/processed'

FULL_BASE_URL = 'http://213.33.244.154:89'

MEDIA_ROOT = '/srv/vhosts/rumbacaracas/media/'

STATIC_DOC_ROOT = '/srv/vhosts/rumbacaracas/media/'

LOCALE_PATHS = ( 
    '/srv/vhosts/rumbacaracas/locale',
 )

OLDDATABOGOTA_PHOTO_PATH = '/mnt/caracas/'
FAKE_IMPORT_IMAGE = '/mnt/maksim/test_images/tst_imgs/1.jpg'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
        'HOST': 'linexternal.td', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'oldcaracas', # Or path to database file if using sqlite3.
            'USER': 'root', # Not used with sqlite3.
            'HOST': 'linexternal.td', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'cleopatra', # Not used with sqlite3.
        }
    }

LANGUAGE_CODE = 'es'

DEBUG = True

FACEBOOK_APP_ID = '134081330023149'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = 'dca4424ae0cec25a25f4f6bb7818483a'

TWITTER_CONSUMER_KEY = 'IYdcJdgtroX4yE7tuqUscA'
TWITTER_CONSUMER_SECRET_KEY = 'nLD3noOIPwSZeyXZaUpwSVLIw9yZOKkAkNjpY85SqLw'

ISSUU_API_KEY = "3g5tlt235dhwzwu9lf8yveetczya50u0"
ISSUU_API_SECRET = "0unbbypa2ck7ls8yjstzelyyssax2026"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'storage': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'caracas'
    }
}

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