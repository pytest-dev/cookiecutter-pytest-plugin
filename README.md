# cookiecutter-pytest-plugin

[![Documentation Status][docs_badge]][documentation]

Minimal [Cookiecutter] template for authoring [pytest] plugins that help
you to write better programs.

> This template requires [Cookiecutter 1.4.0 "Shortbread"][Shortbread] or
> higher

## Getting Started

Install [Cookiecutter] and generate a new pytest plugin project:

```no-highlight
$ pip install cookiecutter
$ cookiecutter https://github.com/pytest-dev/cookiecutter-pytest-plugin
```

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [Raphael Pierzina]: Andreas Pelme
email [raphael@hackebrot.de]: andreas@pelme.se
github_username [hackebrot]: pelme
plugin_name [foobar]: awesome
module_name [awesome]: awesome
short_description [A simple plugin to use with pytest]:
version [0.1.0]:
pytest_version [2.9.1]:
Select docs_tool:
1 - mkdocs
2 - sphinx
3 - none
Choose from 1, 2, 3 [1]: 1
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0+
Choose from 1, 2, 3 [1]: 2
INFO:post_gen_project:Moving files for mkdocs.
```

There you go - you just created a minimal pytest plugin:

```no-highlight
pytest-awesome/
├── LICENSE
├── README.rst
├── pyproject.toml
├── src
│   └── pytest_awesome
│       ├── __init__.py
│       └── plugin.py
├── tests
│   ├── conftest.py
│   └── test_awesome.py
└── tox.ini
```


## Features

- Installable [PyPI] package featuring a `pyproject.toml`.
- Test suite running [tox] and [pytest] that makes sure your plugin is working
  as expected
- Working example code for a fixture, a cli option, as well as a pytest.ini
  option
- Comprehensive `README.rst` file that contains useful information about your
  plugin
- Continuous integration configuration for [AppVeyor]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, such as [MIT], [BSD-3], [Apache v2.0], [GNU GPL
  v3.0+], or [MPL v2.0]

## Requirements to Submit a Plugin

If you plan on submitting your plugin to the [pytest-dev organization] you need
to meet the following requirements:

-   PyPI presence with a pyproject.toml that contains a license, pytest-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information.
-   an issue tracker

Please see the official guidelines at [Submit a Plugin].

## Resources

Please consult the [pytest] docs for more information on hooks at
[pytest hook reference].

## Contribute

We welcome you to contribute to this project. Please visit the [documentation]
to get started!

## Issues

If you encounter any problems, please [file an issue] along with a
detailed description.

## Code of Conduct

Everyone interacting in the Cookiecutter pytest Plugin project's codebases,
issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA
Code of Conduct].

## License

Distributed under the terms of the [MIT license], Cookiecutter pytest
Plugin is free and open source software.

[![OSI certified][osi_certified]][OSI]


  [pytest-dev organization]: https://github.com/pytest-dev/
  [docs_badge]: https://readthedocs.org/projects/cookiecutter-pytest-plugin/badge/?version=latest
  [documentation]: https://cookiecutter-pytest-plugin.readthedocs.io/en/latest/ (Documentation)
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pytest]: https://github.com/pytest-dev/pytest
  [PyPI]: https://pypi.org/project
  [tox]: https://tox.readthedocs.io/en/latest/
  [Submit a Plugin]: https://docs.pytest.org/en/latest/contributing.html#submitting-plugins-to-pytest-dev
  [pytest hook reference]: https://docs.pytest.org/en/latest/writing_plugins.html#pytest-hook-reference
  [MIT license]: https://opensource.org/licenses/MIT
  [file an issue]: https://github.com/pytest-dev/cookiecutter-pytest-plugin/issues
  [Sphinx]: https://sphinx-doc.org/
  [MkDocs]: https://www.mkdocs.org/
  [MIT]: https://opensource.org/licenses/MIT
  [MPL v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
  [BSD-3]: https://opensource.org/licenses/BSD-3-Clause
  [GNU GPL v3.0+]: https://www.gnu.org/licenses/gpl-3.0.txt
  [Apache v2.0]: https://www.apache.org/licenses/LICENSE-2.0
  [AppVeyor]: https://www.appveyor.com/
  [PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
  [Shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
  [osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
  [OSI]: https://opensource.org/
