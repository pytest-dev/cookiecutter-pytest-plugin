# User Guide

## What is Cookiecutter?

[Cookiecutter] is a command-line utility that creates projects from **cookiecutters** (project
templates), e.g. creating a Python package project from a Python package project template.

## Installation

Cookiecutter is available on [PyPI]. Use ``pip`` to download and install:

```no-highlight
$ pip install cookiecutter
```

## Usage

You can generate a new project from a template by using the following command:

```no-highlight
$ cookiecutter https://github.com/pytest-dev/cookiecutter-pytest-plugin
```

This will not only ``git clone`` the template but also start the generation process.

## Template Variables

Each Cookiecutter template uses variables, which are specified in the template, that
it replaces in all of the directory and file names, but also in text such as source code
or markdown formats.

### Plugin Details

Cookiecutter prompts you for information regarding your plugin based on aforementioned variables:

```no-highlight
full_name [Raphael Pierzina]: Andreas Pelme
email [raphael@hackebrot.de]: andreas@pelme.se
github_username [hackebrot]: pelme
plugin_name [foobar]: awesome
short_description [A simple plugin to use with pytest]:
version [0.1.0]:
pytest_version [2.9.0]: 2.9.1
```

The values in the square brackets (f.i. ``[foobar]``) are defaults for the according variables.

## Project Generation

Once you answered to the questions, Cookiecutter renders the the project:

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

There you go - you just created a minimal pytest plugin:

  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [PyPI]: https://pypi.org/project/cookiecutter
