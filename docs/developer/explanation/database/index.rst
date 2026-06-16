.. meta::
   :description: Overview of database topics including PostgreSQL, live 
      patching, Storm migration, and database performance optimization.

.. _database-overview:

Database
=========

Launchpad is deeply integrated with PostgreSQL, making deliberate use of
stored procedures, triggers, functional indexes, and full-text search —
features that go well beyond what a generic ORM layer would expose.

.. toctree::
   :maxdepth: 1
   
   database-performance
   live-patching
   postgresql
   storm-migration-guide
   working-with-db-devel