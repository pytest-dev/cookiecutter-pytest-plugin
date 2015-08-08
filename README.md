----------------------------
Cookiecutter Pytest Plugin
----------------------------

[![Join Chat on Gitter.im]]

[![See Build Status on Travis CI]]

[![Documentation Status]]

Minimal [Cookiecutter] template for authoring [pytest] plugins that help
you to write better programs.

Usage
=====

Simply install [Cookiecutter] and generate a new Pytest plugin project:

    $ pip install cookiecutter
    $ cookiecutter https://github.com/pytest-dev/cookiecutter-pytest-plugin


Features
========

-   Installable [PyPI] package featuring a `setup.py`.
-   Test suite running [tox] and [pytest] that makes sure your plugin is
    working as expected
-   Comprehensive `README.rst` file that contains useful information
    about your plugin

Requirements to Submit Your Plugin
==================================

-   PyPI presence with a setup.py that contains a license, pytest-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information,
    with matching info in setup.py.
-   an issue tracker unless you rather want to use the core pytest
    issue tracker.

Please see the official guidelines at [Submit a Plugin].

Resources
=========

Please consult the [pytest] docs for more information on hooks at
[Pytest Hook Reference].

License
=======

Distributed under the terms of the [MIT license], Cookiecutter Pytest
Plugin is free and open source software

Issues
======

This template has been tested on Mac OS X Yosemite.

If you encounter any problems, please [file an issue] along with a
detailed description.

  [Join Chat on Gitter.im]: https://badges.gitter.im/Join%20Chat.svg
  [![Join Chat on Gitter.im]]: https://gitter.im/pytest-dev/cookiecutter-pytest-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
  [See Build Status on Travis CI]: https://travis-ci.org/pytest-dev/cookiecutter-pytest-plugin.svg?branch=master
  [![See Build Status on Travis CI]]: https://travis-ci.org/pytest-dev/cookiecutter-pytest-plugin
  [Documentation Status]: https://readthedocs.org/projects/cookiecutter-pytest-plugin/badge/?version=latest
  [![Documentation Status]]: https://readthedocs.org/projects/cookiecutter-pytest-plugin/?badge=latest
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pytest]: https://github.com/pytest-dev/pytest
  [PyPI]: https://pypi.python.org/pypi
  [tox]: https://tox.readthedocs.org/en/latest/
  [Submit a Plugin]: https://pytest.org/latest/contributing.html#submit-a-plugin-co-develop-pytest
  [Pytest Hook Reference]: https://pytest.org/latest/plugins.html#well-specified-hooks
  [MIT license]: http://opensource.org/licenses/MIT
  [file an issue]: https://github.com/pytest-dev/cookiecutter-pytest-plugin/issues
