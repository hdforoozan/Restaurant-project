from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurantdb',
        'USER': 'postgres',
        'PASSWORD': 'hdlight74',
        'PORT': '5432',
    }
}
