from os import pardir, environ
from os.path import dirname, abspath, join as path_join


PROJECT_ROOT = abspath(path_join(dirname(__file__), pardir))
PACKAGE_ROOT = abspath(dirname(__file__))
BASE_DIR = PACKAGE_ROOT

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'TAO',
        'USER':'samuel',
        'PASSWORD':'2riixdii',
        #'NAME': 'dev.db',
    }
}

ALLOWED_HOSTS = [
    'localhost',
    '192.168.43.38',
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = int(environ.get('SITE_ID', 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = path_join(PROJECT_ROOT, 'assets')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = '/assets/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = path_join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS=[
    path_join(PROJECT_ROOT, 'static', 'dist'),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9ex%h6$v4b_q7bkx#kfuu68nnt$e!fack^_0+jalt3&6anrleq'

TEMPLATES = [
    {
        #'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path_join(PACKAGE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':DEBUG,
            #'environment': "main.jinja2.environment",
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                #'django.core.context_processors.auth',
                #'account.context_processors.account',
                #'tao.context_processors.settings'
            ],
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'account.middleware.LocaleMiddleware',
    'member.middleware.LoginRequiredMiddleware',
    'member.middleware.PostAuthMiddleWare',
    #'member.middleware.MiddlewareMixin',
]

ROOT_URLCONF = 'tao.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tao.wsgi.application'

DJANGO_APPS= [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles']
BASE_APPS=['tao', 'member', 'medium', 'book', 'haystack']
    #'tts',
    #'qrauth',
INSTALLED_APPS =DJANGO_APPS+BASE_APPS
    #'bootstrapform', 'pinax.templates',
    #'pinax.blog', 'pinax.images', 'pinax.webanalytics', 'account', 'pinax.apps.account',
AUTHOR_APPS=[
    'sutra',
    'tag',
    'friend',
    'post',
    'blog',
    'forum',
    'tug',
    'gallery',
    'ge2ge'
]
INSTALLED_APPS+=AUTHOR_APPS

# Grab your own GA id and replace UA-XXXXXXXX or use another
# pinax-webanalytics provider, or roll your own template.
# PINAX_WEBANALYTICS_SETTINGS = {
#     'google': {
#         2: 'UA-XXXXXXXX',
#     }
# }

# Turn off the admin js; probably should remove from the form
PINAX_BLOG_ADMIN_JS = []

ADMIN_URL = 'admin:index'
CONTACT_EMAIL = 'support@example.com'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

FIXTURE_DIRS = [
    path_join(PROJECT_ROOT, 'fixtures'),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#AUTHENTICATION_BACKENDS = [
#    #'social_core.backends.twitter.TwitterOAuth',
#    'account.auth_backends.UsernameAuthenticationBackend',
#]
TEMPLATE_CONTEXT_PROCESSORS = [
    'account.context_processors.account',
]
AUTH_USER_MODEL='member.Member'
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = path_join(BASE_DIR, 'generated')
MAX_SOUND_LIFE = 60*60*12   # seconds of sound file storing
#DATA_UPLOAD_MAX_NUMBER_FIELDS=None

WEBMASTER='phycomp@gmail.com'
LOGIN_URL='/member/login/'
whooshIndex=path_join(dirname(__file__), 'whooshIndex')
HAYSTACK_CONNECTIONS={
'default':{
	'ENGINE':'haystack.backends.whoosh_backend.WhooshEngine',
	'PATH':whooshIndex,
	},
}
USE_TZ=True
