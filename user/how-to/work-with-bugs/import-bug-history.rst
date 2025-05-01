Import your project's bug history
=================================

You can move your project's bug history to Launchpad by converting the
history into Launchpad's import format.

To request an import you need to:

-  generate an import file using one of our exporters (or create one),
   such as `XML Sourceforge bugs to
   Launchpad <https://launchpad.net/sfbugs2launchpad>`__ or `JSON
   Sourceforge bugs to Launchpad <https://github.com/kevincox/nsf2lp>`__
-  validate it as described later in this page
-  Ask for a staging import to be done by opening a ticket in the lp
   answer tracker https://answers.launchpad.net/launchpad. One of our
   system administrators will check that it validates and import it to
   staging where you can check its all as you wanted.
-  Finally ask for a production import to be done (by opening another
   ticket).

In the future we may offer an LP API for self-service of the import
step.

Requirements
------------

Before we can import bugs into Launchpad, your export file must
validate. Please validate the file against the export format spec in the
Launchpad tree before requesting an import.

To do this:

1. Download
   `bug-export.rnc <https://git.launchpad.net/launchpad/tree/doc/bug-export.rnc>`__
2. Install ``jing``
3. Run:

.. terminal::
    jing -c bug-export.rnc your-export-file.xml

``jing`` must not report any errors before we can attempt an import of
your bugs into Launchpad. Consult the format spec below to understand
any errors that ``jing`` reports.

1. 

   1. Really? We don't change this format ever, as far as I can tell.
      --deryck
.. note::
    this format is a draft and may change. Subscribe tothis page if you
    want to receive an email when we make updates.

The format
----------

::

   default namespace = "https://launchpad.net/xmlns/2006/bugs"

   start = lpbugs

   # Data types

   boolean = "True" | "False"
   lpname = xsd:string { pattern = "[a-z0-9][a-z0-9\+\.\-]*" }
   cvename = xsd:string { pattern = "(19|20)[0-9][0-9]-[0-9][0-9][0-9][0-9]" }
   non_empty_text = xsd:string { minLength = "1" }

   # XXX: jamesh 2006-04-11 bug=105401:
   # These status and importance values need to be kept in sync with the
   # rest of Launchpad.  However, there are not yet any tests for this.
   #     https://bugs.launchpad.net/bugs/105401
   status = (
     "NEW"          |
     "INCOMPLETE"   |
     "INVALID"      |
     "WONTFIX"      |
     "CONFIRMED"    |
     "TRIAGED"      |
     "INPROGRESS"   |
     "FIXCOMMITTED" |
     "FIXRELEASED")
   importance = (
     "CRITICAL"  |
     "HIGH"      |
     "MEDIUM"    |
     "LOW"       |
     "WISHLIST"  |
     "UNDECIDED")

   # Content model for a person element.  The element content is the
   # person's name.  For successful bug import, an email address must be
   # provided.
   person_nobody = (
     attribute name { string "nobody" })
   person_normal = (
     attribute name { lpname }?,
     attribute email { non_empty_text },
     text)
   person = (
     person_nobody |
     person_normal)

   lpbugs = element launchpad-bugs { bug* }

   bug = element bug {
     attribute id { xsd:integer } &
     element private { boolean }? &
     element security_related { boolean }? &
     element duplicateof { xsd:integer }? &
     element datecreated { xsd:dateTime } &
     element nickname { lpname }? &
     # The following will likely be renamed summary in a future version.
     element title { text } &
     element description { text } &
     element reporter { person } &
     element status { status } &
     element importance { importance } &
     element milestone { lpname }? &
     element assignee { person }? &
     element urls {
       element url { attribute href { xsd:anyURI }, text }*
     }? &
     element cves {
       element cve { cvename }*
     }? &
     element tags {
       element tag { lpname }*
     }? &
     element bugwatches {
       element bugwatch { attribute href { xsd:anyURI } }*
     }? &
     element subscriptions {
       element subscriber { person }*
     }? &
     comment+
   }

   # A bug has one or more comments.  The first comment duplicates the
   # reporter, datecreated, title, description of the bug.
   comment = element comment {
     element sender { person } &
     element date { xsd:dateTime } &
     element title { text }? &
     element text { text } &
     attachment*
   }

   # A bug attachment.  Attachments are associated with a bug comment.
   attachment = element attachment {
     attribute href { xsd:anyURI }? &
     element type { "PATCH" | "UNSPECIFIED" }? &
     element filename { non_empty_text }? &
     # The following will likely be renamed summary in a future version.
     element title { text }? &
     element mimetype { text }? &
     element contents { xsd:base64Binary { minLength = "1" } }
   }

An example
----------

::

   <?xml version="1.0"?>
   <launchpad-bugs xmlns="https://launchpad.net/xmlns/2006/bugs">
   <bug xmlns="https://launchpad.net/xmlns/2006/bugs" id="45">
     <private>True</private>
     <security_related>True</security_related>
     <datecreated>2004-10-12T12:00:00Z</datecreated>
     <nickname>some-bug</nickname>
     <title>A test bug</title>

     <description>A modified bug description</description>
     <reporter name="foo" email="foo@example.com">Foo User</reporter>
     <status>CONFIRMED</status>
     <importance>HIGH</importance>
     <milestone>future</milestone>
     <assignee email="bar@example.com">Bar User</assignee>

     <cves>
       <cve>2005-2736</cve>
       <cve>2005-2737</cve>
     </cves>
     <tags>
       <tag>foo</tag>
       <tag>bar</tag>

     </tags>
     <bugwatches>
       <bugwatch href="http://bugzilla.example.com/show_bug.cgi?id=42" />
       <!-- The following tracker has not been registered -->
       <bugwatch href="http://bugzilla.example.com/show_bug.cgi?id=43" />
     </bugwatches>
     <subscriptions>
       <subscriber email="test@canonical.com">Sample Person</subscriber>

       <subscriber name="nobody">Nobody (will not get imported)</subscriber>
     </subscriptions>
     <comment>
       <sender name="foo" email="foo@example.com">Foo User</sender>
       <date>2004-10-12T12:00:00Z</date>
       <title>A test bug</title>
       <text>Original description</text>

       <attachment>
         <type>UNSPECIFIED</type>
         <filename>hello.txt</filename>
         <title>Hello</title>
         <mimetype>text/plain</mimetype>
         <contents>SGVsbG8gd29ybGQ=</contents>

       </attachment>
     </comment>
     <comment>
       <!-- anonymous comment -->
       <sender name="nobody"/>
       <date>2005-01-01T11:00:00Z</date>
       <text>A comment from an anonymous user</text>
     </comment>

     <comment>
       <sender email="other@example.com">Some other bloke</sender>
       <date>2005-01-01T13:00:00Z</date>
       <text>
   A comment from mark about CVE-2005-2730

   * list item 1
   * list item 2

   Another paragraph

       </text>
       <attachment>
         <mimetype>application/octet-stream;key=value</mimetype>

         <contents>PGh0bWw+</contents>
       </attachment>
       <attachment>
         <type>PATCH</type>
         <filename>foo.patch</filename>
         <mimetype>text/html</mimetype>
         <contents>QSBwYXRjaA==</contents>

       </attachment>
     </comment>
   </bug></launchpad-bugs>