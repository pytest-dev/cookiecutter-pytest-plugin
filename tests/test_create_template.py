# -*- coding: utf-8 -*-

"""
test_create_template
--------------------
"""


import os
import pip
import pytest
import shutil
import subprocess

from cookiecutter.main import cookiecutter


TEMPLATE = os.path.realpath('.')


@pytest.fixture(autouse=True)
def clean_tmp_dir(tmpdir, request):
    """
    Remove the project directory that is created by cookiecutter during the
    tests.
    """
    tmp_cwd = tmpdir.mkdir('cookiecutter_out')
    os.chdir(str(tmp_cwd))

    def remove_project_dir():
        if os.path.isdir('pytest-foobar'):
            shutil.rmtree('pytest-foobar')
    request.addfinalizer(remove_project_dir)


def test_run_cookiecutter_cli_and_plugin_tests(testdir):
    try:
        subprocess.check_call(['cookiecutter', '--no-input', TEMPLATE])
    except subprocess.CalledProcessError as e:
        pytest.fail(e)

    project_root = 'pytest-foobar'
    assert os.path.isdir(project_root)

    os.chdir(str(project_root))
    pip.main(['install', '.'])

    if testdir.runpytest().ret != 0:
        pytest.fail('Error running the tests of the newly generated plugin')


def test_run_cookiecutter_and_plugin_tests(testdir):
    cookiecutter(TEMPLATE, no_input=True)

    project_root = 'pytest-foobar'
    assert os.path.isdir(project_root)

    os.chdir(str(project_root))
    pip.main(['install', '.'])

    if testdir.runpytest().ret != 0:
        pytest.fail('Error running the tests of the newly generated plugin')
