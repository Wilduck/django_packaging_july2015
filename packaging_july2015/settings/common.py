from .installed_apps import *
from .middleware import *
from .app_config import *
from .databases import *


STATIC_URL = '/static/'
ALLOWED_HOSTS = []
ROOT_URLCONF = 'packaging_july2015.urls'

WSGI_APPLICATION = 'packaging_july2015.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['packaging_july2015/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
