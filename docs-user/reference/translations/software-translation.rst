Translating your software
=========================

Launchpad has unique infrastructure to support the translation of free
software into many languages. It enables translation communities to form
and organise themselves, leveraging the `Team
Management <ReviewersGuide/TeamManagement>`__ capabilities described
earlier, and allows you to keep track of the translations of multiple
versions of your software into multiple languages.

This translation infrastructure is all web-based, so new translators can
join very easily, without any special tools or needing to commit to the
project's codebase. However, Rosetta imports and exports standard
translation files, enabling more advanced translators to use their
preferred tools and avoid the web interface entirely.

Ubuntu uses Launchpad to manage the translation of several hundred
packages into many different languages, for each successive release. In
particular, once a release has been made, Ubuntu translators can
continue to improve translations, which are delivered to users in the
form of updated language packs every few weeks.

Keeping track of progress
-------------------------

When software is ready to be translated, it results in one or more
"translation templates". You can see the extent to which a particular
template has been translated very easily. For example, here is the
status of the Gnome Terminal translation in Ubuntu's 6.06 LTS release:

    https://translations.launchpad.net/ubuntu/dapper/+source/gnome-terminal/+pots/gnome-terminal

And part of that page, at the time of writing looked like this:

You can immediately tell which languages are well-translated (green) and
which are not. The purple bars represent new translations, added to this
system since the package itself was built. It's also possible to see
when someone last added to the translation of this template in any
particular language, and who that person was.

Contributing translations
-------------------------

It's very easy for people to contribute new translations. Each
translation is presented as a web form, with the English and current
translation as well as suggestions based on other known translations
prominently displayed. Here's an example of the form to translate a
single message in an application (Gnome Terminal again):

Notice that the translator has included the relevant HTML display
markup. The translation is substituted in the interface for the English
string in its entirety. Some more sophisticated translations can contain
multiple lines of text, and placeholders for values that come from the
application itself. And of course, translations sometimes need to deal
with plurals - the difference between "there are 9 cars on the lot" and
"there is 1 car on the lot".

It takes time and skill to become a very good translator. For this
reason, it is possible to have a core group of trusted translators who
can modify any translation. Everyone else is limited to making
suggestions, until they are trusted enough to be part of the core team.

Separating translations for different versions
----------------------------------------------

Often, you may want translators to be able to work on a stable version
of the project code, and at the same time get a head start on the
development version. Launchpad supports this explicitly. Each Series (we
described those earlier - major versions of a project, such as 1.1.x,
1.2.x and trunk) can have its own set of translation files. When a
translation is added to a Series, it is immediately suggested to the
other if the original English string is unchanged.

This mean that some translators can focus on expanding the translation
coverage of your stable release, while others work on the cutting edge.

For example, here you can see the work being done to translate
Wengo``Phone. By default, the "trunk" is shown because the Wengo``Phone
developers have identified that as the most important series to be
translated, at the time of writing. But it is also possible to translate
Wengo``Phone 2.1:

 https://translations.launchpad.net/wengophone/

And here's a snapshot of the relevant part of the page, at the time of
writing:

Translation groups
------------------

Perhaps most importantly, Launchpad makes it easy to organise your
translation community. Here is a list of the translators and translation
teams that work on Ubuntu. Of course, other people can contribute
translations, but these are the formal teams who have the most direct
access.

    https://launchpad.net/translations/groups/ubuntu-translators

At the time of translation, the list started with these teams:

Note that each "translator" in this case is a team. They can also be
individuals, but in our experience it is useful to create teams as soon
as you have more than one person who is judged competent to help with a
particular language.

One lesson that we learned the hard way is that it is better to set high
standards for team membership than to invite too many people into the
team before they have proven their experience and competence. Not only
is it a question of speaking the language fluently, but it's also
important to know the conventions of that application, and the details
of such things as plural forms and data substitutions. To deal with
these issues, we have implemented review systems that allow you to
invite people to contribute translations, which are then held for review
by the official translation team. This way you can mentor translators to
improve, and ultimately accept them into the editorial community with
permission to change any translation.

Levels of permission
--------------------

You can determine the restrictiveness of your translation policy. There
are three options:

-  **Completely open:** anybody can fix any translation in any language.
-  **Partly restricted:** for languages where a specific translator has
   been appointed, only they can made translations. For other languages,
   anyone can make a translation.
-  **Restricted:** appointed translators can work on their specific
   language. For languages where a translator hasn't been appointed,
   anyone can suggest translations and they will be queued for review
   until a translator is appointed for that language.

In summary, Launchpad can be a useful tool to organise the people in
your community who are willing to help make your software accessible to
people in their own native language. You do still need to mentor people
to ensure the quality of the translations, but Launchpad greatly reduces
the barriers to participation and gives you a framework to build a
strong translation effort.

The next step on our tour looks at Launchpad's `feature planning and
release management <FeatureHighlights/BlueprintReleasePlanning>`__
capabilities.