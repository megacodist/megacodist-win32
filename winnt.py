#
# 
#
"""It is a header file that defines the 32-bit Windows types and
constants that are defined by NT, but exposed through the Win32 API.
It is used in C/C++ programming languages to define data types
and function prototypes for Windows NT operating system.
"""
from win_basic_types import DwordFlag


class FILE_ATTRIBUTE(DwordFlag):
    """A DWORD flag which defines options for some file system-related APIs.
    """

    READONLY = 0x00000001
    """A file that is read-only. Applications can read the file, but
    cannot write to it or delete it. This attribute is not honored
    on directories.
    """

    HIDDEN = 0x00000002
    """The file or directory is hidden. It is not included in an
    ordinary directory listing.
    """

    SYSTEM = 0x00000004
    """A file or directory that the operating system uses a part of,
    or uses exclusively.
    """

    DIRECTORY = 0x00000010
    """The handle that identifies a directory."""

    ARCHIVE = 0x00000020
    """A file or directory that is an archive file or directory.
    Applications typically use this attribute to mark files for backup
    or removal.
    """

    DEVICE = 0x00000040
    """This value is reserved for system use."""

    NORMAL = 0x00000080
    """A file that does not have other attributes set. This attribute
    is valid only when used alone.
    """

    TEMPORARY = 0x00000100
    """A file that is being used for temporary storage. File systems
    avoid writing data back to mass storage if sufficient cache memory
    is available, because typically, an application deletes a temporary
    file after the handle is closed. In that scenario, the system can
    entirely avoid writing the data. Otherwise, the data is written after
    the handle is closed.
    """

    SPARSE_FILE = 0x00000200
    """A file that is a sparse file."""

    REPARSE_POINT = 0x00000400
    """A file or directory that has an associated reparse point, or a
    file that is a symbolic link.
    """

    COMPRESSED = 0x00000800
    """A file or directory that is compressed. For a file, all of the
    data in the file is compressed. For a directory, compression is the
    default for newly created files and subdirectories.
    """

    OFFLINE = 0x00001000
    """The data of a file is not available immediately. This attribute
    indicates that the file data is physically moved to offline storage.
    This attribute is used by Remote Storage, which is the hierarchical
    storage management software. Applications should not arbitrarily
    change this attribute.
    """

    NOT_CONTENT_INDEXED = 0x00002000
    """The file or directory is not to be indexed by the content
    indexing service.
    """

    ENCRYPTED = 0x00004000
    """A file or directory that is encrypted. For a file, all data
    streams in the file are encrypted. For a directory, encryption
    is the default for newly created files and subdirectories.
    """

    INTEGRITY_STREAM = 0x00008000
    """The directory or user data stream is configured with integrity
    (only supported on ReFS volumes). It is not included in an ordinary
    directory listing. The integrity setting persists with the file if
    it's renamed. If a file is copied the destination file will have
    integrity set if either the source file or destination directory have
    integrity set.

    Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista,
    Windows Server 2003 and Windows XP: This flag is not supported
    until Windows Server 2012.
    """

    VIRTUAL = 0x00010000
    """This value is reserved for system use."""
    
    NO_SCRUB_DATA = 0x00020000
    """The user data stream not to be read by the background data
    integrity scanner (AKA scrubber). When set on a directory it only
    provides inheritance. This flag is only supported on Storage Spaces
    and ReFS volumes. It is not included in an ordinary directory listing.

    Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista,
    Windows Server 2003 and Windows XP: This flag is not supported until
    Windows 8 and Windows Server 2012.
    """

    EA = 0x00040000
    """A file or directory with extended attributes."""

    PINNED = 0x00080000
    """This attribute indicates user intent that the file or directory
    should be kept fully present locally even when not being actively
    accessed. This attribute is for use with hierarchical storage
    management software.
    """

    UNPINNED = 0x00100000
    """This attribute indicates that the file or directory should not
    be kept fully present locally except when being actively accessed.
    This attribute is for use with hierarchical storage management software.
    """

    RECALL_ON_OPEN = 0x00040000
    """This attribute only appears in directory enumeration classes
    (FILE_DIRECTORY_INFORMATION, FILE_BOTH_DIR_INFORMATION, etc.).
    When this attribute is set, it means that the file or directory has
    no physical representation on the local system; the item is virtual.
    Opening the item will be more expensive than normal, e.g. it will
    cause at least some of it to be fetched from a remote store.
    """

    RECALL_ON_DATA_ACCESS = 0x00400000
    """When this attribute is set, it means that the file or directory
    is not fully present locally. For a file that means that not all of
    its data is on local storage (e.g. it may be sparse with some data
    still in remote storage). For a directory it means that some of the
    directory contents are being virtualized from another location.
    Reading the file / enumerating the directory will be more expensive
    than normal, e.g. it will cause at least some of the file/directory
    content to be fetched from a remote store. Only kernel-mode callers
    can set this bit."""
