import ast

MAPPING = {
    'ABSOLUTE_URL_OVERRIDES': ast.literal_eval,
    'ADMINS': ast.literal_eval,
    'ALLOWED_HOSTS': ast.literal_eval,
    'APPEND_SLASH': ast.literal_eval,
    'AUTHENTICATION_BACKENDS': ast.literal_eval,
    'AUTH_PASSWORD_VALIDATORS': ast.literal_eval,
    'CACHES': ast.literal_eval,
    'CACHE_MIDDLEWARE_SECONDS': ast.literal_eval,
    'CSRF_COOKIE_AGE': ast.literal_eval,
    'CSRF_COOKIE_DOMAIN': ast.literal_eval,
    'CSRF_COOKIE_HTTPONLY': ast.literal_eval,
    'CSRF_COOKIE_SECURE': ast.literal_eval,
    'CSRF_TRUSTED_ORIGINS': ast.literal_eval,
    'CSRF_USE_SESSIONS': ast.literal_eval,
    'DATABASES': ast.literal_eval,
    'DATABASE_ROUTERS': ast.literal_eval,
    'DATA_UPLOAD_MAX_MEMORY_SIZE': ast.literal_eval,
    'DATA_UPLOAD_MAX_NUMBER_FIELDS': ast.literal_eval,
    'DATETIME_INPUT_FORMATS': ast.literal_eval,
    'DATE_INPUT_FORMATS': ast.literal_eval,
    'DEBUG': ast.literal_eval,
    'DEBUG_PROPAGATE_EXCEPTIONS': ast.literal_eval,
    'DISALLOWED_USER_AGENTS': ast.literal_eval,
    'EMAIL_PORT': ast.literal_eval,
    'EMAIL_SSL_CERTFILE': ast.literal_eval,
    'EMAIL_SSL_KEYFILE': ast.literal_eval,
    'EMAIL_TIMEOUT': ast.literal_eval,
    'EMAIL_USE_LOCALTIME': ast.literal_eval,
    'EMAIL_USE_SSL': ast.literal_eval,
    'EMAIL_USE_TLS': ast.literal_eval,
    'FILE_UPLOAD_DIRECTORY_PERMISSIONS': ast.literal_eval,
    'FILE_UPLOAD_HANDLERS': ast.literal_eval,
    'FILE_UPLOAD_MAX_MEMORY_SIZE': ast.literal_eval,
    'FILE_UPLOAD_PERMISSIONS': ast.literal_eval,
    'FILE_UPLOAD_TEMP_DIR': ast.literal_eval,
    'FIRST_DAY_OF_WEEK': ast.literal_eval,
    'FIXTURE_DIRS': ast.literal_eval,
    'FORCE_SCRIPT_NAME': ast.literal_eval,
    'FORMAT_MODULE_PATH': ast.literal_eval,
    'IGNORABLE_404_URLS': ast.literal_eval,
    'INSTALLED_APPS': ast.literal_eval,
    'INTERNAL_IPS': ast.literal_eval,
    'LANGUAGES': ast.literal_eval,
    'LANGUAGES_BIDI': ast.literal_eval,
    'LANGUAGE_COOKIE_AGE': ast.literal_eval,
    'LANGUAGE_COOKIE_DOMAIN': ast.literal_eval,
    'LANGUAGE_COOKIE_HTTPONLY': ast.literal_eval,
    'LANGUAGE_COOKIE_SAMESITE': ast.literal_eval,
    'LANGUAGE_COOKIE_SECURE': ast.literal_eval,
    'LOCALE_PATHS': ast.literal_eval,
    'LOGGING': ast.literal_eval,
    'LOGOUT_REDIRECT_URL': ast.literal_eval,
    'MANAGERS': ast.literal_eval,
    'MIDDLEWARE': ast.literal_eval,
    'MIGRATION_MODULES': ast.literal_eval,
    'NUMBER_GROUPING': ast.literal_eval,
    'PASSWORD_HASHERS': ast.literal_eval,
    'PASSWORD_RESET_TIMEOUT_DAYS': ast.literal_eval,
    'PREPEND_WWW': ast.literal_eval,
    'SECURE_BROWSER_XSS_FILTER': ast.literal_eval,
    'SECURE_CONTENT_TYPE_NOSNIFF': ast.literal_eval,
    'SECURE_HSTS_INCLUDE_SUBDOMAINS': ast.literal_eval,
    'SECURE_HSTS_PRELOAD': ast.literal_eval,
    'SECURE_HSTS_SECONDS': ast.literal_eval,
    'SECURE_PROXY_SSL_HEADER': ast.literal_eval,
    'SECURE_REDIRECT_EXEMPT': ast.literal_eval,
    'SECURE_REFERRER_POLICY': ast.literal_eval,
    'SECURE_SSL_HOST': ast.literal_eval,
    'SECURE_SSL_REDIRECT': ast.literal_eval,
    'SESSION_COOKIE_AGE': ast.literal_eval,
    'SESSION_COOKIE_DOMAIN': ast.literal_eval,
    'SESSION_COOKIE_HTTPONLY': ast.literal_eval,
    'SESSION_COOKIE_SECURE': ast.literal_eval,
    'SESSION_EXPIRE_AT_BROWSER_CLOSE': ast.literal_eval,
    'SESSION_FILE_PATH': ast.literal_eval,
    'SESSION_SAVE_EVERY_REQUEST': ast.literal_eval,
    'SILENCED_SYSTEM_CHECKS': ast.literal_eval,
    'STATICFILES_DIRS': ast.literal_eval,
    'STATICFILES_FINDERS': ast.literal_eval,
    'STATIC_ROOT': ast.literal_eval,
    'STATIC_URL': ast.literal_eval,
    'TEMPLATES': ast.literal_eval,
    'TEST_NON_SERIALIZED_APPS': ast.literal_eval,
    'TIME_INPUT_FORMATS': ast.literal_eval,
    'USE_I18N': ast.literal_eval,
    'USE_L10N': ast.literal_eval,
    'USE_THOUSAND_SEPARATOR': ast.literal_eval,
    'USE_TZ': ast.literal_eval,
    'USE_X_FORWARDED_HOST': ast.literal_eval,
    'USE_X_FORWARDED_PORT': ast.literal_eval,
    'WSGI_APPLICATION': ast.literal_eval,
    'AUTH_USER_MODEL': str,
    'CACHE_MIDDLEWARE_ALIAS': str,
    'CACHE_MIDDLEWARE_KEY_PREFIX': str,
    'CSRF_COOKIE_NAME': str,
    'CSRF_COOKIE_PATH': str,
    'CSRF_COOKIE_SAMESITE': str,
    'CSRF_FAILURE_VIEW': str,
    'CSRF_HEADER_NAME': str,
    'DATETIME_FORMAT': str,
    'DATE_FORMAT': str,
    'DECIMAL_SEPARATOR': str,
    'DEFAULT_CHARSET': str,
    'DEFAULT_EXCEPTION_REPORTER_FILTER': str,
    'DEFAULT_FILE_STORAGE': str,
    'DEFAULT_FROM_EMAIL': str,
    'DEFAULT_INDEX_TABLESPACE': str,
    'DEFAULT_TABLESPACE': str,
    'EMAIL_BACKEND': str,
    'EMAIL_HOST': str,
    'EMAIL_HOST_PASSWORD': str,
    'EMAIL_HOST_USER': str,
    'EMAIL_SUBJECT_PREFIX': str,
    'FILE_CHARSET': str,
    'FORM_RENDERER': str,
    'LANGUAGE_CODE': str,
    'LANGUAGE_COOKIE_NAME': str,
    'LANGUAGE_COOKIE_PATH': str,
    'LOGGING_CONFIG': str,
    'LOGIN_REDIRECT_URL': str,
    'LOGIN_URL': str,
    'MEDIA_ROOT': str,
    'MEDIA_URL': str,
    'MESSAGE_STORAGE': str,
    'MONTH_DAY_FORMAT': str,
    'SECRET_KEY': str,
    'SERVER_EMAIL': str,
    'SESSION_CACHE_ALIAS': str,
    'SESSION_COOKIE_NAME': str,
    'SESSION_COOKIE_PATH': str,
    'SESSION_COOKIE_SAMESITE': str,
    'SESSION_ENGINE': str,
    'SESSION_SERIALIZER': str,
    'SHORT_DATETIME_FORMAT': str,
    'SHORT_DATE_FORMAT': str,
    'SIGNING_BACKEND': str,
    'STATICFILES_STORAGE': str,
    'TEST_RUNNER': str,
    'THOUSAND_SEPARATOR': str,
    'TIME_FORMAT': str,
    'TIME_ZONE': str,  # default None, str
    'X_FRAME_OPTIONS': str,
    'YEAR_MONTH_FORMAT': str,
}


def get_mapping(extra_map: dict = None) -> dict:
    mapping = MAPPING.copy()
    if extra_map:
        mapping.update(extra_map)
    return mapping


def settings_to_dict(settings_module=None) -> dict:
    """
    Convert Django settings module into dict.
    """
    if not settings_module:
        from django.conf import global_settings as settings_module

    return {
        k: type(getattr(settings_module, k)) for k in dir(settings_module) if
        not k.startswith('_') and
        k.upper() == k
    }


def eval_settings(settings: dict, mapping=None) -> dict:
    """
    Given settings map ex. {SECRET_KEY: "asdasd"}
    evaulate values into coresponding Python types.
    """
    mapping = mapping or get_mapping()
    # for opt, value in settings.items():
    #     print(opt, value)
    #     mapping[opt](value)
    return {
        opt: mapping[opt](value) for (opt, value) in settings.items()
    }
