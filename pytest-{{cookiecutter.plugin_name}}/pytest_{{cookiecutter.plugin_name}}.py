# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('{{cookiecutter.plugin_name}}')
    group.addoption(
        '--foo',
        action='store_const',
        dest='foo',
        help='alias for --foo'
    )
