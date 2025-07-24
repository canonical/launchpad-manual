Landing updates for Loggerhead
==============================

`Loggerhead <https://launchpad.net/loggerhead/>`_ is a web-based
`Bazaar <https://en.wikipedia.org/wiki/GNU_Bazaar>`_ code browser.

Landing changes for Loggerhead itself
-------------------------------------

- create a merge proposal for https://launchpad.net/loggerhead
- get approval
- mark merge proposal as **Approved**

Landing changes in Launchpad itself
-----------------------------------

- ask somebody with PyPI access to make a loggerhead release
- see :ref:`Upgrade a Package <upgrade-package>`

Performing QA
-------------

.. The following link does not work.

.. XXX 2023-10-14: jugmac00 - need to verify whether it should actually work

After the changes have landed and passed through buildbot,
they will be available at https://bazaar.staging.launchpad.net.

Please note that only a few Bazaar branches are synced from production to
staging.

You should create a repository and push some changes to perform QA:

.. code-block:: bash

    bzr push lp://staging/~you/+junk/foo

Deployment
----------

To get the changes into production, you need to perform a regular Launchpad
deployment.
