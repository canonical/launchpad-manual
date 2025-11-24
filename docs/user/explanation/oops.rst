What is an OOPS?
================

.. include:: /includes/important_not_revised_help.rst

When Launchpad suffers an error that prevents it doing what you
requested, it will log the error and some diagnostic detail, so that a
developer or system administrator can figure out what has happened and
we can fix it.


What does an OOPS look like?
----------------------------

In the web UI, it will look something like the image below.


The red highlight is around the OOPS ID -- that is the code that lets us
look up the error and see what went wrong.

In response to a command email, it will be a plain text message with an
OOPS id.

In the LP API, it is a 500 response code and the OOPS code will be in
the body.

What do we do with OOPS reports?
--------------------------------

All OOPSes are aggregated and published as a summary to the developer
list daily. We create bugs to match the OOPSes that have been occurring
and treat all OOPS bugs as high priority. That queue is pretty full
though, so please talk to use when you are experiencing a problem -
there may be a workaround that can help you achieve get what you are
trying to do.

Why do they happen?
-------------------

There are multiple causes for an OOPS. Broadly they fall into three
camps.

Firstly, and the most commonly encountered cause, if a Launchpad web
request is going to take a long time to complete, the server aborts the
request to free up resources and hopefully unlock and unblock other
requests. This is the 'timeout' OOPS.

Secondly, we generate an OOPS when an internal link within Launchpad is
broken.

Lastly, a code bug that causes an unhandled exception will show up as an
OOPS.

What to do if you encounter an OOPS
-----------------------------------

Come and :ref:`chat with us <get-help>`. We'll try and help you achieve 
what you are trying to do. We may ask for the OOPS ID - see above under 
`what does an OOPS look like? <#looklike>`__.

We like to make sure there is a bug report for every OOPS - if you want
you can look at the `known OOPS
bugs <https://bugs.launchpad.net/launchpad-project/+bugs?field.tag=timeout,oops>`__
we have.