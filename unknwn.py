#
# Copyright goes in here...
#
"""This header is used by Component Object Model (COM)."""

import ctypes
import comtypes


# Windows basic types ===============================================
from ctypes.wintypes import ULONG


IUnknown = comtypes.IUnknown
"""Enables clients to get pointers to other interfaces on a given
object through the QueryInterface method, and manage the existence of
the object through the AddRef and Release methods. All other COM
interfaces are inherited, directly or indirectly, from IUnknown.
Therefore, the three methods in IUnknown are the first entries in the
vtable for every interface.
"""


LP_IUnknown = ctypes.POINTER(IUnknown)
"""A pointer to IUnknown."""


LP_LP_IUnknown = ctypes.POINTER(LP_IUnknown)
"""A pointer to PIUnknown or a pointer to a pointer of IUnknown."""
