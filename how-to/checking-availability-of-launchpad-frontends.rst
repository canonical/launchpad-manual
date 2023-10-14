============================================
Checking availability of Launchpad frontends
============================================


Launchpad is using round-robin DNS to load balance requests among the
frontends.

So in order to check the availability of the frontends,
you need to get a list of all frontends and then check them individually.

Get list of frontends
=====================

.. code-block:: shell-session

    $ host launchpad.net

    launchpad.net has address 185.125.189.223
    launchpad.net has address 185.125.189.222
    launchpad.net has IPv6 address 2620:2d:4000:1001::8003
    launchpad.net has IPv6 address 2620:2d:4000:1001::8004
    launchpad.net mail is handled by 10 mx.launchpad.net.

Check individual frontend
=========================

.. code-block:: shell-session

    $ curl --resolve launchpad.net:443:185.125.189.222 https://launchpad.net/ 


More infos on `using curl <https://everything.curl.dev/usingcurl/connections/name#provide-a-custom-ip-address-for-a-name>`_.
