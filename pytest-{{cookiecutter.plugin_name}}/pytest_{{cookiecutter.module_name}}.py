# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('{{cookiecutter.plugin_name}}')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default={{cookiecutter.year}},
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo
