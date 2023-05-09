"""This module contains data types that are used by Windows Shell.

A lot of documentations and docstrings rely on Microsoft Learn.
"""

import ctypes


# Windows basic types ===============================================
from win_basic_types import BYTE, USHORT


class SHITEMID(ctypes.Structure):
    """Defines an item identifier."""
    _fields_ = [
        ('cb', USHORT),
        ('abID', BYTE)]


class ITEMIDLIST(ctypes.Structure):
    """Contains a list of item identifiers. Objects of this type are
    used to address either file system items such as files, folders,
    symlinks or virtual items such as 'This PC' or files on a device
    connected to the computer.
    """
    _fields_ = [('mkid', SHITEMID)]


ITEMIDLIST_ABSOLUTE = ITEMIDLIST
"""Fully qualified ITEMIDLIST relative to the root of the namespace.
It may be multi-level.
"""
ITEMIDLIST_RELATIVE = ITEMIDLIST
"""An ITEMIDLIST relative to a parent folder. It may be multi-level."""
ITEMID_CHILD = ITEMIDLIST
"""Single-level ITEMIDLIST relative to a parent folder. It contains
exactly one SHITEMID structure.
"""

LP_IDLIST_ABSOLUTE = ctypes.POINTER(ITEMIDLIST_ABSOLUTE)
"""A pointer to ITEMIDLIST which is absolute and has been allocated, as
indicated by its being non-constant. This means that it needs to be
deallocated with ILFree when it is no longer needed. Because it is a
direct pointer to allocated memory, it is aligned.
"""
LP_LP_IDLIST_ABSOLUTE = ctypes.POINTER(LP_IDLIST_ABSOLUTE)
LP_CIDLIST_ABSOLUTE = ctypes.POINTER(ITEMIDLIST_ABSOLUTE)
"""A pointer to ITEMIDLIST which is absolute and constant. This is
typically used when you are passed an absolute ITEMIDLIST as a parameter
but do not own it, and so are not allowed to change it.
"""
LP_CUIDLIST_ABSOLUTE = ctypes.POINTER(ITEMIDLIST_ABSOLUTE)
"""A pointer to ITEMIDLIST which is absolute, constant and unaligned.
This is rarely used. Absolute ITEMIDLIST are typically allocated in
memory aligned to a DWORD boundary in 32-bit architectures and to a
QWORD boundary in 64-bit architectures. An absolute ITEMIDLIST would be
unaligned only if it has been byte-packed along with other data, such as
in a serialization format.
"""
LP_IDLIST_RELATIVE = ctypes.POINTER(ITEMIDLIST_RELATIVE)
LP_CIDLIST_RELATIVE = ctypes.POINTER(ITEMIDLIST_RELATIVE)
LP_UIDLIST_RELATIVE = ctypes.POINTER(ITEMIDLIST_RELATIVE)
LP_CUIDLIST_RELATIVE = ctypes.POINTER(ITEMIDLIST_RELATIVE)
LP_ITEMID_CHILD = ctypes.POINTER(ITEMID_CHILD)
LP_CITEMID_CHILD = ctypes.POINTER(ITEMID_CHILD)
LP_UITEMID_CHILD = ctypes.POINTER(ITEMID_CHILD)
LP_CUITEMID_CHILD = ctypes.POINTER(ITEMID_CHILD)
LP_CUITEMID_CHILD_ARRAY = ctypes.POINTER(LP_CUITEMID_CHILD)
LP_CUIDLIST_RELATIVE_ARRAY = ctypes.POINTER(LP_CUIDLIST_RELATIVE)
LP_CIDLIST_ABSOLUTE_ARRAY = ctypes.POINTER(LP_CIDLIST_ABSOLUTE)
LP_CUIDLIST_ABSOLUTE_ARRAY = ctypes.POINTER(LP_CUIDLIST_ABSOLUTE)
