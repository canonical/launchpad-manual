Launchpad Database Setup
========================

.. include:: ../includes/important_not_revised.rst

There are two ways to set up your launchpad database.

Automated Launchpad Database Setup
----------------------------------

To set up PostgreSQL for running Launchpad, try using
``utilities/launchpad-database-setup`` from the Launchpad source
tree.

.. caution::

    Do not use this script if you are using PostgreSQL for anything
    besides Launchpad. The script expects a freshly installed postgresql
    database, so it will **destroy** any PostgreSQL databases you already
    have on your system. If that is a problem for you, use the manual
    procedure instead and adapt to your needs.

Manual Launchpad Database Setup
-------------------------------

The initial Launchpad database should be done on your system with the
following sequence of commands:

1. **If you have any versions of PostgreSQL other than 10 on your
   system:** Launchpad requires PostgreSQL 10 on port 5432. Ensure that
   any existing PostgreSQL clusters are not running on port 5432.

:literal:` Edit `/etc/postgresql/$OTHER_VERSION/*/postgresql.conf` and change the `port=` settings to 5433, 5434, 5435 etc.`

| `` For example, if you have postgresql 9.1 installed and nothing fancy (only one cluster) edit /etc/postgresql/9.1/main/postgresql.conf:``
| `` ``

::

   port = 5432

| `` and replace that by``
| `` ``

::

   port = 5433

:literal:` You may also want to edit `/etc/postgresql/$OTHER_VERSION/*/start.conf to select which instances are run on startup, or even uninstall the earlier PostgreSQL versions.`

2. Install packages (Done by rocketfuel-setup, if you used that.):

.. raw:: html

   <!-- end list -->

::

   sudo apt-get install launchpad-database-dependencies

| ``   which is equivalent to:``
| ``   ``

::

   sudo aptitude install postgresql-10 postgresql-plpython-10 postgresql-client-10 postgresql-10-slony1-2 postgresql-10-debversion

3. Nuke the default database and recreate with the current required
   locale:

::

   $ sudo pg_dropcluster 10 main --stop-server

   $ LC_ALL=C sudo pg_createcluster 10 main --start --encoding UNICODE

4. Add the following lines **at the top** of the file
   /etc/postgresql/10/main/pg_hba.conf:

::

   # allow unauthenticated connections to localhost
   local   all         all                               trust
   host    all         all         127.0.0.1/32          trust
   host    all         all         ::1/128               trust

``   Note that this gives all accounts on your local box full access to PostgreSQL - if this is a problem talk to Stuart Bishop for more detailed instructions (this requires occasional maintenance).``

5. Add the following options to /etc/postgresql/10/main/postgresql.conf:

::

   # Per Bug #90809, standard_conforming_strings should be 'on'
   standard_conforming_strings=off
   escape_string_warning=off

   #enable_seqscan=false
   log_statement='none'
   log_line_prefix='[%t] %q%u@%d '
   fsync = off

:literal:`   The first two are required. `enable_seqscan` helps tune queries as it forces PostgreSQL to use indexes if they are available (PostgreSQL often won't use them with our sample data because it is more efficient to simply scan the entire table), but will cause things to run a bit slower. The `log_*` statements output all queries sent to the server to `/var/log/postgresql/postgresql-10-main.log`, which helps you debug and understand what your code (and in particular Storm) is doing. The `fsync = off` line improves performance at the slightly increased risk of database integrity loss, by disabling fsyncs from PostgreSQL. This change makes certain development tasks more efficient, for example, the amount of time required to create a new database can be dramatically reduced. In exchange, if your computer crashes, you would need to recreate the whole PostgreSQL cluster.`

6. Restart the PostgreSQL server:

::

   sudo service postgresql restart

7. Make sure your default PostgreSQL user is a superuser. Your default
   PostgreSQL user has the same name as your login account (if it
   existed already, and it was not a superuser, drop it first):

::

   sudo -u postgres dropuser $(id -un)
   sudo -u postgres createuser -s -d $(id -un)

8. Create the databases, users, permissions and populate it with
   sampledata:

::

   cd $your_launchpad_checkout; make schema

9. Profit! Enjoy your shiny new launchpad database.
