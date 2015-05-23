# -*- coding: utf-8 -*-

"""
Django settings for xswapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Base_dir /usr/xswapp/xswapp
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#PATH /usr/xswapp;
PATH=os.path.dirname(BASE_DIR) 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-!v03#@*1xiv9l9iax08q%o89ve2)74&06k7tc!ar^k_+d*w-('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'xswshop',
#    'xswtest',
    'register',
    'gift',
    'xswclass',
    'xswshop',
    'intro',
    'sendmail',
    'appversion',
    'ckeditor',
    'smart_selects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'xswapp.urls'

WSGI_APPLICATION = 'xswapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
       # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	'NAME':'xswapp',
	'USER':'xswapp',
	'PASSWORD':'xswapp2015',
	'HOST':'',
	'PORT':'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#template 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#responsecharset
FILE_CHARSET="utf-8"

DEFAULT_CHARSET="utf-8"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT= PATH+'/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = PATH+'/media/'
MEDIA_URL = '/media/'

#send mail settings
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.mxhichina.com'
EMAIL_PORT='25'
#EMAIL_USE_SSL= True
EMAIL_HOST_USER='ncheng@ghrdesign.com'
MAIL_HOST_PASSWORD='iloveghrhome'

CKEDITOR_UPLOAD_PATH = "uploads"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '/static/dist/js/jquery-1.11.3.min.js'
