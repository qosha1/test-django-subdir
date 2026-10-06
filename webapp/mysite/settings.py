from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "test-django-subdir-not-a-secret"
DEBUG = False
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["pages"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "mysite.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
}]
WSGI_APPLICATION = "mysite.wsgi.application"
DATABASES = {}
USE_TZ = True
