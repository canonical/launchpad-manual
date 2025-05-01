Set up daily builds with ``bzr-builder``
========================================

``bzr-builder`` is the Bazaar plugin that helps you set up `daily builds in
Launchpad <Packaging/SourceBuilds>`__. You need to install it locally to
test your recipes and builds before you send them to Launchpad.

Installation
------------

The easiest way to install ``bzr-builder`` is to run ``apt-get install
bzr-builder``.

Alternatively, if you find you need a newer version than is packaged in
Ubuntu, you can pull down the branch from Launchpad and install it in
your Bazaar plugins directory:

::

   $ mkdir -p ~/.bazaar/plugins/
   $ bzr branch lp:bzr-builder ~/.bazaar/plugins/builder

To check if it is install and running, enter:

::

   $ bzr plugins -v

Looking for "builder" in the listed plugins.

Getting help
------------

Help for the plugin is available by running:

::

   $ bzr help builder

Help for the individual commands is available as:

::

   $ bzr help build
   $ bzr help dailydeb

Recipes
-------

``bzr-builder`` works with "recipes" that are descriptions of the steps
needed to construct a package from the various Bazaar branches.

`Read our guide to writing recipes <Packaging/SourceBuilds/Recipes>`__.

Running commands in recipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you may need run a partircular command in order to prepare a
branch for packaging.

``bzr-builder`` supports this through the ``run`` command.

.. note::
    Launchpad does not support the ``run`` command.

Let's say you need to run ``autoreconf -i`` at some point during the
build process. You'd add the following line to your recipe:

::

   run autoreconf -i

When ``bzr-builder`` reaches that point in the recipe it will run that
command.

If you place a ``run`` command in a ``nest`` section of a recipe
— i.e. indented by two spaces below a ``nest`` command — the command
will be run in the nested location.

For example:

::

   nest packaging lp:~team/project/ubuntu debian
     run cat control

The command is passed through the shell, so you can use shell
constructs, such as:

::

   run touch a && touch b

If the command exits with a non-zero error code then it will stop the
building of the package.

Building the recipe
~~~~~~~~~~~~~~~~~~~

In order to build the recipe you need to use the \`bzr dailydeb\`
command.

::

   $ bzr dailydeb package.recipe working-dir

This will perform the steps specified in ``package.recipe``. It will
create ``working-dir`` and put the resulting source tree and the source
package there.

You can examine the unpacked source tree and then build the source
package and install the results.

Next steps
----------

There's more in the `daily builds knowledge
base <Packaging/SourceBuilds>`__.