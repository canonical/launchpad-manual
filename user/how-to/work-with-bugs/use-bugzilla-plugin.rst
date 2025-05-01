Use the Bugzilla plugin
=======================

Launchpad can communicate directly with bug trackers that use Bugzilla
through the
`bugzilla-launchpad <http://launchpad.net/bugzilla-launchpad>`__ plugin.

If you run a Bugzilla instance, you can use the plugin to:

-  share comment histories between bugs that are tracked both in your
   Bugzilla tracker and also in Launchpad
-  reduce the server load of bug watches from Launchpad.

To start using the plugin, you need to install it in your Bugzilla
environment and also tell Launchpad that you're now using the plugin.

Version numbers
---------------

The version number of the plugin shows two things:

::

   <plugin version>-<bugzilla version>

``<plugin version>`` is the version of the plugin.

``<bugzilla version>`` is the version of Bugzilla that the plugin is compatible with.

So, a plugin instance with a version number of ``0.9-3.2`` means that
this is version 0.9 of the plugin and it is compatible with Bugzilla
version 3.2.

Get the plugin
--------------

You can download the plugin from its `Launchpad project
page <https://launchpad.net/bugzilla-launchpad/+download>`__. Make sure
you get the right plugin `for your version <#versioning>`__ of Bugzilla.

Install the plugin
------------------

(Wherever it says in these instructions, we mean "the plugin version
number goes here".)

**Step 1:** Untar the package:

::

     tar -xzf bugzilla-launchpad-<version>.tar.gz

**Step 2:** Change to your Bugzilla directory:

::

     cd /path/to/bugzilla

.. tip::
    That's probably /var/www/html/bugzilla if you followed the
    standard Bugzilla installation instructions.

**Step 3:** Apply the patch to your Bugzilla installation:

::

     patch -p0 -i /path/to/bugzilla-launchpad-<version>/patch.diff

It's worth noting that the patch was written and reviewed by core
Bugzilla developers. If you're running Red Hat or an older Fedora, you
might have to fix the SELinux permissions on the files after applying
the patch:

::

     /sbin/restorecon -Rv ./

**Step 4:** Install the extension:

::

     mv /path/to/bugzilla-launchpad-<version>/launchpad extensions/

**Step 5:** Run checksetup.pl to install the plugin:

::

     ./checksetup.pl

**Step 6:** checksetup.pl will direct you to a URL to finish the
installation.

And now the plugin should be working!

Get Launchpad to work with your bugtracker
------------------------------------------

Once the plugin is installed and working you need to register your
bugtracker with Launchpad, if it isn't already registered.

This is really simple to do:

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
in Launchpad that are also tracked in your instance of Bugzilla and then
link the Launchpad bug reports to your reports in Bugzilla. For example:
if there's an Ubuntu package of your software, look to see if there are
any bugs filed against that package that you're also tracking upstream.

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

Next steps
----------

Once you've installed the plugin, `file a question using Launchpad
Answers <https://answers.launchpad.net/malone>`__ to let the Launchapd
team know that you're running the plugin. This will allow the Launchpad
Bugs developers and sys admins to finish the setup from their end.

If you'd like to write a Launchpad plugin for another bug tracker,
follow our `plugin API spec <Bugs/PluginAPISpec>`__.