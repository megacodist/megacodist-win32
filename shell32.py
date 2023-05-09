#
# Copyright notice goes in here...
#
"""Exposes APIs to work with Windows shell32.dll file.

Dependencies:
1. Windows XP or later
"""
# Checking underlying OS ============================================
import platform

_osOk = platform.system() == 'Windows'
_osVer = [int(num) for num in platform.version().split('.')]
if _osOk and not (_osVer >= [5, 1]):
    raise OSError(f"'{__name__}' requires Windows XP or later.")

# Importing variables ===============================================
import ctypes

from objidl import LP_IBindCtx
from shellapi import LP_SHFILEINFOW
from shobjidl import LP_SFGAO, SFGAO
from shtypes import (
    LP_CIDLIST_ABSOLUTE, LP_CUIDLIST_RELATIVE, LP_CUITEMID_CHILD_ARRAY,
    LP_IDLIST_ABSOLUTE, LP_ITEMID_CHILD, LP_LP_IDLIST_ABSOLUTE,
    LP_UITEMID_CHILD)
from winnt import FILE_ATTRIBUTE
# Windows basic types ===============================================
from win_basic_types import (
    DWORD, DWORD_PTR, DwordFlag, HRESULT, LPCWSTR, UINT, UintFlag)


# Flags =============================================================
class OFASI(DwordFlag):
    """A DWORD flag which defines some options for
    SHOpenFolderAndSelectItems DLL function.
    """

    NONE = 0x0000
    """No flag."""

    EDIT = 0x0001
    """Select an item and put its name in edit mode. This flag can only be
    used when a single item is being selected. For multiple item selections,
    it is ignored.
    """

    OPENDESKTOP = 0x0002
    """Select the item or items on the desktop rather than in a Windows
    Explorer window. Note that if the desktop is obscured behind open
    windows, it will not be made visible.
    """


class SHGFI(UintFlag):
    """A UINT flag which defines some options for SHGetFileInfoW
    function in shell32.dll.
    """

    ADDOVERLAYS = 0x000000020
    """Version 5.0. Apply the appropriate overlays to the file's icon.
    The ICON flag must also be set.
    """

    ATTR_SPECIFIED = 0x000020000
    """Modify ATTRIBUTES flag to indicate that the dwAttributes member of
    the SHFILEINFO structure at psfi contains the specific attributes
    that are desired. These attributes are passed to
    IShellFolder.GetAttributesOf. If this flag is not specified,
    0xFFFFFFFF is passed to IShellFolder.GetAttributesOf, requesting
    all attributes. This flag cannot be specified with the ICON flag.
    """

    ATTRIBUTES = 0x000000800
    """Retrieve the item attributes. The attributes are copied to the
    dwAttributes member of the structure specified in the psfi parameter.
    These are the same attributes that are obtained from
    IShellFolder.GetAttributesOf.
    """

    DISPLAYNAME = 0x000000200
    """Retrieve the display name for the file, which is the name as it
    appears in Windows Explorer. The name is copied to the szDisplayName
    member of the structure specified in psfi. The returned display
    name uses the long file name, if there is one, rather than the 8.3
    form of the file name. Note that the display name can be affected
    by settings such as whether extensions are shown.
    """

    EXETYPE = 0x000002000
    """Retrieve the type of the executable file if pszPath identifies
    an executable file. The information is packed into the return value.
    This flag cannot be specified with any other flags.
    """

    ICON = 0x000000100
    """Retrieve the handle to the icon that represents the file and the
    index of the icon within the system image list. The handle is copied
    to the hIcon member of the structure specified by psfi, and the
    index is copied to the iIcon member.
    """

    ICONLOCATION = 0x000001000
    """Retrieve the name of the file that contains the icon representing
    the file specified by pszPath, as returned by the
    IExtractIcon.GetIconLocation method of the file's icon handler.
    Also retrieve the icon index within that file. The name of the file
    containing the icon is copied to the szDisplayName member of the
    structure specified by psfi. The icon's index is copied to that
    structure's iIcon member.
    """

    LARGEICON = 0x000000000
    """Modify ICON flag, causing the function to retrieve the file's large
    icon. The ICON flag must also be set.
    """

    LINKOVERLAY = 0x000008000
    """Modify ICON flag, causing the function to add the link overlay to
    the file's icon. The ICON flag must also be set.
    """

    OPENICON = 0x000000002
    """Modify ICON flag, causing the function to retrieve the file's
    open icon. Also used to modify SYSICONINDEX flag, causing the function
    to return the handle to the system image list that contains the
    file's small open icon. A container object displays an open icon
    to indicate that the container is open. The ICON and/or SYSICONINDEX
    flags must also be set.
    """

    OVERLAYINDEX = 0x000000040
    """Version 5.0. Return the index of the overlay icon. The value of
    the overlay index is returned in the upper eight bits of the iIcon
    member of the structure specified by psfi. This flag requires that
    the ICON flag be set as well.
    """

    PIDL = 0x000000008
    """Indicate that pszPath is the address of an ITEMIDLIST structure
    rather than a path name.
    """

    SELECTED = 0x000010000
    """Modify ICON flag, causing the function to blend the file's icon
    with the system highlight color. The ICON flag must also be set.
    """

    SHELLICONSIZE = 0x000000004
    """Modify ICON flag, causing the function to retrieve a Shell-sized
    icon. If this flag is not specified the function sizes the icon
    according to the system metric values. The ICON flag must also be set.
    """

    SMALLICON = 0x000000001
    """Modify ICON flag, causing the function to retrieve the file's
    small icon. Also used to modify SYSICONINDEX flag, causing the
    function to return the handle to the system image list that
    contains small icon images. The ICON and/or SYSICONINDEX flags must
    also be set.
    """

    SYSICONINDEX = 0x000004000
    """Retrieve the index of a system image list icon. If successful,
    the index is copied to the iIcon member of psfi. The return value
    is a handle to the system image list. Only those images whose indices
    are successfully copied to iIcon are valid. Attempting to access
    other images in the system image list will result in undefined behavior.
    """

    TYPENAME = 0x000000400
    """Retrieve the string that describes the file's type. The string is
    copied to the szTypeName member of the structure specified in psfi.
    """

    USEFILEATTRIBUTES = 0x000000010
    """Indicates that the function should not attempt to access the file
    specified by pszPath. Rather, it should act as if the file specified
    by pszPath exists with the file attributes passed in dwFileAttributes.
    This flag cannot be combined with the ATTRIBUTES, EXETYPE, or PIDL
    flags.
    """


