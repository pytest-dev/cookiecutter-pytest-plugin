# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('{{cookiecutter.plugin_name}}')
    group.addoption(
        '--foo',
        action='store',
        dest='foo',
        help='alias for --foo'
    )


@pytest.fixture
def bar(request):
    return request.config.option.foo
