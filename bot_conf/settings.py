import os
from celery.schedules import crontab
from copy import deepcopy
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ["WEB_SECRET_KEY"]

DEBUG = os.environ["DJANGO_DEBUG"]
HOST = os.environ["WEB_HOST"]

ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = "base.User"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "django_json_widget",
    "telegram_django_bot",
    "base",
    "bscscan",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "handlers": {
        "django_requests": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.environ["LOG_DJANGO"],
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 10,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["django_requests"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bot_conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "bot_conf.wsgi.application"


if os.environ["DB_HOST"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PASSWORD"],
            "HOST": os.environ["DB_HOST"],
            "PORT": "5432",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "../db.sqlite3"),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


REDIS_HOST = os.environ["REDIS_HOST"]
CELERY_BROKER_URL = "redis://" + REDIS_HOST + ":6379"
CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + ":6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
BACKEND_QUEUE = os.environ["BACKEND_QUEUE"]

CELERY_TASK_DEFAULT_QUEUE = BACKEND_QUEUE

CELERY_QUEUES = {
    BACKEND_QUEUE: {
        "exchange": BACKEND_QUEUE,
        "routing_key": BACKEND_QUEUE,
    }
}

BEAT_SCHEDULE = {
    # 'task-create_triggers': {
    #     'task': 'telegram_django_bot.tasks.create_triggers',
    #     'schedule': crontab(minute='*/12'),
    #     'options': {'queue': BACKEND_QUEUE}
    # },
}

CELERY_BEAT_SCHEDULE = deepcopy(BEAT_SCHEDULE)


STATIC_URL = "/static/"
MEDIA_ROOT = "/web/media/"
STATIC_ROOT = "/web/static/"


TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
MAIN_BOT_USERNAME = os.environ["TELEGRAM_BOT_NAME"]
TELEGRAM_LOG = os.environ["TELEGRAM_LOG"]

TELEGRAM_ROOT_UTRLCONF = "bot_conf.utrls"


TELEGRAM_BOT_MAIN_MENU_CALLBACK = "main_menu"


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


BSCSCAN_URL = os.environ["BSCSCAN_URL"]
BSCSCAN_API_KEY = os.environ["BSCSCAN_API_KEY"]
