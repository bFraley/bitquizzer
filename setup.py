try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'bitquizzer',
    'author': 'Brett Fraley',
    'url': 'https://github.com/bFraley/bitquizzer',
    'license':'https://github.com/bFraley/bitquizzer/blob/master/LICENSE',
    'version': '1.0',
    'packages': ['bitquizzer-1.0'],
    'name': 'bitquizzer'
}

setup(**config)
