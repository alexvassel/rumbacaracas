
DEBUG = True
#INTERNAL_IPS = ( '127.0.0.1', '213.33.244.154',)

LANGUAGE_CODE = 'es'

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    '/web/apps/rumbabogota/templates',
 )

FIXTURE_DIRS = (
   '/web/apps/rumbabogota/locations/fixtures/',
 )


OLDBOGOTA_PHOTO_PATH = '/web/apps/oldbogota/processed'

FULL_BASE_URL = 'http://rumbabogota.com'

MEDIA_ROOT = '/web/apps/rumbabogota/media'

STATIC_DOC_ROOT = '/web/apps/rumbabogota/media'

LOCALE_PATHS = (
    '/web/apps/rumbabogota/locale',
 )




OLDDATABOGOTA_PHOTO_PATH = '/mnt/rumbacaracas.com/var/www/vhosts/rumbabogota.com/httpdocs/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bogota', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'bM_We1FA', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'bogotadb', # Or path to database file if using sqlite3.
            'USER': 'rumbogodb', # Not used with sqlite3.
            'HOST': 'rumbabogota.com', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'mWazqXFUqjperr3', # Not used with sqlite3.
        }
    }


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
