"""
Django settings for recruitment01 project.

Generated by 'django-admin startproject' using Django 2.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qxb&$edm7ci=^1g1o+j8&=$gay#14n6ezmz4bbmowp@1-!xsj1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/'
SIMPLE_BACKEND_REDIRECT_URL = '/accounts/login/'


# Application definition

INSTALLED_APPS = [
    'registration',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
    'interview',
    'django_python3_ldap',
    'bootstrap4',

]

MIDDLEWARE = [
    'interview.performance.PerformanceAndExceptionLoggerMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recruitment01.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'jobs/templates')]
        ,
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

WSGI_APPLICATION = 'recruitment01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ("zh-hans",_("Chinese")),
    ("en",_("English")),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR,'locale'),
)
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, "/static/"),
]

# AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend","django.contrib.auth.backends.ModelBackend",)

LDAP_AUTH_URL = "ldap://localhost:389"
LDAP_AUTH_USE_TLS = False
LDAP_AUTH_SEARCH_BASE = "dc=lidan,dc=com"
LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"
LDAP_AUTH_USER_FIELDS = {
    "username": "cn",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# 使用username作为登录的用户名
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"

# LDAP连接的用户名和密码
LDAP_AUTH_CONNECTION_USERNAME = None
LDAP_AUTH_CONNECTION_PASSWORD = None

DINGTALK_WEB_HOOK = 'https://oapi.dingtalk.com/robot/send?access_token=a88279abc6fee4fa59ffcdb03cb230f75f94e407cb94bb2cf9e8cdae5071cc06'

BOOTSTRAP4 = {
    'jquery_url':{
        'url':'https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.js'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file':{
            'class':'logging.FileHandler',
            'formatter':'simple',
            'filename':os.path.join(os.path.dirname(BASE_DIR),'recruitment.admin.log'),
        },
        'performance':{
            #'level': 'INFO',
            'class':'logging.FileHandler',
            'formatter':'simple',
            'filename':os.path.join(os.path.dirname(BASE_DIR),'recruitment.performance.log'),
        },
    },
    'root':{
        'handlers':['console','file'],
        'level':'INFO',
    },
    'loggers': {
        'django_python3_ldap': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
        },
        'interview.performance': {

            'handlers': ['console','performance'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = "/media/"

# 阿里云 CDN 存储静态资源文件 & 阿里云存储上传的图片/文件
DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
OSS_ACCESS_KEY_ID = 'LTAI4GJtfmitmxJbX7mhwSEY'
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = 'zncyF3u3JJ1nENwRCZVXQjlu0DBgBt'
# The name of the bucket to store files in
# 刚进去的名字，不是用户的，用户的名字是recruitment01
OSS_BUCKET_NAME = 'recruiment'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'