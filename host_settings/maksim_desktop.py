FIXTURE_DIRS = ( 
   '/home/maksim/Documents/Develop/rumbabogota/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldbogota/processed'

FULL_BASE_URL = 'http://localhost.td'

MEDIA_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

STATIC_DOC_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

LOCALE_PATHS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/locale',
 )


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bogota', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

