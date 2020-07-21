import ast
import os
from unittest import TestCase

from django.conf import global_settings

from bukdjango_envsettings import settings_to_dict, eval_settings, MAPPING


class TestMapping(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.django_default_settings = {
            k: getattr(global_settings, k) for k in dir(global_settings) if
            not k.startswith('_') and
            k.upper() == k
        }

    @staticmethod
    def print_as_key(v):
        print(f"'{v}': ast.literal_eval,")

    def test_settings_to_dict(self):
        """
        Converting settings module to dict works.
        """
        settings = settings_to_dict(global_settings)
        settings2 = settings_to_dict()
        self.assertEqual(settings, settings2)

        # todo there are settings, but we dont know exact values
        for opt in ["SECRET_KEY", "INSTALLED_APPS"]:
            self.assertIn(opt, settings.keys())

    def test_all_settings_mapped(self):
        """
        Default Django settings have
        coresponding casting type.
        """
        self.assertCountEqual(
            settings_to_dict(global_settings),
            MAPPING,
        )

    def test_custom_settings_module(self):
        """
        Given custom settings module, all works.
        """
        from . import settings_test

        settings = settings_to_dict(settings_test)

        for x in ['A', 'NEW', 'EXTRA']:
            self.assertIn(x, settings)

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


class TestEnv(TestCase):

    file_dir = os.path.dirname(os.path.realpath(__file__))

    def test_open(self):
        import configparser
        config = configparser.ConfigParser()
        config.read(os.path.join(self.file_dir, 'envsettings/1.env'))
        for k in config["CONFIG"]:
            print(config["CONFIG"][k])
