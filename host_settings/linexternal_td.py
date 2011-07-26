TEMPLATE_DIRS = ( 
    '/srv/vhosts/rumbabogota/templates',
 )

FIXTURE_DIRS = ( 
   '/srv/vhosts/rumbabogota/locations/fixtures/',
 )


OLDBOGOTA_PHOTO_PATH = '/srv/vhosts/oldbogota/processed'

FULL_BASE_URL = 'http://213.33.244.154:88'

MEDIA_ROOT = '/srv/vhosts/rumbabogota/media/'

STATIC_DOC_ROOT = '/srv/vhosts/rumbabogota/media/'

LOCALE_PATHS = ( 
    '/srv/vhosts/rumbabogota/locale',
 )

OLDDATABOGOTA_PHOTO_PATH = '/mnt/maksim/Documents/Develop/rumbabogota/olddata/'
FAKE_IMPORT_IMAGE = '/mnt/maksim/test_images/tst_imgs/1.jpg'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bogota', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
        'HOST': 'linexternal.td', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'oldbogotadata', # Or path to database file if using sqlite3.
            'USER': 'root', # Not used with sqlite3.
            'HOST': 'linexternal.td', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'cleopatra', # Not used with sqlite3.
        }
    }

LANGUAGE_CODE = 'es'