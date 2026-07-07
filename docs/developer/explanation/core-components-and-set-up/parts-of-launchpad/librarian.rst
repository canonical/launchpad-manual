.. meta::
   :description: How Launchpad's librarian stores and retrieves files,
      including URL resolution, database relationships, and Swift
      storage strategy.

.. _librarian-file-storage:

Librarian file storage
======================

Librarian is Launchpad's file storage service. It stores and serves
hundreds of millions of files and provides durability at scale, deduplication,
and deterministic file location. It uses the OpenStack Swift service
for storing the files.

Core design
-----------

Librarian uses aliases to represent why a file exists in the system and
content to represent the actual file bytes.

Aliases
~~~~~~~

An alias represents the external interface to a file. It stores:

- The URL to download the source package
- The MIME type to send to the web browser or a client
- Whether or not access to the file is restricted (private)

An alias has a numeric ID, filename, MIME type, creation date, expiry,
hits count, and a restriction flag. A file with ID 849901997 and filename
git_2.53.0-1ubuntu1.dsc is accessed via
https://launchpadlibrarian.net/849901997/git_2.53.0-1ubuntu1.dsc.

Content
~~~~~~~

Content represents the physical bytes on disk. It stores:

- The numeric ID used to determine a file's location.
- Multiple cryptographic hashes of the file's contents.
- The file size.
- The creation timestamp

Aliases and content separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two different packages may need the exact same tarball. Without this
separation, the tarball would be stored twice on disk with duplicate hashes.
With separation, both packages reference the same content record. The
tarball is stored once, saving storage and ensuring consistency. If the
file is deleted, both references are deleted.

URL-to-file lookup flow
-----------------------

When a user visits
https://launchpadlibrarian.net/849901997/git_2.53.0-1ubuntu1.dsc, the
following steps occur.

Step 1. URL Parsing
~~~~~~~~~~~~~~~~~~~

The librarian extracts the alias ID (849901997) and the filename
(git_2.53.0-1ubuntu1.dsc).

AStep 2. Alias lookup in the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian queries for LibraryFileAlias where id equals 849901997.
The result includes:

.. code-block:: text

   id: 849901997
   content_id: 1234567
   filename: git_2.53.0-1ubuntu1.dsc
   mimetype: text/plain
   date_created: 2025-06-01
   restricted: false

Step 3. Filename validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian compares the URL filename against the database filename.
If they match, continue. If not, return 404. The filename acts as a
secret URL component. You cannot guess a working URL without knowing
both the alias ID and the correct filename. This prevents casual
enumeration attacks.

Step 4. Content metadata retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Content metadata matching `content_id` value of 1234567 is retrieved.

.. code-block:: text

   id: 1234567
   filesize: 2847
   md5: a1b2c3d4e5f6789abcdef0123456789a
   sha1: 9a8b7c6d5e4f3210abcdef0123456789abcdef01
   date_created: 2025-05-15

Response headers will include the file size and hashes.

Step 5. File location in the storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian uses the content ID to calculate where the file physically
lives (integer division).

.. code-block:: text

   container_number = content_id // 500000
                    = 1234567 // 500000
                    = 2

   container_name = librarian_2
   object_name = 1234567

The file is stored at librarian_2/1234567.

Step 6. File retrieval from storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The librarian connects to Swift (or falls back to disk) and fetches the
object. Response headers are set from database metadata:

.. code-block:: text

   Content-Type: text/plain
   Content-Length: 2847
   Last-Modified: 2025-06-01T14:32:00Z
   Cache-Control: max-age=31536000, public

Librarian sets the cache control headers for public files to allow a year
of caching and disables caching for restricted files.

Step 7. File sent to the client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
makes old files irretrievable. Hardcoding prevents this misconfiguration.

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

Swift has a hard limit on file size and no single object can exceed 5 GB.
The librarian handles larger files using Dynamic Large Objects (DLO), a
standard Swift mechanism. Please check
https://docs.openstack.org/swift/latest/overview_large_objects.html
for more details.

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

The Librarian's design comes with several trade-offs.

The 500,000 file limit is hardcoded. This prevents misconfiguration but
sacrifices operational flexibility.

Although the alias/content separation saves a lot of storage, it adds
a database join on every lookup and causes a slight performance impact.

The file location is calculated mathematically rather than looked up. This
eliminates a centralized registry but freezes container assignments once
issued.

With large file segmentation, each segment has to be cleaned up explicitly
during garbage collection.

Disk versus Swift
~~~~~~~~~~~~~~~~~

Launchpad migrates old files from local disk to Swift. Swift has several
advantages over disk:

- Handles hundreds of millions of objects without I/O bottlenecks
- Replicates across data centers (disk is a single point of failure)
- Cheaper for long-term cold storage

A disk fallback is maintained for files missing from Swift (e.g., during
migration).
