import ast
import functools
import os
from unittest import TestCase

from django.conf import global_settings

from bukdjango_envsettings.utils import settings_to_dict, eval_settings, MAPPING
from django.core.management import call_command

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class ContextDecorator:

    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return decorated


class temp_django_settings(ContextDecorator):

    def __enter__(self):
        import django.conf.global_settings
        self.old_settings = django.conf.global_settings
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import django.conf.global_settings
        django.conf.global_settings = self.old_settings


class temp_environ(ContextDecorator):

    def __enter__(self):
        self.old_env = dict(os.environ.copy())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.environ.clear()
        os.environ.update(self.old_env)


class TestMapping(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.django_default_settings = {
            k: getattr(global_settings, k) for k in dir(global_settings) if
            not k.startswith('_') and
            k.upper() == k
        }

    @temp_environ()
    def test_all_settings_mapped(self):
        """
        Default Django settings have
        coresponding casting type.
        """
        for k in settings_to_dict(global_settings):
            self.assertIn(k, MAPPING)

    @temp_environ()
    def test_eval_extra_map(self):
        """
        Given extra mapping, settings typemap is correct.
        """
        settings = {
                'A': "1,2,3,4,5",
                'B': '["127.0.0.1", 55, 43]',
                'C': "a|b|c|d",
        }
        extra_map = {
                'A': lambda v: v.split(','),
                'C': lambda v: v.split('|'),
                'B': ast.literal_eval,
        }

        evaulted = eval_settings(
            settings=settings,
            mapping=extra_map,
        )

        for k, v in evaulted.items():
            if k == 'A':
                self.assertEqual(['1', '2', '3', '4', '5'], v)
            if k == 'B':
                self.assertEqual(['127.0.0.1', 55, 43], v)
            if k == 'C':
                self.assertEqual(["a", "b", "c", "d"], v)

    @temp_environ()
    def test_eval_with_default_settings(self):
        """
        Given default Django settings, convert them
        to string, cast them back and check their type.
        """
        settings_str = {
            k: str(v) for (k, v) in self.django_default_settings.items()
        }
        settings_eval = eval_settings(settings_str)

        self.assertCountEqual(settings_str, settings_eval)
        self.assertCountEqual(settings_str, self.django_default_settings)
        self.assertCountEqual(settings_eval, self.django_default_settings)

        for k, v in self.django_default_settings.items():
            self.assertEqual(v, settings_eval[k])

    @temp_environ()
    def test_update_from_env(self):
        os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
        os.environ["DJANGO_SECRET_KEY"] = 'key'
        os.environ["DJANGO_SITE_ID"] = '255'
        os.environ["DJANGO_EMAIL_PORT"] = '644'
        os.environ["DJANGO_EXTRA_KEY"] = 'asdd'
        os.environ["DJANGO_EXTRA_KEY2"] = 'asdds'
        os.environ["DJANGO_ENGINE_NAME"] = ':memory:'

        import django

        django.setup()

        from django.conf import settings

        self.assertEqual('key', settings.SECRET_KEY)
        self.assertEqual(255, settings.SITE_ID)
        self.assertEqual(25, settings.EMAIL_PORT)
        self.assertEqual('asdd', settings.EXTRA_KEY)
        self.assertIsNone(getattr(settings, "EXTRA_KEY2", None))

        call_command('migrate')


if __name__ == '__main__':
    import unittest
    unittest.main()
