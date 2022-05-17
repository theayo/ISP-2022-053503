#!/usr/bin/env python

from distutils.core import setup

setup(name='SERIA',
      version='1.0',
      description='Serializer for objects(json/yaml/toml)',
      author='alohadance',
      install_requires=['PyYAML', 'qtoml'],
      packages=['Serializers', 'Console']
      )
