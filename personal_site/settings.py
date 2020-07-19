"""
Django settings for personal_site project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
key = ''
with open('personal_site/secret.txt') as file:
    key = file.read()

SECRET_KEY = key

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#WILL be true by deafault. use export DJANGO_DEBUG=False to disable
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

# when in production
if DEBUG == False:
     CSRF_COOKIE_SECURE = True
     SESSION_COOKIE_SECURE = True


#for now allow all host, will change
#use in nginx to reject default host
# server {
#     listen 80 default_server;
#     return 444;
# }
ALLOWED_HOSTS = ['*']

# Application definition

#for django.contrib.sites
SITE_ID = 1

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio.apps.PortfolioConfig',
    'rest_framework',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
'sekizai',
'filer',
'easy_thumbnails',
'mptt',
'djangocms_text_ckeditor',
'djangocms_link',
'djangocms_file',
'djangocms_picture',
'djangocms_video',
# 'djangocms_googlemap',
'djangocms_snippet',
'djangocms_style',

]

MIDDLEWARE = [
'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
'django.middleware.locale.LocaleMiddleware',
'cms.middleware.user.CurrentUserMiddleware',
'cms.middleware.page.CurrentPageMiddleware',
'cms.middleware.toolbar.ToolbarMiddleware',
'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'personal_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
'sekizai.context_processors.sekizai',
'cms.context_processors.cms_settings',
'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'personal_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# CMS
X_FRAME_OPTIONS = 'SAMEORIGIN'
CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#filer for cms
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)