.. _log-into-websites-with-openid:

Log into websites with OpenID
=============================

.. include:: /includes/important_not_revised_help.rst


`OpenID <http://openid.net>`_ is a way to log into many websites using just one username and password. However, rather than entering that username and password at each website, you use a website you trust, such as `Launchpad <https://launchpad.net>`_ to confirm your identity to the other sites.

Here's how it works:


#. You visit a website that supports OpenID and it asks you to log in.
#. Enter the Launchpad profile URL - ``https://launchpad.net/~your-nickname``
#. If you're not already logged into Launchpad, it'll ask you to enter your username and password.
#. Once you're successfully logged into Launchpad, it'll return you to the site you want to visit.

This means that you only need to remember your Launchpad profile URL, username and password in order to log into websites that support OpenID.

We will send your Launchpad nickname to the site but some websites may choose to refer to you by your Launchpad profile URL - e.g. ``https://launchpad.net/~your-nickname``.

Launchpad supports both `OpenID 2.0 <http://openid.net/specs/openid-authentication-2_0.html>`_ and `1.1 <https://openid.net/specs/openid-authentication-1_1.html>`_.

`Learn more about OpenID <https://openid.net/foundation/>`_.

Where can I use it?
-------------------

You can use Launchpad to log into any of the growing number of sites that support OpenID. These include:

* `LiveJournal <http://livejournal.com>`_.

Find out more about `where you can use OpenID <http://en.wikipedia.org/wiki/OpenID#Adoption>`_.

FAQs
----

**Where can I see a list of bugs filed against Launchpad's OpenID implementation?**

All of our `OpenID bugs are tagged <https://bugs.launchpad.net/launchpad-project/+bugs?field.tag=openid>`_ with the openid tag.

**Can I log into Launchpad with my existing OpenID?**

Not at this time. Launchpad is currently an OpenID Provider (OP) and not a consumer (RP).

**I Can I link my existing OpenID to my Launchpad OpenID?**

There is no way today to associate your other OpenIDs with your Launchpad OpenID.

**Can I change my OpenID id?**

Yes. You can `change your Launchpad id <https://launchpad.net/people/+me/+edit>`_ and that will change your identity URL. That could mean that sites you've already logged into using your previous OpenID URL may consider you a new user.

**Do you support immediate mode authentication requests?**

Currently we do not support immediate mode properly since we do not support pre-authorising an RP to avoid the login page. We have some infrastructure to support pre-authorisation, but decided to leave it out because it complicated the UI.
