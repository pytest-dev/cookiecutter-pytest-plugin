# Publish a Plugin

There are several ways to publish a [Pytest] plugin.

Essentially Pytest plugins are not different from any other Python Package, so
you may want to create a distribution and submit it to the Python Package Index ([PyPI]).

By doing so, enables your users to easily install via ``easy-install`` or ``pip``.

Please see the official [Python Packaging User Guide] for detailed information.

## Requirements to Submit a Plugin

If you plan on submitting your plugin to the [pytest-dev organization] you need
to meet the following requirements:

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

  [pytest-dev organization]: https://github.com/pytest-dev/
  [Submit a Plugin]: https://pytest.org/latest/contributing.html#submit-a-plugin-co-develop-pytest
  [Pytest]: https://github.com/pytest-dev/pytest
  [PyPI]: https://pypi.python.org/pypi
  [Python Packaging User Guide]: https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
