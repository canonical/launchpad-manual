.. _launchpad-project-translation-best-practices:

Launchpad project translation Best Practices
============================================

.. include:: /includes/important_not_revised_help.rst

This page provides a set of recommendations for managing translations
for your project on Launchpad.

.. note::
    There are many Launchpad translation features and options that
    are not discussed here. This page recommends a simple approach that may
    be the best fit for most projects.

.. note::
    If your project is used in Ubuntu Main, you need to consider
    whether it should be separately translated in your project or only in
    Ubuntu. This page assumes the project is not in Ubuntu Main (but it does
    apply to projects in Ubuntu Universe or Multiverse).

Assumptions
-----------

-  You have written a program using US English as its interface
   language, and now you want to have it translated into other languages
   using Launchpad
-  You have not yet done any internationalization (i18n) on your
   software project
-  No translations (localization, l10n) have been done

.. note::
    Messages in source code must be in US English. Gettext and
    Launchpad require this.

Demonstration project and user name
-----------------------------------

For examples in this page, let's assume:

-  The Launchpad project is named ``frobnob``. Like all projects, frobnob
   would be hosted at https://launchpad.net/frobnob/ on Launchpad.
-  Your user name is ``joe``.

.. note::
    The frobnob project does not exist on Launchpad. It is used
    here only for examples.

.. tip::
    If you have not yet created your project on Launchpad, :ref:`read
    about it here <registering-your-project>`.

Preparing the source code
-------------------------

Your source code has to be set up to support translation with GNU
gettext.

.. note::
    This step is called "internationalization (i18n)" because it
    enables the translation of your monolingual software.

GNU gettext
~~~~~~~~~~~

`GNU gettext <http://www.gnu.org/software/gettext/>`__ is the standard
internationalization framework used in most free software projects.

Gettext is installed by default in Ubuntu as the ``gettext`` package.

Gettext consists of:

-  Tools for developers and translators
-  A library that retrieves translations at run time

Your source code must use the gettext API.

The `gettext
manual <http://www.gnu.org/software/gettext/manual/gettext.html#Sources>`__
provides detailed explanations and has examples in the C programming
language. Other programming languages have their own APIs to the gettext
library, For example, Python has a `gettext
module <http://docs.python.org/library/gettext.html>`__.

Translation domain
~~~~~~~~~~~~~~~~~~

Gettext requires that your project has a unique translation doman. It
uses this domain and the user's locale (language and region) to find the
translation catalog that is used to retrieve translations at run time.

The translation domain is usually the name of the source package, which
should also be the name of your Launchpad Project (all lower case).

So in this case:

-  Launchpad Project: ``frobnob``
-  Source package name: ``frobnob``
-  Translation domain: ``frobnob``

The translation domain is used as the filename for your Launchpad
translation template. (In gettext terms, this is the pot file:
frobnob.pot.)

