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

OLDDATABOGOTA_PHOTO_PATH = '/mnt/maksim/Documents/Develop/rumbabogota/olddata/'
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
            'NAME': 'oldbogotadata', # Or path to database file if using sqlite3.
            'USER': 'root', # Not used with sqlite3.
            'HOST': 'linexternal.td', # Set to empty string for localhost. Not used with sqlite3.
            'PASSWORD': 'cleopatra', # Not used with sqlite3.
        }
    }

LANGUAGE_CODE = 'es'

DEBUG = True

FACEBOOK_APP_ID = '237180929639489'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '68e652ad4024ba1c2a563e7ff833f856'
