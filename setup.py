#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import setuptools
from setuptools import setup

# Cargar la versión sin importar tastypie
about = {}
with open(os.path.join("tastypie", "version.py")) as f:
    exec(f.read(), about)

setup(
    name='django-tastypie',
    version=about["__version__"],
    description='A flexible & capable API layer for Django.',
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='https://github.com/django-tastypie/django-tastypie',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'tastypie',
        'tastypie.utils',
        'tastypie.management',
        'tastypie.management.commands',
        'tastypie.migrations',
        'tastypie.contrib',
        'tastypie.contrib.gis',
        'tastypie.contrib.contenttypes',
    ],
    package_data={
        'tastypie': ['templates/tastypie/*'],
    },
    zip_safe=False,
    requires=[
        'python_mimeparse(>=0.1.4, !=1.5)',
        'dateutil(>=2.1)',
    ],
    install_requires=[
        'python-mimeparse >= 0.1.4, != 1.5',
        'python-dateutil >= 2.1',
    ],
    tests_require=['PyYAML', 'lxml', 'defusedxml'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Utilities'
    ],
)
