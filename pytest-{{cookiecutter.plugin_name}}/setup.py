#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-{{cookiecutter.plugin_name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    maintainer='{{cookiecutter.full_name}}',
    maintainer_email='{{cookiecutter.email}}',
    license='{{cookiecutter.license}}',
    url='https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.rst'),
    py_modules=['pytest_{{cookiecutter.module_name}}'],
    install_requires=['pytest>={{cookiecutter.pytest_version}}'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        {% if cookiecutter.license == "MIT" -%}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == "BSD-3" -%}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.license == "GNU GPL v3.0" -%}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- elif cookiecutter.license == "Apache Software License 2.0" -%}
        'License :: OSI Approved :: Apache Software License',
        {%- endif %}
    ],
    entry_points={
        'pytest11': [
            '{{cookiecutter.plugin_name}} = pytest_{{cookiecutter.module_name}}',
        ],
    },
)
