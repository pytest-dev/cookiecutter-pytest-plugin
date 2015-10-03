# -*- coding: utf-8 -*-

"""
test_create_template
--------------------
"""


import os
import pytest
import subprocess

from cookiecutter.main import cookiecutter

TEMPLATE = os.path.realpath('.')


@pytest.fixture
def output_dir(tmpdir):
    return str(tmpdir.mkdir('output'))


def run_tox(plugin):
    """Run the tox suite of the newly created plugin."""
    try:
        subprocess.check_call([
            'tox',
            plugin,
            '-c', os.path.join(plugin, 'tox.ini'),
            '-e', 'py'
        ])
    except subprocess.CalledProcessError as e:
        pytest.fail(e)


def test_run_cookiecutter_and_plugin_tests(testdir, output_dir):
    """Create a new plugin via cookiecutter and run its tests."""
    cookiecutter(TEMPLATE, no_input=True, output_dir=output_dir)

    new_plugin = os.path.join(output_dir, 'pytest-foobar')
    assert os.path.isdir(new_plugin)

    run_tox(new_plugin)
