
launchpadlib API compatibility
==============================

The API compatibility of the launchpadlib Python library has not always
been maintained as well as an author of a program using it would hope.

&gt;= 1.5.5 (&gt;= Ubuntu Lucid Lynx)
-------------------------------------

Version 1.5.5 added the support for accessing various different versions
of the remote web-service API (at the time of writing, these versions are
known as "beta", "1.0" and "devel"). Whilst the new version parameters were
compatibly added, there was an incompatible change to the URLs that launchpadlib
would accept as service_root parameters:


* launchpadlib 1.5.4 and earlier **requires** URLs of the form https://api.launchpad.net/beta/  
* launchpadlib 1.5.5 and later **requires** URLs of the form https://api.launchpad.net/

and either will break in non-obvious ways if you give it the wrong form.

1.8.0 (no Ubuntu release)
-------------------------

Version 1.8.0 changed things, which 1.9.0 then changed again.
And, it never went into any final Ubuntu release. Probably best to just pretend it doesn't exist.

&gt;= 1.9.0 (&gt;= Ubuntu Natty Narwhal)
----------------------------------------

Version 1.9.x's changes versus 1.6.x include a major refactor of how
authentication tokens are obtained. Notable consequences:


* Different kinds of tokens are obtained, and they are stored differently by default
(in GNOME keyring or similar technologies instead of files), meaning it's highly
unlikely that tokens stored by launchpadlib 1.6.x will be noticed by 1.9.x,
so users will have to re-authorize.  
* Most of the methods by which a Launchpad object is obtained have changed
significantly:

.. note::
    Positional parameter indices referred to below are 1-based.

``Launchpad.init``
~~~~~~~~~~~~~~~~~


* Parameters authorization_engine and credential_store inserted at position 2.

.. caution::
    It is no longer safe to call Launchpad.__init__ with positional parameters beyond
    the first in compatible applications!

``Launchpad.login``
~~~~~~~~~~~~~~~~~~~

* Method is now deprecated.  
* Five new parameters inserted at position 8. Mitigating factor: the only parameter
  after this was version, which was probably being passed as a keyword argument anyway.

``Launchpad.get_token_and_login``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Method is now deprecated.  
* Parameter 6 renamed from authorizer_class to authorization_engine.  
* Parameters credential_store and credential_save_failed inserted at position 9.
  Mitigating factor: the only parameter after this was version, which was probably
  being passed as a keyword argument anyway.

``Launchpad.login_with``
~~~~~~~~~~~~~~~~~~~~~~~~

* Positional parameter 1 changed from consumer_name to application_name to attempt to
  force common use-cases to acquire a desktop integration rather than consumer-specific token without code changes.  
* Parameter 6 renamed from authorizer_class to authorization_engine.  
* New parameter consumer_name appended to replace the incarnation removed at position 1.
  (But it does not actually work - see `https://launchpad.net/bugs/755313 <https://launchpad.net/bugs/755313>`_\ )  
* New parameters credential_save_failed and credential_store appended.