#coding=utf-8
# Django settings for center_service project.


DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEFAULT_CHARSET = 'utf-8'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

INTERNAL_IPS = ('192.168.8.79',) # 你的ip地址s
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gyyxmail',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
   
}

#######自定义配置###################
from os.path import abspath, dirname, join
CONTEXT = {} #配置上下文
CONTEXT["SITE_NAME"] = "Center Service"
CONTEXT["SITE_ROOT"] = abspath(join(dirname(__file__), '../')) #站点根目录物理路径
CONTEXT["SITE_ROOT"] =  CONTEXT["SITE_ROOT"] + "/"
CONTEXT["SERVICE_PATH"] = CONTEXT["SITE_ROOT"] #服务程序的地址
CONTEXT["SITE_PATH"] = '/'

CONTEXT["THEMES"] = 'default'
CONTEXT["CSS"] = '%sthemes/%s/' % (CONTEXT["SITE_PATH"], CONTEXT["THEMES"])
CONTEXT["IMG"] = '%sthemes/%s/' % (CONTEXT["SITE_PATH"], CONTEXT["THEMES"])
CONTEXT["JS"] =  '%sjs/' % CONTEXT["SITE_PATH"]
CONTEXT["JQUERY"] = '%sjquery/' % CONTEXT["JS"]
CONTEXT["JQUERY_CSS"] = '%sui/css/' % CONTEXT["JQUERY"]

CONTEXT["THEMES_PATH"] = CONTEXT["SITE_ROOT"] + 'media/themes/'
CONTEXT["CSS_PATH"] = CONTEXT["THEMES_PATH"] +CONTEXT["THEMES"] + '/'
CONTEXT["JS_PATH"] = CONTEXT["SITE_ROOT"] + 'media/js/'

UC_WEB = 'http://www.xieli.com/ucenter/api.php'
CLIENT_ID = 24
TOKEN = 'XsDB!*oKqcTSzc~1'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.126.com'
EMAIL_HOST_USER = 'lichunyin919@126.com'
EMAIL_HOST_PASSWORD = 'lele1988919'
EMAIL_PORT = 25

#######自定义配置结束################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT =  CONTEXT["SITE_ROOT"] + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = CONTEXT["SITE_PATH"] +'media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bgbs=!!&00=u!30631+z1_5lah&m45%t5=+o&=xz+hvfys_3yd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'center_service.service.middleware.SqlPrintingMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',

)

ROOT_URLCONF = 'center_service.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    CONTEXT["SITE_ROOT"] + 'templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


#以下用于初始化UCENTER API
from gyyx.uc_client.config import ClientConfigManager
ClientConfigManager.LoadConfig(UC_WEB, CLIENT_ID, TOKEN)

