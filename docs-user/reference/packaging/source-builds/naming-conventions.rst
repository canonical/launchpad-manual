Naming conventions for daily builds
====================================

It would be nice if we had a nice agreeable way to name daily builds so
we don't confuse users. Here are some recommendations. These are still
draft, so please leave a comment.

Recommendations
---------------

1. Create a team for the project if one doesn't exist already.

- This will ensure that the PPA has the project's name in it and that people can rotate in and out to run the PPA if you move on.
- Many projects in Launchpad have pages that are sitting there owned by Registry (which means no one is looking after it), this could be an excellent opportunity to take over that page and give it some love and have the team own that page.
- If the project you are interested in already has a team but no daily then ask them to register one, or maybe you can join the team and help them out!

2. Create the daily PPA and name it ``daily``, and set the team as the
   owner.

- A bunch of projects already use "ppa" as their main ppa, so by making it ``daily`` this will be distinguishable from the normal PPA.
- This will mean that daily PPAs will end up being ppa:projectname/daily.

Other Tips
----------

-  Use the term ``daily``, not dailies, nightlies, nightly, etc. that way
   we can keep it consistent throughout the project.
-  Avoid using your personal PPA space for "production" daily builds; as
   users start to use these and they become popular we should encourage
   the use of ppa:projectname/daily instead of
   ppa:~billybobthorton/loltesting. This will also allow us to keep the
   maintenance of them team oriented in case the person who sets them up
   gets bored and moves on.