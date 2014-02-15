"""
Django settings for proyectos_ecys project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#toma el directorio de configuracion para el deploy en diferentes ambientes.
#conf = open('../Conf/db.conf', 'r')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6tnm19li$(t$ul%vcox69!u%$(v_sudjo-4sh-&vihw4!!mt-x'

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
    'django_jenkins',
    'sistema_pe',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ProyectosEcys.urls'

WSGI_APPLICATION = 'ProyectosEcys.wsgi.application'


JENKINS_TASKS = (
	'django_jenkins.tasks.run_pylint',
        'django_jenkins.tasks.with_coverage',
        'django_jenkins.tasks.django_tests',   # select one django or
        #'django_jenkins.tasks.dir_tests'      # directory tests discovery
        'django_jenkins.tasks.run_pep8',
#	'django_jenkins.tasks.run_flake8',
#        'django_jenkins.tasks.run_pyflakes',
#        'django_jenkins.tasks.run_jslint',
#        'django_jenkins.tasks.run_csslint',    
#        'django_jenkins.tasks.run_sloccount',    
#        'django_jenkins.tasks.lettuce_tests',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
#    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME':  conf.readline().strip(),
#        'USER':  conf.readline().strip(),
#        'HOST':  conf.readline().strip(),
#	'PASSWORD': conf.readline().strip()  
#    }
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'proyectos_ecys_db',
        'USER':  'AyD2',
        'HOST':  'localhost',
        'PASSWORD': 'AyD2'
    }
    #'
    #'test_database':{
    #   'ENGINE': 'django.db.backends.postgresql_psycopg2',
      #  'NAME': 'proyectos_ecys_pdb',
       # 'USER': 'AyD2',
        #'HOST': 'localhost'

    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
