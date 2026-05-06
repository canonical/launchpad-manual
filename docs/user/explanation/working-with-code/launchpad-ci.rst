.. meta::
   :description: Understand how Launchpad CI helps improve the quality of your
      code when you want to contribute.

.. _continuous-integration:

Continuous integration
======================

Launchpad CI makes software development and collaboration easier.

You can use Launchpad CI to run tests to catch bugs before they are merged into
your project, to enforce coding standards by running linters, or to make sure
your project's documentation is still building.

How does this work?
-------------------

1. Create a ``.launchpad.yaml`` with your desired configuration.
2. Add it to the root of your repository
3. Push the changes to your project on Launchpad.

Launchpad will then run the configured CI jobs for your project and report the
status of the build in the UI via a green checkmark or a red ``X``.

In case of an error you will also receive an email.

.. note::

   Launchpad CI uses `lpci`_ (Launchpad CI runner) to execute your CI pipeline.
   You can also run `lpci` locally to test your configuration before pushing.

.. _lpci: https://lpci.readthedocs.io/

Example configuration
---------------------

A basic configuration file which runs the test suite of your project via
`pytest` would look as follows:

.. code-block:: yaml

   pipeline:
   - test

   jobs:
   test:
      series: noble
      architectures: amd64
      packages: [python3-pytest]
      run: pytest

You can find the complete configuration syntax in the lpci documentation linked
below.

Documentation
-------------

- `Configuration syntax`_ for ``.launchpad.yaml`` files.

.. _Configuration syntax:
   https://lpci.readthedocs.io/en/latest/configuration.html

Feature requests / known issues
-------------------------------

You can report feature requests and bugs to the Launchpad team using the `issue
tracker <https://bugs.launchpad.net/lpci>`__.

Support
-------

If you have any questions, please reach out to the
:ref:`Launchpad team <get-help>`.

Canonical employees can get support through the Launchpad channel on Mattermost.
