# coding: utf-8
from __future__ import absolute_import
VERSION = (0, 1, 2)

from .base import BaseImporter, ValidationError
from .readers import *
#from . import tests


def get_version():
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])


__version__ = get_version()
