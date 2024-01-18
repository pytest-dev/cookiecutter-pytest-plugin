# Publish a Plugin

There are several ways to publish a [pytest] plugin.

Essentially pytest plugins are not different from any other Python Package, so
you may want to create a distribution and submit it to the Python Package Index
([PyPI]).

By doing so, enables your users to easily install via ``pip``.

## Python Package Index

Submitting to [PyPI] that includes the following steps:

- Configuring your plugin (which is already covered in this template)
- Creating a distribution for your project
- Uploading your pytest plugin to PyPI

Please see the official [Python Packaging User Guide] for detailed information.

## pytest-dev Organization

If you plan on submitting your plugin to the [pytest-dev organization] you need
to meet the following requirements:

-   PyPI presence with a pyproject.toml that contains a license, pytest-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information.
-   an issue tracker.

Please see the official guidelines at [Submit a Plugin].

  [pytest-dev organization]: https://github.com/pytest-dev/
  [Submit a Plugin]: https://pytest.org/latest/contributing.html#submit-a-plugin-co-develop-pytest
  [pytest]: https://github.com/pytest-dev/pytest
  [PyPI]: https://pypi.org/project
  [Python Packaging User Guide]: https://python-packaging-user-guide.readthedocs.io/en/latest/distributing.html
