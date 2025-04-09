# Add necessary configurations for the octofit-tracker project

# Consolidating INSTALLED_APPS and MIDDLEWARE blocks
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "tracker",
    "octofit_tracker",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# Ensure only one DATABASES block remains
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
        "HOST": "localhost",
        "PORT": 27017,
    }
}

# Allow all hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Enable CORS for all origins
CORS_ALLOW_ALL_ORIGINS = True


