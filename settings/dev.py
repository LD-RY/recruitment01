from .base import *

DEBUG = True

# 务必修改以下值
ALLOWED_HOSTS = ['172.168.43.85','127.0.0.1']

SECRET_KEY = 'jD++jKkaNvla371O1IxPldcTXdSwR5b0'

LDAP_AUTH_URL = "ldap://172.168.43.85:389"
LDAP_AUTH_CONNECTION_USERNAME = 'admin'
LDAP_AUTH_CONNECTION_PASSWORD = 'password'

INSTALLED_APPS += (
    # other apps for production site
)

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="http://ec32f6371ce5490bacc89ced76459a78@172.16.43.150:9000/2",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        'TIMEOUT':None,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
        }
    }
}