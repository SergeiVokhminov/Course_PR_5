# Импорт необходимых библиотек
import os
import sys
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

# BASE_DIR - определяет корневую директорию проекта.
# BASE_DIR - этот параметр используется для построения абсолютных путей внутри проекта.
# Основная директория проекта.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ, используемый для криптографических подписей. Необходимо держать его в секрете.
SECRET_KEY = os.getenv("SECRET_KEY")

# Включает или отключает режим отладки.
# Включен (True) только в процессе разработки. При разворачивании на сервере обязательно установить значение False.
DEBUG = True if os.getenv("DEBUG") == "True" else False

# Список разрешенных доменов (используется "*" для разрешения всех), которые могут обслуживаться приложением.
ALLOWED_HOSTS = ["*"]

# Содержит список всех приложений, активированных в проекте.
# После создания своих приложений, их необходимо прописать тут!
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "django_celery_beat",
    "drf_yasg",
    "users",
    "habittracker",
]

# Список промежуточного ПО, которое обрабатывает входящие запросы и выходящие ответы.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Указывает на модуль маршрутизации, который будет использоваться для маршрутизации URL-адресов в проекте.
# URL-конфигурация корневого уровня.
ROOT_URLCONF = "config.urls"

# Настройки шаблонизации.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Указывает путь к WSGI-приложению. Это точка входа вашего приложения для совместимости с WSGI-серверами.
# Настройки необходимы в основном для разворачивания на сервере.
WSGI_APPLICATION = "config.wsgi.application"

# Настройки базы данных (Database - PostgreSQL). Использовать можно и другие базы данных.
if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db.sqlite3",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST", default="db"),
            "PORT": os.getenv("DATABASE_PORT", default="5432"),
        }
    }

# Список валидаторов, используемых для проверки надежности паролей пользователей.
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

# Устанавливает язык для проекта.
LANGUAGE_CODE = "ru-ru"

# Устанавливает часовую зону для проекта.
TIME_ZONE = "Europe/Moscow"

# Включает поддержку интернационализации.
USE_I18N = True

# Включает поддержку локализации, применяя форматирование даты и времени.
USE_L10N = True

# Включает поддержку временных зон.
USE_TZ = True

# Настройки статических файлов.
# Содержит информацию о URL для доступа к статическим файлам.
STATIC_URL = "static/"
# Список директорий на диске, из которых будут подгружаться статические файлы.
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Настройки медиатеки.
# Содержит информацию о URL для доступа к медиафайлам
MEDIA_URL = "/media/"
# Директория на диске, где будут храниться медиафайлы, загружаемые пользователем.
MEDIA_ROOT = BASE_DIR / "media"

# Определяет тип поля по умолчанию для первичных ключей всех приложений
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Стандартная модель пользователя
AUTH_USER_MODEL = "users.User"

# Именованный адрес на который следует перенаправлять пользователя после успешной авторизации
LOGIN_REDIRECT_URL = "/"
# Именованный адрес на который перенаправляется пользователь после выхода
LOGOUT_REDIRECT_URL = "/"

# Настройка почтового сервера
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 2525
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False) == "True"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", False) == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Адрес на который следует перенаправить неавторизованного пользователя при попытке посетить закрытую страницу сайта
# LOGIN_URL = "users:login"

# Настройка кэширования
CACHE_ENABLED = True
if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": os.getenv("LOCATION"),
        }
    }

# Настройки для REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Настройки срока действия токенов
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Секретный ключ STRIPE
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

# Настройки для Celery

# URL-адрес брокера сообщений
CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL"
)  # Например, Redis, который по умолчанию работает на порту 6379

# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

# Часовой пояс для работы Celery
CELERY_TIMEZONE = TIME_ZONE

# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True

# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60

# Словарь с настройками расписания для задач в Celery Beat.
CELERY_BEAT_SCHEDULE = {
    "task-name": {
        "task": "users.tasks.user_last_login",
        "schedule": timedelta(minutes=15),
    },
}

# Настройка, которая указывает, какой модуль и класс использовать для планировщика периодических задач в Celery.
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Настройки телеграм
TELEGRAM_URL = os.getenv("TELEGRAM_URL")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://localhost:80",
]