# Loading DLL object ================================================
_shell32 = ctypes.OleDLL('shell32')
"""Windows shell32 DLL object."""


# DLL functions =====================================================
def ILCloneFirst(pidl: LP_CUIDLIST_RELATIVE) -> LP_ITEMID_CHILD:
    """Clones the first SHITEMID structure in an ITEMIDLIST structure."""
    pass
ILCloneFirst = _shell32.ILCloneFirst
ILCloneFirst.argtypes = (LP_CUIDLIST_RELATIVE,)
ILCloneFirst.restype = LP_ITEMID_CHILD


def ILFindLastID(pidl: LP_CUIDLIST_RELATIVE) -> LP_UITEMID_CHILD:
    """Returns a pointer to the last SHITEMID structure in an ITEMIDLIST
    structure. This function does not clone the last item, so you do not
    have to call ILFree to release the returned pointer.
    """
    pass
ILFindLastID = _shell32.ILFindLastID
ILFindLastID.argtypes = (LP_CUIDLIST_RELATIVE,)
ILFindLastID.restype = LP_UITEMID_CHILD


def ILFree(pidl: LP_IDLIST_ABSOLUTE) -> None:
    """Frees an ITEMIDLIST structure allocated by the Shell."""
    pass
ILFree = _shell32.ILFree
ILFree.argtypes = (LP_IDLIST_ABSOLUTE,)
ILFree.restype = None


def SHGetFileInfoW(
        pszPath: LPCWSTR,
        dwFileAttributes: FILE_ATTRIBUTE,
        psfi: LP_SHFILEINFOW,
        cbFileInfo: UINT,
        uFlags: SHGFI,
        ) -> DWORD_PTR:
    pass
SHGetFileInfoW = _shell32.SHGetFileInfoW
SHGetFileInfoW.argtypes = (
    LPCWSTR,
    FILE_ATTRIBUTE,
    LP_SHFILEINFOW,
    UINT,
    SHGFI)
SHGetFileInfoW.restype = DWORD_PTR


def SHOpenFolderAndSelectItems(
        pidlFolder: LP_CIDLIST_ABSOLUTE,
        cidl: UINT,
        apidl: LP_CUITEMID_CHILD_ARRAY,
        dwFlags: OFASI,
        ) -> HRESULT:
    """Opens a Windows Explorer window with specified items in a
    particular folder selected.
    """
    pass
SHOpenFolderAndSelectItems = _shell32.SHOpenFolderAndSelectItems
SHOpenFolderAndSelectItems.argtypes = (
    LP_CIDLIST_ABSOLUTE,
    UINT,
    LP_CUITEMID_CHILD_ARRAY,
    DWORD,)
SHOpenFolderAndSelectItems.restype = HRESULT


def SHParseDisplayName(
            pszName: LPCWSTR,
            pbc: LP_IBindCtx,
            ppidl: LP_LP_IDLIST_ABSOLUTE,
            sfgaoIn: SFGAO,
            psfgaoOut: LP_SFGAO,
            ) -> HRESULT:
    """Translates a Shell namespace object's display name into an item
    identifier list and returns the attributes of the object. This function
    is the preferred method to convert a string to a pointer to an item
    identifier list (PIDL).
    """
    pass
SHParseDisplayName = _shell32.SHParseDisplayName
SHParseDisplayName.argtypes = (
    LPCWSTR,
    LP_IBindCtx,
    LP_LP_IDLIST_ABSOLUTE,
    SFGAO,
    LP_SFGAO,)
SHParseDisplayName.restype = HRESULT
