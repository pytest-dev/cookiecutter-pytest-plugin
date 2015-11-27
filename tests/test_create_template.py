# -*- coding: utf-8 -*-

"""
test_create_template
--------------------
"""


import os
import pytest
import subprocess


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


def test_run_cookiecutter_and_plugin_tests(cookies):
    """Create a new plugin via cookiecutter and run its tests."""
    result = cookies.bake(extra_context={'plugin_name': 'foo-bar'})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'pytest-foo-bar'
    assert result.project.isdir()
    assert result.project.join('pytest_foo_bar.py').isfile()
    assert result.project.join('tests', 'test_foo_bar.py').isfile()

    run_tox(str(result.project))
