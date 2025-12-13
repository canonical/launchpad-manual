.. _translation-groups:

Translation groups
==================

.. include:: /includes/important_not_revised_help.rst

Launchpad makes it easy for anyone to make or suggest translations for a
free software project. Each project can choose a :ref:`review
policy <choosing-a-permissions-policy>` that lets them find a
balance between encouraging spontaneous contributions and maintaining
high quality translations.

This is where translation groups come in. They're umbrella organisations

-  made up of teams and individuals - that work with one or more
   projects to review translations.

When a project owner activates Launchpad Translations for their project,
they choose which translation group they want to work with. In effect,
they delegate the review of their project's translations to the people
in that group.

To maintain the quality of their project's localisation, project owners
should find someone they trust who can review those translations, and
translation groups are a convenient way to delegate responsibility for
reviews.

Each translation group is made up of teams and individuals who have
taken responsibility for a particular language. Although the groups
often start life associated with only one project, they are independent
and can work with any project in Launchpad. So, a project ownercan either
choose to work with an existing translation group or create their own.

Within each translation group, an individual or team is assigned to look
after one or more languages. When you choose a translation group, you're
entrusting the review of your project's translations to its members. Not
only must you be certain that you're comfortable with the people already
involved in the group but you must also be sure that you're happy with
their methods of vetting new recruits.

The advantage of working with an existing translation group is that they
should already have established teams for several languages, as well as
the community processes necessary to ensure efficient review. However,
selecting a translation group is not the same as persuading people to
review translations made for your project!

For project owners
-------------------

Working with an existing translation group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take a look at an example translation group, the default choice
for most new projects: `Launchpad Translators <https://translations.launchpad.net/+groups/launchpad-translators>`__.

By visiting the group's overview page, you can see which:

-  individual or team owns the group
-  individuals and teams are assigned to which languages
-  projects and distributions have delegated their translation review to
   Launchpad Translators.

In most circumstances, the Launchpad Translators group will suit your
needs. You can learn more about Launchpad Translators in the :ref:`help article about the group <launchpad-translators-group>`.

To choose Launchpad Translators, or any other existing translation
group, visit ``https://translations.launchpad.net//+settings``.

Although many projects find that people spontaneously contribute
translations to their projects, you now need to encourage the teams
within your chosen group to review translations in your project.

Creating your own translation group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most projects choose to join an existing translation group because they
already have established teams for one or more languages.

However, if you want to maintain control of which teams or individuals
can review translations in your project, or have specific requirements
for the people who review your project's translations, you can request the
creation of a new translation group. 

`File a support request <https://answers.launchpad.net/rosetta/+addquestion>`__
with the Launchpad administrators.

For translators
---------------

If all you want to do is help translate free software, you don't need to
join a translation group. Translation groups exist to review
translations that have already been made or suggested. However, there
are a couple of things to note:

-  projects with a ``Closed`` translations policy allow only members
   of the translations group to make or suggest translations
-  in practice, many of a project's most active translators join the
   translation group and so both translate and review other people's
   translations.

Joining a translation group
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're confident that you make accurate and useful translations, and
you're familiar with the review requirements of the projects you want to
work with, you have two options:

-  join a team that has responsibility for a language within a
   translation group.
-  if you work in a language for which your chosen translation group has
   no appointed supervisor, you can apply to take that role either as an
   individual or as part of a team.

Choosing a translation group to join
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can see which translation groups are active in Launchpad, and which projects they work with, on the `translation groups page <https://translations.launchpad.net/+groups>`__. Click on any of the groups to see:

-  who owns them
-  which teams and individuals are responsible for which languages.

You should choose the translation group you want to join based on which project(s) you're most interested in working with. For example: if you want to help translate `Avant Window Navigator <https://launchpad.net/awn>`__, you'd join the `Ubuntu Translators <https://translations.launchpad.net/+groups/ubuntu-translators>`__ group.

What you do next depends on whether that group has already appointed a
team or individual for your chosen language:

-  **A team is responsible for your language**: visit the team's
   overview page and contact the team owners about their membership
   requirements.
-  **An individual is responsible for your language**: visit their
   profile page to find out how to contact them and then let them know
   you want to help.
-  **No one looks after that language**: contact the translation group
   owners to let them know you want to help with that language.

Creating a new translation team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to take responsibility for a particular language, within a
translation group, either as an individual or member of a team, contact
the translation group's administrators. You can find their contact
details by following the link to their profile page on the translation
group's home page.

Reviewing translations
~~~~~~~~~~~~~~~~~~~~~~

Once you're involved in a translation group, you're ready to start
reviewing strings. You can see where your review is needed by visiting
either:

-  **for a project**: the translations overview page for that project
   (for example:
   https://translations.launchpad.net/silva/trunk/+pots/silva)
-  **for a distribution**: the distro's overview page for the language
   that you work in (for example:
   https://translations.launchpad.net/ubuntu/gutsy/+lang/en_GB)

On these pages, Launchpad shows you how well advanced the translation
effort is. The part we're interested in, for now, is the "Needs review"
column. As you might expect, this shows you how many strings need to be
reviewed before they enter the official translation for that project or
distribution package.

To start review, simply click one of the numbers in that column!
Launchpad will then show you the original English string, the current
accepted translation (if any) and the suggested translation that
requires your review.

Further information
-------------------

Let :ref:`Launchpad and local translators know about your team guidelines <translation-guidelines>`

Once people start using Launchpad to translate your project, you'll want
to :ref:`export those translations <exporting-translations-from-launchpad>` for
use in your software.

For Lunchpad translators, find out more: :ref:`launchpad-translators-group`.
