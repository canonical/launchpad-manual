.. meta::
   :description: Install software from a private PPA.

Install software from private PPAs
==================================

There are two types of Personal Package Archive: public PPAs and private
PPAs. Private PPAs are great for people who want to control who can
install their software.

To access a Private PPA, you'll need to contact its owner and ask for a
subscription. It's up to the Private PPA's owner how they decide to
grant access.

:ref:`Contact us <get-help>` to find out how to get your own Private PPA.

Activate your subscription
--------------------------

Subscribing to a private PPA is a two-step process:

1. The Private PPA's owner offers you a subscription in Launchpad.
2. You either accept or reject the subscription.

You can see whether you have any outstanding subscription offers on your
`archive
subscriptions <https://launchpad.net/people/+me/+archivesubscriptions>`__
page.

Once you've accepted the offer, Launchpad will generate a unique
password that gives you access to the archive.

Add the private PPA to Ubuntu
------------------------------

Ubuntu uses the Debian system of software archives, also called
repositories. Private PPAs are like any other Debian-style software
archive, except that each subscriber has their own unique password.

* Check your subscriptions in the `archive subscriptions
  <https://launchpad.net/people/+me/+archivesubscriptions>`__
  page and get the name of the archive you want to add. It should be
  something like ``ppa:user/ppa-name``.
* Then, run the ``add-apt-repository``
  using the ``--login`` flag and update the package list.

::

   sudo add-apt-repository --login ppa:user/ppa-name
   sudo apt update
