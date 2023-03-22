"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


def _is_debug():
    # import sys
    # import os
    # return os.name == 'nt' or sys.platform == 'darwin'
    return True


if _is_debug():  # Debug
    from .local import *

else:  # Production
    from .prod import *

del _is_debug
