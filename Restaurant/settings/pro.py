from .base import *

DEBUG = False

ADMINS = (
    ('Hadi Foroozanfar', 'hdforoozan@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurantdb',
        'USER': 'postgres',
        'PASSWORD': 'hdlight74',
    }
}
