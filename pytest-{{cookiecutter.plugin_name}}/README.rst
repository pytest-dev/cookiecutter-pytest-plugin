{%- from "macros/rst" import doc_title, doc_subtitle -%}

{{ doc_title('pytest-' + cookiecutter.plugin_name) }}

.. image:: https://img.shields.io/pypi/v/pytest-{{cookiecutter.plugin_name}}.svg
    :target: https://pypi.org/project/pytest-{{cookiecutter.plugin_name}}
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-{{cookiecutter.plugin_name}}.svg
    :target: https://pypi.org/project/pytest-{{cookiecutter.plugin_name}}
    :alt: Python versions

.. image:: https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}/actions/workflows/main.yml/badge.svg
    :target: https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}/actions/workflows/main.yml
    :alt: See Build Status on GitHub Actions

{{cookiecutter.short_description}}

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "pytest-{{cookiecutter.plugin_name}}" via `pip`_ from `PyPI`_::

    $ pip install pytest-{{cookiecutter.plugin_name}}


Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `{{cookiecutter.license}}`_ license, "pytest-{{cookiecutter.plugin_name}}" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: https://opensource.org/licenses/MIT
.. _`BSD-3`: https://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: https://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: https://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
