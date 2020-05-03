"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['django-showcase.herokuapp.com', 'localhost', '127.0.0.1', '0.0.0.0']

AUTH_USER_MODEL = 'users.CustomUser' # points to our custom user model

# media file configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')# file system path for user uploaded files
MEDIA_URL = '/media/'# url used in templates to find files uploaded


# static file configuration
STATIC_URL = '/static/' # url to reference static files
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ] # where staticfiles are held for local development
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # collectstatic will places static files for deployment
# remind django how to look for static files
STATICFILES_FINDERS = [ # checks in STATICFILES_DIRS and applies that value within each app
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# let cripsy forms apply pre-styled forms for us
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # to serve static files in production
    'django.contrib.staticfiles', # if whitenoise comes before staticfiles it will work for development
    'django.contrib.sites', # sites framework to control multiple sites

    # local apps 
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'formapp.apps.FormappConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',

    # third party apps can also be installed and are listed below
    'crispy_forms',# makes everything so pretty
    'allauth', # now manages logins for us
    'allauth.account',
    'debug_toolbar', # for django-debug-toolbar

]


MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # placement of this matters?
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # for django-debug-toolbar
    'django.middleware.cache.FetchFromCacheMiddleware',

]
# some cache configuration settings
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''


ROOT_URLCONF = 'bookstore_root.urls'

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

WSGI_APPLICATION = 'bookstore_root.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django allauth config, this is site 1
LOGIN_REDIRECT_URL = 'home' # where users will be redirected upon successful login
ACCOUNT_LOGOUT_REDIRECT = 'home'
ACCOUNT_SESSION_REMEMBER = True # keeps user logged in
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # wont require user to retype password
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# email backend config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@mg.pleasehiremeforcomputerstuff.com'
EMAIL_HOST =  'smtp.mailgun.org'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', default='email_user')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', default='email_password')
EMAIL_PORT = 587
EMAIL_USE_TLS = 1

# stripe credit card processing configuration
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')


# configure internal ips so that docker doesnt throw us off for django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ ip[:-1] + "1" for ip in ips ]


# production tweaks
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True # help prevent cross site scripting
    X_FRAME_OPTIONS = 'DENY' # helps prevent clickjacking, no invisible iframes pls
    SECURE_SSL_REDIRECT = True # force all traffic to use ssl/tls
    SECURE_HSTS_SECONDS = 3600 # configure http strict transport layer options
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True # force session cookies to be transmitted securely
    CSRF_COOKIE_SECURE = True # follow suit with csrf tokens 
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


    # unsure about this secure_refferer_policy setting
    #SECURE_REFERRER_POLICY = True

# heroku settings
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
