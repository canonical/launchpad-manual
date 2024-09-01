========================= 
Renaming a database table
=========================

Renaming a table involves a few steps:

1. Rename the table
2. Rename dependent objects, like constraints, indexes and sequences.
3. Create a writable view using the old name so deployed code keeps working.

For example::

| ``   -- Copyright 2011 Canonical Ltd.  This software is licensed under the``
| ``   -- GNU Affero General Public License version 3 (see the file LICENSE).``
| ``   SET client_min_messages=ERROR;``

| ``   -- Rename the table``
| ``   ALTER TABLE IrcId RENAME TO IrcNickname;``

| ``   -- And rename sequences, constraints and indexes to match.``
| ``   ALTER SEQUENCE ircid_id_seq RENAME TO ircnickname_id_seq;``
| ``   ALTER TABLE IrcNickname``
| ``   --    With slony 1.2.22, renaming the primary key fails. Leave these``
| ``   --    with the old names for now.``
| ``   --    DROP CONSTRAINT ircid_pkey,``
| ``   --    ADD CONSTRAINT ircnickname_pkey PRIMARY KEY (id),``
| ``       DROP CONSTRAINT ircid_person_fk,``
| ``       ADD CONSTRAINT ircnickname__person__fk``
| ``           FOREIGN KEY (person) REFERENCES Person;``
| ``   ALTER INDEX ircid_person_idx RENAME TO ircnickname__person__idx;``

| ``   -- Create a view with the old table name for backwards compatibility.``
| ``   CREATE OR REPLACE VIEW IrcId AS SELECT * FROM IrcNickname;``

| ``   -- Make the backwards compatibility view updatable.``
| ``   CREATE OR REPLACE RULE IrcId_ins AS ON INSERT TO IrcId DO INSTEAD``
| ``       INSERT INTO IrcNickname VALUES (``
| ``           COALESCE(NEW.id, nextval('ircnickname_id_seq')),``
| ``           NEW.person,``
| ``           NEW.network,``
| ``           NEW.nickname)``
| ``       RETURNING IrcNickname.*;``

| ``   CREATE OR REPLACE RULE IrcId_upd AS ON UPDATE TO IrcId DO INSTEAD``
| ``       UPDATE IrcNickname SET``
| ``           id = NEW.id,``
| ``           person = NEW.person,``
| ``           network = NEW.network,``
| ``           nickname = NEW.nickname``
| ``       WHERE id = OLD.id``
| ``       RETURNING IrcNickname.*;``

| ``   CREATE OR REPLACE RULE IrcId_del AS ON DELETE TO IrcId DO INSTEAD``
| ``       DELETE FROM IrcNickname WHERE id = OLD.id``
| ``       RETURNING IrcNickname.*;``

``   INSERT INTO LaunchpadDatabaseRevision VALUES (2208, 85, 0);``