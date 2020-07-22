# envsettings

Allows updating all django settings from `env` variables.

1. Usage:
    - set environment variable `DJANGO_SETTINGS_MODULE` ex. `myproject.settings`
    - in `myproject.settings`:
        ```python
        from bukdjango_envsettings import update_from_env
            
        # by default all settings should  be allowed
        # but if any of them is still missing in the lib, `Exception` will be raised
        # see `conversion.py`
  
        update_from_env(
            pre='DJANGO_',
            allowed=[
                'SECRET_KEY',
                'SITE_ID',
            ])
       ```
    - all settings should be prefixed with `DJANGO_` by default, see 