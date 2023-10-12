===================
Testing CLI scripts
===================

.. note::

    This is about testing scripts within the Launchpad context,
    not a general guide about testing CLI scripts.

    ``run_script`` should only be used for smoke tests as these kinds of
    end-to-end tests slow down the test suite.

Launchpad offers a convenient test helper for testing scripts,
which are usually found in the top level ``scripts`` folder.

.. code-block:: python

    from lp.testing.script import run_script

    returncode, stdout, stderr = run_script(
        script="scripts/script.py",
        args=["--help"],
    )

For more available options please have a look at the source code of
``run_script``.

.. note::

    ``run_script`` uses a subprocess to run the script. This has impact on both
    debugging via a Python debugger and on using ``strace``
    (use ``strace -f``).
