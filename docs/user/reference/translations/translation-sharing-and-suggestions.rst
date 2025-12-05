Translation sharing and suggestions
===================================

.. include:: /includes/important_not_revised_help.rst

The same messages crop up in many places. For a simple example, think of
how often you've seen the phrase "Save as" in many different
applications.

This duplication of the same message happens across projects, within
different series of the same project and between an upstream project
that's translated in Launchpad and its Ubuntu packages.

There are two ways in which Launchpad can use this to reduce the amount
of work needed to translate a project:

-  translation suggestions: Launchpad will suggest a translation if
   it already has one in its database
-  translation sharing: when the same English strings appear in
   different versions (series) of a project, Launchpad will use the
   same translation across all these versions.

Translation suggestions
-----------------------

Whenever someone makes a translation in Launchpad it becomes part of
Launchpad's global database of translated strings. At the time of
writing, there are 1,619,290 English strings that have been translated
in up to `320
languages <https://translations.launchpad.net/+languages>`__ in
Launchpad. `Check the latest
numbers <https://translations.launchpad.net/>`__.

When Launchpad spots that you're about to work on an English message for
which it already has one or more translations in your language, it will
suggest those translations to you. You can then chose to accept one of
the suggestions or create a new translation that's better suited to the
project you're working with.

This is all possible because when people make translations in Launchpad
they agree to :ref:`license them with the flexible BSD
licence <translations-licensing-faq>`.

Translation sharing
-------------------

Translation sharing can happen both between different series of a
project and between a project and its Ubuntu package.

Both start out the same way:

1. Translation sharing happens between templates of the same name in
   more than one series, or in the project and its Ubuntu package.
2. English strings that are the same across those identically named
   templates are stored only once.
3. Any change to the translation of each English string for a specific
   language immediately appears in all these templates.

This means that the work of translating new versions of a project is
greatly reduced: whenever a new version (series) of a project is created
it will immediately inherit the translations for any English strings
that are kept from the earlier version. Thus a new version will start
out mostly translated without the need to import old translation files.
Any translation work done on the newer version will also keep the
translations in the older versions up-to-date and they won't become
stale.

On the other hand, translation reviewers can specifically chooses to
diverge one or more of the translations if they need to be different in
a specific version.

Similarly, translations made for the Ubuntu package of a project can be
shared upstream and vice versa.

How it works differs slightly, depending on whether you're sharing
translations between series of a project or between a project and its
Ubuntu package.

Sharing between series
~~~~~~~~~~~~~~~~~~~~~~

In Launchpad translations between the series of a project are always
shared. As soon as a translation is changed in one series it
automatically changes in all other series. You don't need to do anything
to enable this type of sharing.

Translation reviewers — i.e. for most projects, that'll be members of
the appropriate translation group, but for projects with an *Open*
translations policy that's everyone — can choose to diverge a
translation for a particular series. Those diverged translations are
then shown in the Launchpad UI as being different from the shared
translation.

Sharing between a project and its Ubuntu package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sharing translations between an upstream project and its Ubuntu package
works in a similar way. There are some differences, though:

-  you must link the relevant project series to its corresponding Ubuntu
   package
-  upstream translations are automatically shared with the Ubuntu
   package, unless the Ubuntu translators specifically chose a different
   translation
-  if the the upstream project uses Launchpad for translation work, a
   translation done in the Ubuntu packagage by a translator with the
   right permissions will also update that translation in the upstream
   project.

Enabling sharing between a project and its package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable translations sharing between a project and its Ubuntu package,
you need to:

-  link each project series to the relevant Ubuntu package (e.g. link
   series 1.0 of your project to the Ubuntu package for the Natty
   distro-series)
-  make sure there are templates with the same name for both the project
   and the package.

If the project is translated in Launchpad, you don't need to do
anything. However, if the project is translated outside Launchpad you'll
need to:

-  tell Launchpad where the translation work happens: follow the
   *Configure translations* link on the project's translations overview
   page
-  select an appropriate :ref:`translations permissions
   policy <choosing-a-permissions-policy>`
-  :ref:`import the project's translations into
   Launchpad <how-to-import-project-translations>`

Sharing upstream project translations with the Ubuntu package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once sharing is enabled, Launchpad will automatically copy any new
translations from the upstream project to the Ubuntu package.

On the translations web pages Ubuntu translators can chose to translate
individual strings differently for Ubuntu.

Sharing Ubuntu package translations with upstream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upstream projects can :ref:`manually export Ubuntu
translations <how-to-export-translations>` for use with their
project.

Launchpad can also automatically share translations made for the Ubuntu
package with the upstream project. To do so, the person making the
translation needs to have translation permission &mash; i.e. be a member
of the appropriate translations team — for both the Ubuntu package and
the project.