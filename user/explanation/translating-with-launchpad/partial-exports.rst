Exporting partial gettext PO files
==================================

Distributions, such as Ubuntu, use Launchpad to translate the free
software packages that make up the operating system. Where an upstream
project has an existing translation effort, the distribution's
translators can import the upstream PO files into Launchpad and either
customise those translations to the distro's needs or even correct
translation errors.

To make it easier for upstream projects to take advantage of this
translation work, Launchpad can generate a partial PO file that contains
only the translations that differ from the last imported upstream
translation files.

Requesting a partial export
---------------------------

When you are on the web page for the PO file in question, select
"Download" from the grey menu bar. You will be presented with the option
to choose the file format for the download - either ``PO format``, or ``MO
format``, or ``Changes from packaged translations in partial PO format``.
Choose the latter option for a partial export.

How partial PO files differ from full PO files
----------------------------------------------

While a standard PO file has a full gettext header, and so can be edited
offline and then re-imported into Launchpad, the partial PO files that
Launchpad provides do not have a header.

.. note::
    Partial PO files cannot be re-imported into Launchpad because
    their lack of a header makes them fail the import validation. Please use
    these files only to merge the translation strings into existing full PO
    files. Those merged PO files can then, of course, be imported into

What can upstreams do with partial PO files
-------------------------------------------

Partial PO files are useful for reviewing or merging into existing
(upstream) PO files. Review can be as simple as going through all the
messages and removing those you don't want to accept.

For merging, a further step is required: one has to add a content type
declaration to partial PO files before using them with ``msgcat`` or
``msgmerge``.

To do this, insert the following block at the start (right after the
comment) of a partial PO export:

::

   msgid ""
   msgstr "Content-type: text/plain; charset=UTF-8\n"

After adding this bit to the exported partial PO file you got from
Launchpad, you can merge this with the upstream PO file using:

::

   msgmerge -o merged.launchpad.sr.po partial-export.sr.po upstream.sr.po 

where ``partial-export.sr.po`` is a Launchpad-exported file with the
content-type definition added, ``upstream.sr.po`` is the translation file
from the upstream repository, and ``merged.launchpad.sr.po`` is a resulting
merged file where translations from ``partial-export.sr.po `` override
translations from ``upstream.sr.po``.

If you want to give preference to upstream translations when merging,
you can run something along the lines of

::

   msgcat -o merged.upstream.sr.po --use-first upstream.sr.po partial-export.sr.po

To learn more about GNU gettext tools, look through the `documentation
for
gettext <http://www.gnu.org/software/gettext/manual/gettext.html>`__