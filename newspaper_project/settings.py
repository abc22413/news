import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=['*'], cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #ours
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'articles.apps.ArticlesConfig',
    #3rd party
    'captcha',
    'crispy_forms',#Make HTML forms nicer
    'profanity',#protect against profanity
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',#Referral policy
]

ROOT_URLCONF = 'newspaper_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'newspaper_project.wsgi.application'


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

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"templates/css"),
]
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Sentry.io integration
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=config('dsn'),
    integrations=[DjangoIntegration()]
)


#Custom users
AUTH_USER_MODEL = "users.CustomUser"


#LOGIN AND LOGOUT FUNCTIONALITY
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


#EMAIL-SENDING FOR PASSWORD RESET
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True


#django-crispy-form integrations
CRISPY_TEMPLATE_PACK = 'bootstrap4'


#SECURITY-OPTIONS
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


#CSP OPTIONS
CSP_DEFAULT_SRC = "'none'"
CSP_FONT_SRC = "https://fonts.gstatic.com"
CSP_FORM_ACTION = "'self'"
CSP_FRAME_SRC = "https://www.google.com"
CSP_IMG_SRC = "'self'"
CSP_SCRIPT_SRC = [
    "'unsafe-inline'",
    "https://browser.sentry-cdn.com/5.9.1/bundle.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
    "https://code.jquery.com/jquery-3.3.1.slim.min.js",
    "https://sentry.io/api/embed/error-page/",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js",
    "https://www.google.com/recaptcha/api.js",
    "https://www.gstatic.com/recaptcha/releases/75nbHAdFrusJCwoMVGTXoHoM/recaptcha__en.js",
]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    "https://fonts.googleapis.com/",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/css/",
]
CSP_BASE_URI = "'self'"
CSP_FRAME_ANCESTORS = "'self'"

'''
  default-src 'none'; font-src https://fonts.gstatic.com; form-action 'self'; frame-src https://www.google.com; img-src 'self' data:; script-src 'unsafe-inline' https://browser.sentry-cdn.com/5.9.1/bundle.min.js https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js https://code.jquery.com/jquery-3.3.1.slim.min.js https://sentry.io/api/embed/error-page/ https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js https://www.google.com/recaptcha/api.js https://www.gstatic.com/recaptcha/releases/75nbHAdFrusJCwoMVGTXoHoM/recaptcha__en.js; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com/ https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/css/
'''


#REFERRER POLICY
REFERRER_POLICY = 'strict-origin'


#RECAPTCHA
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
