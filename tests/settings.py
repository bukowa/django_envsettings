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
    },
    extra_allowed=[
        'EXTRA_KEY',
    ]
)
