.. meta::
   :description: How Launchpad's librarian stores and retrieves files,
      including URL resolution, database relationships, and Swift
      storage strategy.

.. _librarian-file-storage:

Librarian file storage
======================

Introduction
------------

Launchpad stores millions of files. The librarian subsystem addresses three
core problems: durability at scale, deduplication, and deterministic
file location. It separates concerns through two concepts: aliases
represent why a file exists in the system, and content represents the
actual file bytes.

Core design
-----------

The design uses two database concepts to separate concerns: aliases and
content.

Aliases
~~~~~~~

An alias represents the external interface to a file. It stores:

- What is the URL to download the source package git_2.53.0?
- What MIME type should we tell the browser?
- Is this a restricted (private) file?

An alias has a numeric ID, filename, MIME type, creation date, and
restriction flag. A file with ID 849901997 and filename
git_2.53.0-1ubuntu1.dsc is accessed via
https://launchpadlibrarian.net/849901997/git_2.53.0-1ubuntu1.dsc.

Content
~~~~~~~

Content represents the physical bytes on disk. It stores:

- What is the cryptographic hash?
- How big is the file?
- Where is it stored?

Each content record has a numeric ID used for storage location
calculation, the file size, multiple cryptographic hashes, and a
creation timestamp.

Alias and content separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two different packages often need the exact same tarball. Without
separation, the tarball is stored twice on disk with duplicate hashes.
With separation, both packages reference the same content record. The
tarball is stored once, saving storage and ensuring consistency. If the
file is deleted, both references disappear together.

The URL-to-file lookup flow
---------------------------

When a user visits
https://launchpadlibrarian.net/849901997/git_2.53.0-1ubuntu1.dsc, the
following steps occur.

Step 1. Parse the URL
~~~~~~~~~~~~~~~~~~~~~

The librarian extracts the alias ID (849901997) and the filename
(git_2.53.0-1ubuntu1.dsc).

Step 2. Look up the alias in the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian queries for LibraryFileAlias where id equals 849901997.
The result includes:

.. code-block:: text

   id: 849901997
   content_id: 1234567
   filename: git_2.53.0-1ubuntu1.dsc
   mimetype: text/plain
   date_created: 2025-06-01
   restricted: false

Step 3. Validate the filename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian compares the URL filename against the database filename.
If they match, continue. If not, return 404. The filename acts as a
secret URL component. You cannot guess a working URL without knowing
both the alias ID and the correct filename. This prevents casual
enumeration attacks.

Step 4. Look up the content record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using content_id 1234567, retrieve the content metadata:

.. code-block:: text

   id: 1234567
   filesize: 2847
   md5: a1b2c3d4e5f6789abcdef0123456789a
   sha1: 9a8b7c6d5e4f3210abcdef0123456789abcdef01
   date_created: 2025-05-15

Response headers will include the file size and hashes.

Step 5. Locate the file in storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian uses the content ID to calculate where the file physically
lives (integer division).

.. code-block:: text

   container_number = content_id // 500000
                    = 1234567 // 500000
                    = 2

   container_name = librarian_2
   object_name = 1234567

The file is stored at librarian_2/1234567.

Step 6. Retrieve from storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian connects to Swift (or falls back to disk) and fetches the
object. Response headers are set from database metadata:

.. code-block:: text

   Content-Type: text/plain
   Content-Length: 2847
   Last-Modified: 2025-06-01T14:32:00Z
   Cache-Control: max-age=31536000, public

Public files get one year of cache. Restricted files get no cache.

Step 7. Stream to the client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file bytes are sent to the client.

Physical storage at scale
--------------------------

Swift and most object storage systems have performance limits on
containers. Performance degrades beyond about one million objects per
container, with a hard practical limit around ten million. Launchpad has
processed nearly one billion files, making a single container infeasible.

Distribution by ID
~~~~~~~~~~~~~~~~~~~

The librarian divides files into containers based on ID ranges. Files
with ID 0–499,999 go to librarian_0, IDs 500,000–999,999 to
librarian_1, and IDs 1,000,000–1,499,999 to librarian_2, and so on.

Each container holds up to 500,000 files. This limit is conservative:
Swift can theoretically handle a million or more, but large files
consume multiple slots, making 500,000 safer in practice.

Hardcoded limits
~~~~~~~~~~~~~~~~

The 500,000 limit is hardcoded, not configurable. If changed in a config
file to one million, the librarian would store new files in different
containers while old files remain in their original containers. This
makes old files unretrievable. Hardcoding prevents this misconfiguration.

What happens when a container fills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Containers do not fill dynamically. A new file does not try to fit into
an available container. Its content ID determines which container it goes
to. Once a container is assigned a range of IDs, those IDs always map to
that container, whether it has 10 files or 500,000.

When a container reaches 500,000 files, it is effectively frozen for new
writes. Deletes and garbage collection continue. The next files created
get higher IDs that naturally map to the next container.

Dynamic large objects
---------------------

Swift has a hard limit. No single object can exceed 5 GB. The librarian
handles larger files using Dynamic Large Objects (DLO), a standard Swift
mechanism.

How DLO works
~~~~~~~~~~~~~

When uploading a 12 GB file, the librarian chunks the file into 5 GB
pieces.

Segment 0 contains bytes 0 to 5 GB. Segment 1 contains bytes 5 GB to 10
GB. Segment 2 contains bytes 10 GB to 12 GB.

Each segment is stored with a slash in its name.

.. code-block:: text

   librarian_2/1234567/0000
   librarian_2/1234567/0001
   librarian_2/1234567/0002

An empty object is created at librarian_2/1234567 with a special header.

.. code-block:: text

   Name: librarian_2/1234567
   Content-Length: 0
   X-Object-Manifest: librarian_2/1234567/

This tells Swift to concatenate everything in the
librarian_2/1234567/ directory in order when requested.

Transparent reassembly
~~~~~~~~~~~~~~~~~~~~~~

When a user downloads the file, the librarian fetches librarian_2/1234567.
Swift sees the X-Object-Manifest header and automatically concatenates
the three segments. The user receives all 12 GB as a single stream.

From the user's perspective, the URL works exactly the same. They have
no idea the file was segmented.

Practical limits
~~~~~~~~~~~~~~~~

With up to 10,000 segments, the maximum file size is around 50 TB. When a
large file is deleted, the librarian explicitly removes all segments and
the manifest to prevent orphaned data.

Design trade-offs
-----------------

The design involves several trade-offs.

The 500,000 file limit is hardcoded, not configurable. This prevents
misconfiguration but sacrifices operational flexibility.

Alias/content separation adds a database join on every lookup. It saves
enormous storage through deduplication.

File location is calculated mathematically rather than looked up. This
eliminates a centralized registry but freezes container assignments once
issued.

Large file segmentation is completely hidden from users. A 12 GB file
appears as a single file. The cost is explicit segment cleanup during
garbage collection.

Disk versus Swift
~~~~~~~~~~~~~~~~~

Launchpad migrates old files from local disk to Swift. Swift has several
advantages over disk:

- Handles hundreds of millions of objects without I/O bottlenecks
- Replicates across data centers (disk is a single point of failure)
- Cheaper for long-term cold storage

A disk fallback is maintained for files missing from Swift (e.g., during
migration).

Summary
-------

Aliases provide the user-facing interface (URLs, filenames, metadata).
Content provides deduplication and integrity (hashes, storage location).
ID-based distribution spreads files across containers without a
centralized registry. DLO transparently handles files larger than 5 GB.
Hardcoded limits prevent misconfiguration.