.. note::
    The translation domain is restricted to lowercase letters
    (a-z), numbers (0-9), dashes (-), and dots (.). (This is because the
    domain is used in Launchpad URLs. For example. LimeWire's template is
    named ``limewire``, and here is the Launchpad URL to it:
    https://translations.launchpad.net/limewire/trunk/+pots/limewire)

Important Notes on Gettext
~~~~~~~~~~~~~~~~~~~~~~~~~~

It is important that you use the gettext API in your source code
properly. Otherwise:

-  Translators may not have enough information
-  Plurals may not be properly translated

In short, your translations may not be of high quality and other
problems may occur.

So, take some time to review the gettext manual, especially where it
explains `pitfalls when marking translatable
strings <http://www.gnu.org/software/gettext/manual/gettext.html#Preparing-Strings>`__.

Please:

-  Avoid these pitfalls.
-  Add comments to provide translators helpful information. Placing a
   comment that begins with ``TRANSLATORS:`` before a translatable string
   creates a comment.
-  Use `translation
   contexts <http://www.gnu.org/software/gettext/manual/gettext.html#Contexts>`__
   where appropriate.

Building the template
---------------------

All messages in the sources code that are marked for translation with
the gettext API are extracted into the ``template``. (In gettext terms,
this is the pot file).

In our example, the template is ``po/frobnob.pot``.

.. note;;

All translation-specific files are in the po/ directory.

You need to keep the template consistent with the set of messages in the
source code by regenerating it whenever source code changes.

.. tip::
    Set up the package to use ``intltool``. With intltool, you
    generate/update the template with

::

   intltool-update -p

(in the po/ directory). This approach supports a wide range of source
code file types, such as C and Python, desktop files, gconf, and more.

The template is what tells Launchpad what messages are in your source
code that need translations, so updating it is critical.

.. note::
    At a lower level, intltool uses the `xgettext
    program <http://www.gnu.org/software/gettext/manual/gettext.html#Template>`__
    to create the template. You can use that approach as well. In this case
    you will need to explicitly set the filename of the generated template with the

::

   -o frobnob.pot

option.

Setting up your package for template generation is an important and
non-trivial topic and is covered elsewhere.

.. note:: 
    Some source packages have multiple templates (for example
    `gtk+2.0 <https://translations.launchpad.net/ubuntu/lucid/+source/gtk+2.0/+translations>`__).
    This is an advanced topic not covered here.

Creating a Bazaar branch
------------------------

Launchpad uses `Bazaar <http://www.bazaar-vcs.org/>`__ for source code
repositories. Launchpad Translations makes use of these to import
translation templates. Since your project needs to be Open Source in
order to use Launchpad for free, you should use this as the way to
publish your source code. Do *not* create a separate repository for your
i18n-related files.

If your project is stored locally in the ``frobnob`` directory, use these
commands to create a ``trunk`` branch on Launchpad:

::

   cd frobnob
   bzr init
   bzr add
   bzr commit -m "Initial commit."
   bzr push --remember lp:~joe/frobnob/trunk

.. note::
    Be sure to add the ``po/`` directory and the template file ``po/frobnob.pot`` to the branch.

.. note:: Template files are not usually added to a bzr branch because they are generated as needed. However, Launchpad Translations currently
    uses the template file to learn what messages need translation, so it is necessary at this time to add it to bzr source control. (We expect that
    this will not be necessary later.)

Whenever the source code changes and you generate a new template file,
update the branch on Launchpad with these commands:

::

   cd frobnob
   bzr add # Only if new files were created.
   bzr commit -m "Description of change."
   bzr push

You can view your branch in Launchpad by going to its URL
https://code.launchpad.net/~joe/frobnob/trunk.

Set up your project in Launchpad
--------------------------------

Enabling Translations
~~~~~~~~~~~~~~~~~~~~~

If not already done, enable translations for your project at this URL:
https://launchpad.net/frobnob/+configure-translations

Setting the source code branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may have noticed that you pushed the Bazaar branch to a URL under
your own name. Now you need to tell Launchpad that this is the main
source code location for your ``trunk`` series. A ``trunk`` series is a
required part of every Launchpad project.

Got to this URL https://launchpad.net/frobnob/trunk/+linkbranch and
select the branch named ~joe/frobnob/trunk. To do this, click on
``Choose`` and search for ``joe``. Your branch should come right up. Once
this is done, you can refer to it as simply ``lp:frobnob``.

Enabling translation imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you are ready to tell Launchpad to import your translation template
from the branch you pushed to Launchpad. Go to this URL to do so:
https://translations.launchpad.net/frobnob/trunk/+translations-settings

At the bottom of the left side of the page select the second option:
``Import template files``. Above that you see a reference to the official
Bazaar branch you created in the last step. Click on ``Save settings`` to
activate the import.

Importing the template into Launchpad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import of your template happens automatically whenever the file is
updated in the trunk branch. You can watch the progress of the import on
the import queue page for your project here:
https://translations.launchpad.net/frobnob/+imports. It is initially
marked as ``Approved`` and is later changed to ``Imported``. Depending on
the server load, the import may take a few hours but usually happens
much more quickly.

Once your template has been imported, you can see it in Launchpad at
this URL: https://translations.launchpad.net/frobnob/trunk/+pots/frobnob

Translation permission and group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You as the maintainer are most likely not the one doing the translations
into all the different languages. In fact, you may have come to
Launchpad Translations in order to find translators.

But how do you know the translations contributed through Launchpad and
its commununity are correct and of good quality? That's what translation
groups are for.

Take a look at the `Launchpad
translators <https://translations.launchpad.net/+groups/launchpad-translators>`__
group and you will see that it consists of translation teams for many
languages. The members of these teams are translation experts and are
usually native speakers. These are the people that will help you ensure
good quality translations.

So, go to https://translations.launchpad.net/frobnob/+settings and chose
``Launchpad Translators`` as the translation group and ``Structured`` as the
translation permission. Then set the translation focus to ``Frobnob
trunk`` and click ``Change``. Now translations for the languages covered by
Launchpad Translators can only be approved by the members of the
respective language team. Any registered user of Launchpad can still
make suggestions, but it is these teams that review and accept or
decline them.

Translate!
----------

Now the actual translating can start!

Please read the :ref:`Launchpad
Translators <launchpad-translators-group>`
instructions for project maintainers. You should also join the `team on
Launchpad <https://launchpad.net/~launchpad-translators>`__.

.. _exporting-translations-from-launchpad:

Exporting translations from Launchpad
-------------------------------------

Setting up export to your branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Translations done in Launchpad need to be exported back to your project
branch so that you can include them in releases of your software.
Launchpad provides automatic daily export of new translations to your
branch. Go to the settings page to enable this:
https://translations.launchpad.net/frobnob/trunk/+translations-settings

In the right column click ``Choose a target branch``, then enter
``lp:frobnob`` as the branch name and click ``Update``. This directs
Launchpad to export the translations into the same branch where it
imports the template from (the trunk branch). You can await the export
on the branches page under ``Recent revisions``:
https://code.launchpad.net/~joe/frobnob/trunk.

.. note::
    Exports only happen once a day and only if there are any new translations to export.

Updating your local branch
~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the translations to your local copy of the branch, simply
pull in the changes from Launchpad:

::

   cd frobnob
   bzr pull

The translations will be placed in the ``po`` directory where your
template file resides. They are in PO format and are named according to
the language code, e.g. ``po/fr.po`` for the French translations.

Deploying translations
----------------------

The translations are shipped with binary packages in the binary MO
format. MO files are created from PO files using the `gettext msgfmt
utility <http://www.gnu.org/software/gettext/manual/gettext.html#Binaries>`__.
MO files are usually installed as
``/usr/share/locale/ll/LC_MESSAGES/frobnob.mo`` where ``ll`` is the
respective language code. Remember that ``frobnob`` here is the
translation domain that you chose in the beginning. You should integrate
the MO file creation into the install portion of your build system, i.e.
include it in you Makefile.

.. tip::
    Set up your package to use standard approaches for mo file
    generation and distribution. Do not try to write your own. Check packages in Ubuntu Main to use as examples.

What if ... ?
-------------

Some help for special situations or issues you might encounter.

What if I made changes to my local copy of the branch while translations were exported into the Launchpad copy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When ever you make changes to your source code you should commit those
changes as described above. If Launchpad exported translations while you
committed to your local branch, the two copies will differ. A subsequent
``bzr push`` or ``bzr pull`` will complain about the branches having
diverged. You can simply merge the changes that Launchpad made to your
branch into your local copy and then push that updated version back out
to Launchpad. These are the commands to do that.

::

   cd frobnob
   bzr  merge lp:frobnob
   bzr commit -m "Merged translation exports."
   bzr push

Now both your branches will be identical again. You should not encounter
any conflicts during the merge because the translations export will only
touch PO files in the ``po`` directory which you should not be editing
manually when working with Launchpad.

What if the translation statistics never show my strings as "translated"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the translations overview page for your project, project series or
template, i.e. https://translations.launchpad.net/frobnob/trunk, you see
a color-coded status bar for each language. As they start out *red* when
all strings are untranslated, maintainers expect these to turn *green*
as translation work progresses. For projects that work entirely on
Launchpad, though, the target color is *purple* which means "Newly
translated in Launchpad".

There is work under way that will redefine and simplify the different
statuses.

What if I already have translations for my project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is least error-prone to do a full switch to using Launchpad
Translations. Any translations that you may already have when you begin
using Launchpad Translations can be imported, though, so they are not
lost. This assumes that these are already available in PO files.

Place the PO files into your ``po`` directory, named the same way as
Launchpad would do, e.g. ``po/fr.po`` for the French translations. Use
``bzr add``, ``bzr commit`` and ``bzr push`` as described earlier to copy them
to Launchpad. Now go to this page on Launchpad:
https://translations.launchpad.net/frobnob/trunk/+request-bzr-import and
click ``Request one-time import``. This will place all the translation
files into the import queue from where they will eventually be imported.

Please be aware that although all translations done in Launchpad are
BSD-licensed, translations imported like this retain their original
license.
