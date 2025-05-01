Use the Trac plugin
===================

Launchpad can communicate directly with bug trackers that use Trac
through the `trac-launchpad <https://launchpad.net/trac-launchpad>`__
plugin.

If you run a Trac instance, you can use the plugin to:

-  share comment histories between bugs that are tracked both in your
   Trac tracker and also in Launchpad
-  reduce the server load of bug watches from Launchpad.

To start using the plugin, you need to install it in your Trac
environment and also tell Launchpad that you're using the plugin.

Prerequisites
-------------

Before installing the Launchpad plugin for Trac, you need to have the
following:

-  Trac 0.10.x or 0.11
-  Setuptools for Python
-  `TracXMLRPC Plugin <http://trac-hacks.org/wiki/XmlRpcPlugin>`__ (this
   must be installed for any Trac instance to which you wish to add the
   Launchpad plugin).
-  (for Trac 0.11+) Genshi 0.5 or better
-  (for Trac 0.10) a couple of patches to the Trac core (see
   `below <#patching-0.10>`__).

Get the plugin
--------------

You can download the plugin from its `Launchpad project
page <https://launchpad.net/trac-launchpad/+download>`__.

Patch Trac ``0.10``
-------------------

If you're using ``Trac 0.10``, you need to apply the patches, provided in the
``0.10-patches`` directory of the trac-launchpad tarball, to your current
Trac installation:

::

   $ cd /path/to/trac; patch -p1 < /path/to/trac-launchpad/0.10-patches/*

System-wide installation
------------------------

To install the plugin, unpack the tarball to ``/tmp`` and run ``python
setup.py install`` in the unpacked directory:

::

   $ cd /tmp
   $ tar zxvf /path/to/trac-launchpad-0.1.2.tgz
   $ cd trac-launchpad
   $ sudo python setup.py install

Activating the plugin
---------------------

To activate the plugin in a specific Trac instance, edit
``$TRAC_ENV/conf/trac.ini`` and add the following lines:

::

   [components]
   tracrpc.* = enabled
   tracext.launchpad.* = enabled

   [ticket-custom]
   launchpad_bug = text
   launchpad_bug.label = Launchpad Bug

You must then grant the special ``launchpad`` user permission to access
the XML-RPC interface, by executing:

::

   $ trac-admin $TRAC_ENV permission add launchpad XML_RPC
   $ trac-admin $TRAC_ENV permission add launchpad LAUNCHPAD_RPC

After restarting your webserver, launchpad should be able to sync bugs.
In order to verify whether the plugin was enabled correctly, you can
always log in with TRAC_ADMIN privileges and then visit
``$YOUR_TRAC_URL/plugins`` if you have version ``0.11``.

Get Launchpad to work with your bugtracker
------------------------------------------

Once the plugin is installed and working, you need to register your
bugtracker with Launchpad, if it isn't already registered.

**Step 1:** Visit https://launchpad.net/bugs/bugtrackers

**Step 2:** Check to see if your bugtracker is registered. If it isn't,
click the `Register another
bugtracker <https://launchpad.net/bugs/bugtrackers/+newbugtracker>`__
link at the bottom of the page.

**Step 3:** Enter your bugtracker's details and click the ``Add``
button.

**Step 4:** Your bug tracker should now show up in the list of
`registered bugtrackers <http://launchpad.net/bugs/bugtrackers>`__.

**Step 5:** Look through Launchpad to find bugs that are being tracked
in Launchpad that are also tracked in your instance of Trac and then
link the Launchpad bug reports to your reports in Trac. For example: if
there's an Ubuntu package of your software, look to see if there are any
bugs filed against that package that you're also tracking upstream.

Can't find suitable bugs in Launchpad?
--------------------------------------

If you can't see any suitable bugs already in Launchpad, you can create
some test bugs in Launchpad's `staging
environment <https://staging.launchpad.net>`__.

.. note::
    The database for staging is reset every day with a fresh copy
    of Launchpad's live production database. This can have two impacts:

-  your test bugs will disappear from staging within the next 24 hours
-  if you've added your bug tracker to Launchpad's production
   environment in the past 24 hours, you need to add it manually to
   staging.

Troubleshooting
---------------

To set up a test tokenserver, edit the environment's ``trac.ini`` as
follows:

::

   [launchpad]
   auth_server = http://localhost:8081/tokens/%s/+bugtracker-handshake

Find ``simple_tokenserver.py`` in the tarball and run as follows:

::

   $ python simple_tokenserver.py +

The plus gives the default policy, which allows all requested tokens to
match.

Now visit ``$TRAC_URL/launchpad-auth/abc`` in your browser, and you
should get an "OK" along with a cookie. Now visit ``$TRAC_URL/xmlrpc``
and you should get a listing of XML-RPC endpoints. If you get a listing
but Launchpad is not in it, check the permissions for the launchpad
user.

Next steps
----------

Once you've installed the plugin, `file a question using Launchpad
Answers <https://answers.launchpad.net/malone>`__ to let the Launchpad
team know that you're running the plugin. This will allow the Launchpad
Bugs developers and sys admins to finish the setup from their end.

If you'd like to write a Launchpad plugin for another bug tracker,
follow our `plugin API spec <Bugs/PluginAPISpec>`__.