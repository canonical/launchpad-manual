.. meta::
   :description: Overview of the valid_until_config on a distroseries

.. _valid-until-config:

Valid-Until configuration for distribution series
==================================================

Overview
--------

The ``valid_until_config`` feature adds support for configuring 
``Valid-Until`` tags in APT repository Release files for Launchpad 
distribution series. This allows fine-grained control over how long 
repository metadata remains valid, improving security by ensuring clients 
regularly refresh repository information.

What is Valid-Until?
---------------------

The ``Valid-Until`` field in APT Release files specifies an expiration 
timestamp for repository metadata. APT clients will refuse to use Release 
files that have expired, forcing them to fetch fresh metadata. This security 
feature helps prevent replay attacks and ensures clients have up-to-date 
repository information.

Permissions
-----------

The ``valid_until_config`` property can be:

-  **Read** by anyone with access to view the distribution series
-  **Modified** only by users with edit permissions on the distribution 
   series (typically distribution owners and administrators)

For API access, see the `DistroSeries API documentation 
<https://api.launchpad.net/devel.html#distro_series>`_.

Example usage
-------------

The following example demonstrates how to configure ``valid_until_config`` 
for a distribution series using the Launchpad API::

    In [5]: stonking = lp.load(
    ...    "https://api.launchpad.net/devel/ubuntu/stonking")

    In [6]: stonking.valid_until_config
    Out[6]: {}

    In [7]: stonking.valid_until_config = {
    ...    'Backports': {'refresh_threshold': 7, 'validity_period': 14}}

    In [8]: stonking.lp_save()

    In [9]: stonking.valid_until_config
    Out[9]: {'Backports': {'refresh_threshold': 7, 'validity_period': 14}}

This configurations above is used during the publishing runs:

-  ``refresh_threshold``: Refresh the Valid-Until tag, when it is within this 
   many days from being expired. 
-  ``validity_period``: The number of days before expiration at which the 
   Valid-Until value is refreshed.


