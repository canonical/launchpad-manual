PO Templates
============

.. include:: /includes/important_not_revised_help.rst

Some people may be confused by the term PO *Template* ''' because in
traditional Gettext environments, they have only worked with '''PO
*Files* '''. Here is a short explanation of the term.

In Gettext
----------

If you never encountered PO templates before, you have either only been
working with existing PO files (i.e. improving existing translations) or
have been creating new PO files using xgettext (or some other tool). For
example, to start new Esperanto translations, you may have run a command
like this in your po directory:

::

   $ xgettext -o eo.po -D ../src

Then you started translating by filling out *eo.po*. Actually, this is
where you just created a PO template file but you did not save it. The
correct approach is to have the template generated once during build and
start new translations by copying the template file. The gettext package
provides the *msginit* utility to do the copying and adjust header
information in the newly created PO file.

::

   $ xgettext -o mydomain.pot -D ../src
   $ msginit --locale=eo

So, a *PO template* is no more than a generic *PO file* without any
translations filled out and generic header information. Using xgettext
and msginit to create a template and PO files is also described in the
`Gettext
manual <http://www.gnu.org/software/gettext/manual/gettext.html>`__,
sections 5 and 6.

In Launchpad
------------

In Launchpad you make translating your project possible by `importing a
PO template file </../YourProject/ImportingTemplates>`__. After the
import, all the English strings from the template are available in
Launchpad for being translated. When a translator starts translating
your project into their language, for which there were no translations
before, a new (virtual) PO file is created in the Launchpad database. It
becomes a real PO file when you chose to download it.

Please make sure to keep the PO template in Launchpad current by importing 
updated versions of the file you create from your source code.