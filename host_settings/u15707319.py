DEBUG = False
TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (
    '/web/rumbabogota/templates',
 )

FIXTURE_DIRS = (
   '/web/rumbabogota/locations/fixtures/',
 )


OLDBOGOTA_PHOTO_PATH = '/web/oldbogota/processed'

FULL_BASE_URL = 'http://rumbacr.com'

MEDIA_ROOT = '/web/rumbabogota/media/'

STATIC_DOC_ROOT = '/web/rumbabogota/media/'

LOCALE_PATHS = (
    '/web/rumbabogota/locale',
 )

OLDDATABOGOTA_PHOTO_PATH = '/mnt/maksim/Documents/Develop/rumbabogota/olddata/'
FAKE_IMPORT_IMAGE = '/mnt/maksim/test_images/tst_imgs/1.jpg'

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
            'NAME': 'oldbogotadata', # Or path to database file if using sqlite3.
            'USER': 'root', # Not used with sqlite3.
            'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'bM_We1FA', # Not used with sqlite3.
        }
    }

