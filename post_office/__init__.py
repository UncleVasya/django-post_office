import django

VERSION = '3.6.3+jw.1'

from .backends import EmailBackend

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'post_office.apps.PostOfficeConfig'
