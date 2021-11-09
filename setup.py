#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name='redis-python-client',
	version='0.1.0',
	description='redis client',
	long_description='redis client',
	packages=['redis_client'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'redis==3.0.0',
	],
	entry_points='''
''')
