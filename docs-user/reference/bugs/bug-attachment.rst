Bug Attachment
==============

A bug attachment has two purposes:

- It may contain data that is useful to describe a bug, like a screenshot or data needed to reproduce the bug.
- It may contain a patch, i.e., something that fixes the bug.

A patch shows in most cases the changes that should be applied to the
code and looks usually like so:

::

       --- lib/lp/bugs/browser/bugattachment.py        2009-11-26 10:35:21 +0000
       +++ lib/lp/bugs/browser/bugattachment.py        2010-01-11 13:19:15 +0000
       @@ -14,6 +14,7 @@

        from zope.interface import implements
        from zope.component import getUtility
       +from zope.contenttype import guess_content_type

But a patch may also consist of a changed graphics or sound file which
improves, for example, the user interface of a program.

Launchpad has a very simple mechanism to detect the content of an
attachment. When you upload an attachment or when you change the "patch"
flag of an existing attachment, Launchpad checks if the file looks like
a patch and if you set the "patch" flag accordingly.

If the flag is not set as Launchpad expects, you are redirected to the
attachment edit page, where you can override Launchpad's assumption that
the file is (not) a patch.
