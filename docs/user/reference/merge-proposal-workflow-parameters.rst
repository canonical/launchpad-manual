.. meta::
   :description: Reference for the parameters you can set in a merge proposal
      description to configure the validation workflow.

.. _merge-proposal-workflow-parameters:

Merge proposal workflow parameters
==================================

The :ref:`merge proposal validation workflow
<merge-proposal-validation-workflow>` can be tuned with parameters that you add
to the **end of the merge proposal description**. Each parameter is written on
its own line in the form:

.. code-block:: text

   <Key>: <value>

This reference lists the supported keys.


Available parameters
--------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Key
     - Explanation
   * - ``Autopkgtest-Trigger``
     - Add additional "from proposed" triggers to the autopkgtest, for example
       to test the package together with other proposed packages.
   * - ``Autopkgtest-All-Proposed``
     - Defaults to ``False``. Set to ``True`` to run the autopkgtests against
       all proposed packages.
   * - ``Activate-Workflow``
     - Defaults to ``True`` once the feature is fully released. Set to ``False``
       to opt this merge proposal out of the workflow.

Planned parameters
------------------

The following parameters are planned for future releases and are not yet
available:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Key
     - Explanation
   * - ``PPA-Size``
     - Future improvement to allow larger PPA sizes for large packages.
   * - ``PPA-Dependencies``
     - Future improvement to select dependencies from ``release`` or
       ``proposed`` (default).

Example
-------

.. code-block:: text

   This merge proposal fixes the foo crash on startup.

   Autopkgtest-All-Proposed: True
   Autopkgtest-Trigger: bar/1.2-3

See also
--------

- :ref:`Merge proposal validation workflow <merge-proposal-validation-workflow>`
- :ref:`Use the merge proposal validation workflow <use-merge-proposal-validation-workflow>`
