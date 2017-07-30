from django.conf import settings
from ..settings import *
from django.utils.html import mark_safe


DEBUG = True

ALLOWED_HOSTS = []

# SECRET_KEY = '=7d@j@ogxkb^79pjc+4n!febd1td$jm9eby+d461&_9-54xp_c'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'assets', 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '',  # Or path to database file if using sqlite3.
#         'USER': '',  # Not used with sqlite3.
#         'PASSWORD': '',
#         'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
#         'TEST_NAME': 'rebateceo-korona-test',
#     },
# }


# Grappelli
GRAPPELLI_ADMIN_TITLE = mark_safe('<span style="color:red; font-weight: 900;">MySandbox DEV</span>')


