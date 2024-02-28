import os
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-lq$%9&l6v)!v07atxpz=f54dgjysrgw%8-)67ech9(by3!7y!y'
LOGIN_URL='/login'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
     'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vv',
     'django.contrib.sites',
     "allauth",
     "allauth.account",
     "allauth.socialaccount",
     "allauth.socialaccount.providers.google"
]
SITE_ID = 1
SOCIALACCOUNT_LOGIN_ON_GET=True

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vehicle_vault.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
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

WSGI_APPLICATION = 'vehicle_vault.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIALACCOUNT_PROVIDERS ={
    "google":{
        "SCOPE":[
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {"access_type":"online"}
    }
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
GEOCODER = 'geopy.geocoders.Nominatim'
GEOCODER_OPTIONS = {
    'user_agent': 'my_geocoder',  # Set your user agent
}
RAZORPAY_KEY_ID ='rzp_test_YM3NrhdHc4MtJd'
RAZORPAY_KEY_SECRET = '7GTeZp4p7eEBvMzolURUvp5y'
# GOOGLE_CLOUD_API_KEY = config('API_KEYS__GOOGLE_CLOUD_KEY', default='')
# settings_secrets.py
GOOGLE_CLOUD_API_KEY = 'AIzaSyDuVkxqozowjpt0vz9OHcCVsVC3Sc82ol0'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:/jacob/vehicle_vault/google_cloud/dynamic-return-400903-d3c31dd2bb70.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
# credential_path ="D:\jacob\vehicle_vault\vehicle_vault\dynamic-return-400903-d3c31dd2bb70.json"



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'validationmailshow@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'rjjh qjcq ouql pchb'  # Your Gmail email password or an app-specific pass