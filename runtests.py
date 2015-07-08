#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import os, sys

import django
from django.conf import settings

if not settings.configured:
    settings_dict = dict(
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware'
        ),
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'data_importer',
            'data_importer.tests',
        ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3"
            }
        },
    )

    settings.configure(**settings_dict)

django.setup()


def runtests(*test_args):

    if not test_args:
        test_args = ['data_importer']

    # try to set more used args to django test
    test_kwargs = {
        'pattern': 'test*.py',
        'verbosity': 1,
        'noinput': False,
        'failfast': False,
        'interactive': True,
    }
    for i, arg in enumerate(sys.argv):
        if arg.startswith('-v'):
            _value = arg.replace('-v', '')
            if len(_value):
                test_kwargs['verbosity'] = int(_value)
            else:
                test_kwargs['verbosity'] = int(sys.argv[i + 1])
        if arg == '--noinput':
            test_kwargs['noinput'] = True
        if arg == '--failfast':
            test_kwargs['failfast'] = True

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    from django.test.runner import DiscoverRunner
    failures = DiscoverRunner(**test_kwargs).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
