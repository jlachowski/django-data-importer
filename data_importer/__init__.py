# coding: utf-8
VERSION = (0, 3, 1)


def get_version():
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])


__version__ = get_version()
