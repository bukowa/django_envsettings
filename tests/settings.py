import os

from bukdjango_envsettings import update_from_env

update_from_env(
    pre='DJANGO_',
    allowed=[
        'SECRET_KEY',
        'SITE_ID',
    ])
