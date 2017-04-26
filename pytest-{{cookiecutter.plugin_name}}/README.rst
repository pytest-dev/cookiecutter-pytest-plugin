{%- from "macros/rst" import doc_title, doc_subtitle -%}

{{ doc_title('pytest-' + cookiecutter.plugin_name) }}

.. image:: https://travis-ci.org/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}?branch=master
    :target: https://ci.appveyor.com/project/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}/branch/master
    :alt: See Build Status on AppVeyor

{{cookiecutter.short_description}}

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


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
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
