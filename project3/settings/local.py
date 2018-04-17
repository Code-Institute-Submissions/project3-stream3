from .base import *

DEBUG = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

# Testing email form on contact page
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True       
# EMAIL_HOST = 'smtp.sendgrid.net'      
# EMAIL_PORT = 587     
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')     
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')