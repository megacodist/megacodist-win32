#
# 
#
"""This is a header file used in C/C++/Objective-C programming languages.
It contains programming interfaces for:

* Windows Shell
* Windows Property System
* Windows Runtime C++ reference
* Windows Search
* Windows Sidebar
* WMI Provider for NFS2
"""
from __future__ import annotations
import ctypes
import enum


# Windows data types ================================================
from win_basic_types import UlongFlag, LP_ULONG


class SFGAO(UlongFlag):
    """Attributes that can be retrieved on an item (file or folder)
    or set of items.
    """
    CANCOPY = 0x00000001
    """The specified items can be copied."""

    CANMOVE = 0x00000002
    """The specified items can be moved."""

    CANLINK = 0x00000004
    """Shortcuts can be created for the specified items. This attribute
    has the same value as DROPEFFECT_LINK. If a namespace extension returns
    this attribute, a Create Shortcut entry with a default handler is
    added to the shortcut menu that is displayed during drag-and-drop
    operations. The extension can also implement its own handler for
    the link verb in place of the default. If the extension does so,
    it is responsible for creating the shortcut. A Create Shortcut item
    is also added to the Windows Explorer File menu and to normal
    shortcut menus. If the item is selected, your application's
    IContextMenu::InvokeCommand method is invoked with the lpVerb
    member of the CMINVOKECOMMANDINFO structure set to link. Your
    application is responsible for creating the link.
    """

    STORAGE = 0x00000008
    """The specified items can be bound to an IStorage object through
    IShellFolder.BindToObject."""

    CANRENAME = 0x00000010
    """The specified items can be renamed. Note that this value is
    essentially a suggestion; not all namespace clients allow items
    to be renamed. However, those that do must have this attribute set.
    """

    CANDELETE = 0x00000020
    """The specified items can be deleted."""

    HASPROPSHEET = 0x00000040
    """The specified items have property sheets."""

    DROPTARGET = 0x00000100
    """The specified items are drop targets."""

    CAPABILITYMASK = 0x00000177
    """This flag is a mask for the capability attributes: CANCOPY, CANMOVE,
    CANLINK, CANRENAME, CANDELETE, HASPROPSHEET, and DROPTARGET. Callers
    normally do not use this value.
    """

    SYSTEM = 0x00001000
    """Windows 7 and later. The specified items are system items."""

    ENCRYPTED = 0x00002000
    """The specified items are encrypted and might require special
    presentation.
    """

    ISSLOW = 0x00004000
    """Accessing the item (through IStream or other storage interfaces)
    is expected to be a slow operation. Applications should avoid
    accessing items flagged with ISSLOW.
    Opening a stream for an item is generally a slow operation at all
    times. ISSLOW indicates that it is expected to be especially
    slow, for example in the case of slow network connections or
    offline (FILE_ATTRIBUTE_OFFLINE) files. However, querying
    ISSLOW is itself a slow operation. Applications should query
    ISSLOW only on a background thread. An alternate method, such
    as retrieving the PKEY_FileAttributes property and testing for
    FILE_ATTRIBUTE_OFFLINE, could be used in place of a method call
    that involves ISSLOW.
    """

    GHOSTED = 0x00008000
    """The specified items are shown as dimmed and unavailable to the user."""

    LINK = 0x00010000
    """The specified items are shortcuts."""

    SHARE = 0x00020000
    """The specified objects are shared."""

    READONLY = 0x00040000
    """The specified items are read-only. In the case of folders, this
    means that new items cannot be created in those folders. This
    should not be confused with the behavior specified by the
    FILE_ATTRIBUTE_READONLY flag retrieved by IColumnProvider.GetItemData
    in a SHCOLUMNDATA structure. FILE_ATTRIBUTE_READONLY has no meaning
    for Win32 file system folders.
    """

    HIDDEN = 0x00080000
    """The item is hidden and should not be displayed unless the
    Show hidden files and folders option is enabled in Folder Settings.
    """

    DISPLAYATTRMASK = 0x000FC000
    """Do not use."""

    NONENUMERATED = 0x00100000
    """The items are nonenumerated items and should be hidden. They are
    not returned through an enumerator such as that created by the
    IShellFolder.EnumObjects method.
    """

    NEWCONTENT = 0x00200000
    """The items contain new content, as defined by the particular
    application.
    """

    STREAM = 0x00400000
    """Indicates that the item has a stream associated with it. That
    stream can be accessed through a call to IShellFolder.BindToObject
    or IShellItem.BindToHandler with IID_IStream in the riid parameter.
    """

    STORAGEANCESTOR = 0x00800000
    """Children of this item are accessible through IStream or IStorage.
    Those children are flagged with STORAGE or STREAM.
    """

    VALIDATE = 0x01000000
    """When specified as input, VALIDATE instructs the folder to validate
    that the items contained in a folder or Shell item array exist. If
    one or more of those items do not exist, IShellFolder::GetAttributesOf
    and IShellItemArray::GetAttributes return a failure code. This flag
    is never returned as an [out] value.

    When used with the file system folder, VALIDATE instructs the folder
    to discard cached properties retrieved by clients of
    IShellFolder2.GetDetailsEx that might have accumulated for the
    specified items.
    """

    REMOVABLE = 0x02000000
    """The specified items are on removable media or are themselves
    removable devices.
    """

    COMPRESSED = 0x04000000
    """The specified items are compressed."""

    BROWSABLE = 0x08000000
    """The specified items can be hosted inside a web browser or
    Windows Explorer frame.
    """

    FILESYSANCESTOR = 0x10000000
    """The specified folders are either file system folders or contain
    at least one descendant (child, grandchild, or later) that is a
    file system (FILESYSTEM) folder.
    """

    FOLDER = 0x20000000
    """The specified items are folders. Some items can be flagged with
    both STREAM and FOLDER, such as a compressed file with a .zip file
    name extension. Some applications might include this flag when testing
    for items that are both files and containers.
    """

    FILESYSTEM = 0x40000000
    """The specified folders or files are part of the file system (that
    is, they are files, directories, or root directories). The parsed
    names of the items can be assumed to be valid Win32 file system paths.
    These paths can be either UNC or drive-letter based.
    """

    STORAGECAPMASK = 0x70C50008
    """This flag is a mask for the storage capability attributes: STORAGE,
    LINK, READONLY, STREAM, STORAGEANCESTOR, FILESYSANCESTOR, FOLDER, and
    FILESYSTEM. Callers normally do not use this value.
    """

    HASSUBFOLDER = 0x80000000
    """The specified folders have subfolders. The HASSUBFOLDER attribute
    is only advisory and might be returned by Shell folder
    implementations even if they do not contain subfolders. Note,
    however, that the converse—failing to return HASSUBFOLDER—definitively
    states that the folder objects do not have subfolders.

    Returning HASSUBFOLDER is recommended whenever a significant amount
    of time is required to determine whether any subfolders exist. For
    example, the Shell always returns HASSUBFOLDER when a folder is
    located on a network drive.
    """

    CONTENTSMASK = 0x80000000
    """This flag is a mask for content attributes, at present only
    HASSUBFOLDER. Callers normally do not use this value.
    """

    PKEYSFGAOMASK = 0x81044000
    """Mask used by the PKEY_SFGAOFlags property to determine attributes
    that are considered to cause slow calculations or lack context:
    ISSLOW, READONLY, HASSUBFOLDER, and VALIDATE. Callers normally
    do not use this value.
    """


LP_SFGAO = LP_ULONG
"""A pointer to SFGAO."""
