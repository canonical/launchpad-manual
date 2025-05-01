========================
PostgreSQL and Launchpad
========================

Why PostgreSQL?
===============

PostgreSQL was chosen in 2004 because it supported most of the features we
thought we would need; MySQL did not.  The other contender was Oracle, and
for a while we made sure we would be able to switch to Oracle if necessary
but PostgreSQL has worked great.

How integrated is the database in the code?
===========================================

Highly. We make use of PostgreSQL specific features, such as:

* SQL language extensions
* PL/pgSQL and Python stored procedures
* Triggers
* Functional indexes
* Automatic load balancing over the replicas with Slony-I
* Transactional DDL
* tsearch2 full text search
* Database permissions
