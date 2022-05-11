#!/usr/bin/env python

from distutils.core import setup

setup(name='',
      version='1.0',
      description='Serializer for objects',
      author='therealyou',
      install_requires=['PyYAML', 'toml', 'pytest'],
      packages=['distutils', 'distutils.command'],
     )