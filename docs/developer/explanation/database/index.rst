.. meta::
   :description: Overview of database topics including PostgreSQL, live 
      patching, Storm migration, and database performance optimization.

.. _database-overview:

Database
=========

Launchpad uses PostgreSQL, making use of stored procedures, triggers,
functional indexes, and other PostgreSQL-specific features. It uses `Storm <https://storm-orm.readthedocs.io/en/latest/>`_
as its object-relational mapper (ORM).

.. toctree::
   :maxdepth: 1
   
   database-performance
   live-patching
   postgresql
   storm-migration-guide
   working-with-db-devel