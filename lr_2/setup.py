#!/usr/bin/env python

from distutils.core import setup

setup(name='SERIAlizer',
      version='1.0',
      description='Serializer for objects(json/yaml/toml)',
      author='therealyou',
      install_requires=['PyYAML', 'toml', 'pytest'],
      packages=['Serializers', 'Console'],
      #scripts=['Console/ctrl.py']
     )