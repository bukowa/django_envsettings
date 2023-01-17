#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
from djangobuk_envsettings import update_from_env

os.environ["DJANGO_SECRET_KEY"] = 'key'
os.environ["DJANGO_SITE_ID"] = '255'
os.environ["DJANGO_EMAIL_PORT"] = '644'
os.environ["DJANGO_EXTRA_KEY"] = 'asdd'
os.environ["DJANGO_EXTRA_KEY2"] = 'asdds'
os.environ["DJANGO_ENGINE_NAME"] = ':memory:'


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
