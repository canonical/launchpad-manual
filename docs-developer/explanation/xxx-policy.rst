XXX policy
==========

.. include:: ../includes/important_not_revised.rst

Policy Statement
----------------

1. We put "XXX" in our code in a specific format to denote areas
   requiring follow up.

   * Python

     .. code:: python

        # XXX: SteveAlexander YYYY-MM-DD bug=NNNN: Comment here.

   * TAL

     .. code:: xml

        <tal:XXX condition="nothing">YYYYMMDD mpt: Comment here.</tal:XXX>


     The XXX cannot be followed by a colon here, because that would be
     an XML error. And if the XXX was put inside the element instead,
     that would make the code longer and XXXes a bit harder to find.
     (See also `bug 120005 <http://launchpad.net/bugs/120005>`__, "Page
     template comment syntax is too verbose".)

   *  Consider filing a bug or spec for an XXX.
   *  Our current tools use the following regex (XXX:?|TODO|FIXME) which
      means XXX will be found even if it does not have a colon.
   *  TODO comments are permitted in the same format.
   *  FIXME items should be listed as XXX.


2. Reviewers will not approve code that does not follow this format.
3. Developers when modifying code which contains an XXX block should
   strive to resolve the XXX if possible.

Rationale
---------

The use of this standardized format allows us to write scripts which scan our
code for these areas and generate reports. This enables us to identify areas of
our code which may need further attention.

Principles
----------

-  Each XXX is an indicator of tech debt (not the debt itself)
-  We must strive to eliminate tech debt
-  Marking existing code that ought to be cleaned with an XXX is good
-  Actually cleaning up code is best

Scope
-----

-  Affects: All Launchpad Code
-  Term: Permanent
