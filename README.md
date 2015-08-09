============================
Cookiecutter Pytest Plugin
============================

[![Join Chat on Gitter.im][gitter_badge]][gitter]
[![See Build Status on Travis CI][travis_badge]][travis]
[![Documentation Status][docs_badge]][documentation]

Minimal [Cookiecutter] template for authoring [Pytest] plugins that help
you to write better programs.

Getting Started
---------------

Simply install [Cookiecutter] and generate a new Pytest plugin project:

    $ pip install cookiecutter
    $ cookiecutter https://github.com/pytest-dev/cookiecutter-pytest-plugin

Cookiecutter will ask you for some information regarding your plugin:

    full_name [Raphael Pierzina]: Andreas Pelme
    email [raphael@hackebrot.de]: andreas@pelme.se
    github_username [hackebrot]: pelme
    plugin_name [foobar]: awesome
    short_description [A simple plugin to use with Pytest]:
    version [0.1.0]:
    pytest_version [2.7.2]: 2.7.3
    year [2015]:

There you go - you just created a minimal Pytest plugin:

    pytest-awesome/
    ├── LICENSE
    ├── README.rst
    ├── pytest_awesome.py
    ├── setup.py
    ├── tests
    │   ├── conftest.py
    │   └── test_awesome.py
    └── tox.ini


Features
--------

- Installable [PyPI] package featuring a `setup.py`.
- Test suite running [Tox] and [Pytest] that makes sure your plugin is
  working as expected
- Comprehensive `README.rst` file that contains useful information
  about your plugin

Requirements to Submit Your Plugin to the Pytest Organization
-------------------------------------------------------------

-   PyPI presence with a setup.py that contains a license, pytest-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using Tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information,
    with matching info in setup.py.
-   an issue tracker unless you rather want to use the core Pytest
    issue tracker.

Please see the official guidelines at [Submit a Plugin].

Resources
---------

Please consult the [Pytest] docs for more information on hooks at
[Pytest Hook Reference].

Contribute
----------

We welcome you to contribute to this project. Please visit the [documentation] to get started!

Issues
------

This template has been tested on Mac OS X Yosemite.

If you encounter any problems, please [file an issue] along with a
detailed description.

License
-------

Distributed under the terms of the [MIT license], Cookiecutter Pytest
Plugin is free and open source software


  [gitter_badge]: https://badges.gitter.im/Join%20Chat.svg
  [gitter]: https://gitter.im/pytest-dev/cookiecutter-pytest-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge (Join Chat on Gitter.im)
  [travis_badge]: https://travis-ci.org/pytest-dev/cookiecutter-pytest-plugin.svg?branch=master
  [travis]: https://travis-ci.org/pytest-dev/cookiecutter-pytest-plugin (See Build Status on Travis CI)
  [docs_badge]: https://readthedocs.org/projects/cookiecutter-pytest-plugin/badge/?version=latest
  [documentation]: https://readthedocs.org/projects/cookiecutter-pytest-plugin/?badge=latest (Documentation Status)
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [Pytest]: https://github.com/pytest-dev/pytest
  [PyPI]: https://pypi.python.org/pypi
  [Tox]: https://tox.readthedocs.org/en/latest/
  [Submit a Plugin]: https://pytest.org/latest/contributing.html#submit-a-plugin-co-develop-pytest
  [Pytest Hook Reference]: https://pytest.org/latest/plugins.html#well-specified-hooks
  [MIT license]: http://opensource.org/licenses/MIT
  [file an issue]: https://github.com/pytest-dev/cookiecutter-pytest-plugin/issues
