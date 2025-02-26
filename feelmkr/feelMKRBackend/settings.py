import os
import sys

from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

IS_TESTING = "pytest" in sys.argv[0]

DEBUG = os.getenv("DEBUG")

# Récupère la clé secrète
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", default="_e%qms%*-i8!0p+48omg&^_si%if6q1@4u&h=^xsyj@o9z@=^z"
)


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Spécifiez ici les répertoires contenant vos templates personnalisés
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "feelMKRBackend",
    "rest_framework",
    "rest_framework_simplejwt",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

ALLOWED_HOSTS = ["feelmkr-cda-backend.onrender.com", "127.0.0.1", "aws-0-eu-west-3.pooler.supabase.com"]

DATABASE_URL = os.getenv('DATABASE_URL')

ROOT_URLCONF = os.getenv("ROOT_URLCONF")


if IS_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': "feelmkr",  # Base de test locale
            'USER': "mouss",       # Ton user PostgreSQL local
            'PASSWORD': "root",   # Ton mot de passe PostgreSQL
            'HOST': "localhost",      # PostgreSQL en local
            'PORT': "5432",           # Port par défaut de PostgreSQL
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DBNAME"),
            'USER': os.getenv("DBUSER"),
            'PASSWORD': os.getenv("DBPASSWORD"),
            'HOST': os.getenv("HOST"),
            'PORT': os.getenv("PORT"),
        }
    }
