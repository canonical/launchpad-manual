Using Rosetta
=============

Rosetta is an easy-to-use web interface allowing translation of many
software projects.

Concepts
--------

FIXME: describe templates, products, distros,...

Web Experience
--------------

Rosetta is designed to be easy to use and accessible to everyone. You
don't need to learn anything you don't already know: you update
translations by browsing through web pages listing available programs
and distributions, and go straight to updating translations using your
web browser.

This means Rosetta runs from any operating system, and you don't need to
install anything on your existing system.

FIXME: describe how translation works (with lots of screenshots)

Fast Updates
------------

At the same time, Rosetta is a live system, and as soon as you submit
your translations, they are available to all. To other Rosetta users to
be used in other translations as suggestions, to package maintainers to
incorporate into new releases of their software, to distributors to be
included in their language pack updates.

And what's else, Ubuntu is actually creating and distributing language
packs directly from Rosetta for entire core set of software, which means
that your updates get quickly to real world users of Ubuntu.

At the same time, even if upstream doesn't provide updated translations,
you can work independently on them and make your language support better
even if upstream packages never see another release.

Translating Together
--------------------

Rosetta is used by thousands of users worldwide. That means that using
Rosetta for translations will bring you the benefits of many different
people collaborating on the same goal of improving translations for your
language and product.

This is most obvious in the way translation suggestions work. Whenever
someone submits a translation, it also becomes a suggestion to all the
other translators for the same string in all the other programs across
Rosetta.

When you are not sure about a specific translation, and want to get
input from others, you're encouraged to mark your translation as the one
needing review: as soon as someone goes over it, they'll either accept
it as is, or fix it and enable it.

Status Overview
---------------

Whether you are a translator interested only in a subset of languages,
or a developer interested in what languages are supported in your
product, Rosetta gives you clearly formatted status overviews listing
all translations and measure of their completeness.

Status is displayed whenever a pointer to a language or translation is
given, which makes it very obvious as to what you can work on.

If you look closely at the status graphs, you'll notice that there are
four types of colour indications:

-  green is for translations coming from "upstream", i.e. i.e. already provided along with the product when it was added to Rosetta
- blue is for those translations coming from upstream which were
  modified in Rosetta (eg. typos being fixed, rewordings, etc.)
- purple is for new translations originally submitted through
  Rosetta: yes, that means your translations!
- red indicates all the text messages which are untranslated or in
  need of review: these are the ones you can work on in Rosetta!

Import and export
-----------------

For experienced translators, there is an option of exporting a PO file,
translating that using any of the offline editors, and submitting it
back (importing).

This is also useful if you want to test a translation on your local
system, when you can export either a PO or MO file, install it on your
system and see how it all looks in the application.

At the same time, Rosetta provides translations for Ubuntu language
packs, and automatically imports any translations and templates from
newly uploaded Ubuntu packages.

Organizing Projects
-------------------

Maintainers of a software project can decide to make Rosetta their
preferred translation system, when they'll be able to make most from
Rosetta: organize translation teams and their privileges, make use of
huge database of Rosetta translations, and take advantage of many
translators already familiar with Rosetta.

For most projects, startin translation for new version is as simple as
uploading a new template file for translation: all the translations will
be automatically synced

Organizing Teams
----------------

Translating teams are groups of people working together on a single
language translation. When you create a team, you'll probably add a few
translators you trust. They'll be able to contribute translations and
make suggestions.

Rosetta users who are not part of your team will only be able to send
suggestions, so it's not needed to add untrusted translators to your
team.

And when a member gains enough trust, you might want to appoint him an
administrator: helping you moderate the team and put some direction in
your translation effort.