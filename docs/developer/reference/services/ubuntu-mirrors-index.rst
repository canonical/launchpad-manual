Ubuntu Mirrors Index
==================== 

Short description
-----------------

The Ubuntu mirrors index service publishes an index of Ubuntu mirror listings 
per country, to help users download packages from nearby up-to-date mirrors. 
The charm is a subordinate to Apache2 in the Launchpad environment, and updates 
mirror data regularly via a cron job.

Detailed description
--------------------    
The Ubuntu mirrors index (referred as ``prod-ubuntu-mirror-index`` in juju) is 
a subordinate charm to Apache2 that generates and serves a mirror index:

- Queries Launchpad database every 6 hours via a cron job.

- Gets the best official mirrors by country, using Launchpad API method ``getBestMirrorsForCountry``:

  - Given a user IP address.

  - If no mirrors are located in the country of the request it falls back to the main Ubuntu repositories.

- The charm logic updates and publishes them in http://mirrors.ubuntu.com/mirrors.txt.


Documentation
-------------
- Mirrors list - http://mirrors.ubuntu.com/mirrors.txt 
- Charmhub ubuntu-mirrors - https://charmhub.io/ubuntu-mirrors	
- Launchpad lib/lp/registry/doc/distribution-mirror.rst - explains how distribution mirrors are created and managed in Launchpad.

Git Repositories
----------------
The source repository for the Ubuntu mirrors charm is located in https://launchpad.net/ubuntu-mirrors	

Production
~~~~~~~~~~
The Ubuntu mirrors index service ``prod-ubuntu-mirror-index`` is deployed in the Launchpad 
production environment as a subordinate charm to an Apache2 unit.
