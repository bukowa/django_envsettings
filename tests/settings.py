import os

from bukdjango_envsettings import update_from_env

update_from_env(
    pre='DJANGO_',
    allowed=[
        'SECRET_KEY',
        'SITE_ID',
    ],
    extra_mapping={
        'EXTRA_KEY': str,
        'EXTRA_KEY2': str,
        'ENGINE_NAME': str,
    },
    extra_allowed=[
        'EXTRA_KEY',
        'ENGINE_NAME',
    ]
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ENGINE_NAME,
    }
}
