pytest-timebox
===================================

.. image:: https://travis-ci.org/comandrei/pytest-timebox.svg?branch=master
    :target: https://travis-ci.org/comandrei/pytest-timebox
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/comandrei/pytest-timebox?branch=master
    :target: https://ci.appveyor.com/project/comandrei/pytest-timebox/branch/master
    :alt: See Build Status on AppVeyor

py.test plugin to timebox your test suite


Features
--------

The intent of this plugin is to help enforce time budgets for time-sensitive test suites (like a smoke test for your application).
You can set a timebox in which your tests must run. If the limit is exceeded, the test session will fail.


Installation
------------

You can install "pytest-timebox" via `pip`_ from `PyPI`_::

    $ pip install pytest-timebox


Usage
-----

* py.test --timebox 300 # tests must run in under 5 minutes

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `BSD-3`_ license, "pytest-timebox" is free and open source software


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
.. _`file an issue`: https://github.com/comandrei/pytest-timebox/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
