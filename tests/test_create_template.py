import os
import pytest
import subprocess


def run_tox(plugin):
    """Run the tox suite of the newly created plugin."""
    try:
        subprocess.check_call([
            'tox',
            '--workdir', plugin,
            '-c', os.path.join(plugin, 'tox.ini'),
            '-e', 'py',
        ])
    except subprocess.CalledProcessError as e:
        pytest.fail(str(e))


def test_run_cookiecutter_and_plugin_tests(cookies):
    """Create a new plugin via cookiecutter and run its tests."""
    result = cookies.bake(extra_context={'plugin_name': 'foo-bar'})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'pytest-foo-bar'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('src', 'pytest_foo_bar', '__init__.py').is_file()
    assert result.project_path.joinpath('src', 'pytest_foo_bar', 'plugin.py').is_file()
    assert result.project_path.joinpath('tests', 'test_foo_bar.py').is_file()

    run_tox(str(result.project_path))
