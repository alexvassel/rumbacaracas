
DEBUG = False
TEMPLATE_DEBUG = False

#INTERNAL_IPS = ( '127.0.0.1', '213.33.244.154',)

LANGUAGE_CODE = 'es'



TEMPLATE_DIRS = (
    '/web/apps/rumbacaracas/templates',
 )

FIXTURE_DIRS = (
   '/web/apps/rumbacaracas/locations/fixtures/',
 )


OLDCARACAS_PHOTO_PATH = '/web/apps/oldcaracas/processed'

FULL_BASE_URL = 'http://rumbacaracas.com'

MEDIA_ROOT = '/web/apps/rumbacaracas/media'

STATIC_DOC_ROOT = '/web/apps/rumbacaracas/media'

LOCALE_PATHS = (
    '/web/apps/rumbacaracas/locale',
 )




OLDDATABOGOTA_PHOTO_PATH = '/mnt/rumbacaracas.com/var/www/vhosts/rumbacaracas.com/httpdocs/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'caracas', # Not used with sqlite3.
        'PASSWORD': 'swimedFw', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'rumbaccs', # Or path to database file if using sqlite3.
            'USER': 'rumbaccs', # Not used with sqlite3.
            'HOST': 'rumbacaracas.com', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'dXqGg7XHA5Mfax4', # Not used with sqlite3.
        }
    }


KEY_PREFIX = 'car'

CACHES_OLD = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Amazon S3 configs
DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
AWS_ACCESS_KEY_ID = 'AKIAJAVN6BXUTZ3VMAVA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rumbacaracas.com'