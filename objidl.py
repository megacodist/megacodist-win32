#
# Copyright notice goes in here...
#
"""
"""

import ctypes

from comtypes import GUID


# Windows basic types ===============================================
from win_basic_types import DWORD, HWND, LCID, LPWSTR
from unknwn import IUnknown
from wtypesbase import LP_COAUTHINFO


class COSERVERINFO(ctypes.Structure):
    """Identifies a remote computer resource to the activation functions."""
    _fields_ = [
        ('dwReserved1', DWORD),
        ('pwszName', LPWSTR),
        ('pAuthInfo', LP_COAUTHINFO),
        ('dwReserved2', DWORD),]


LPCOSERVERINFO = ctypes.POINTER(COSERVERINFO)
"""A pointer to COSERVERINFO."""


class BIND_OPTS3(ctypes.Structure):
    """Contains parameters used during a moniker-binding operation."""
    _fields_ = [
        ('cbStruct', DWORD),
        ('grfFlags', DWORD),
        ('grfMode', DWORD),
        ('dwTickCountDeadline', DWORD),
        ('dwTrackFlags', DWORD),
        ('dwClassContext', DWORD),
        ('locale', LCID),
        ('pServerInfo', LPCOSERVERINFO),
        ('hwnd', HWND),]


LP_BIND_OPTS3 = ctypes.POINTER(BIND_OPTS3)
"""A pointer to BIND_OPTS3."""


class IRunningObjectTable(IUnknown):
    """Provides access to a bind context, which is an object that
    stores information about a particular moniker binding operation.
    """
    _case_insensitive_ = True
    _iid_ = GUID("{00000010-0000-0000-C000-000000000046}")
    _idlflags_ = []


class IBindCtx(IUnknown):
    """Provides access to a bind context, which is an object that
    stores information about a particular moniker binding operation.
    """
    _case_insensitive_ = True
    _iid_ = GUID("{0000000E-0000-0000-C000-000000000046}")
    _idlflags_ = []


LP_IBindCtx = ctypes.POINTER(IBindCtx)
"""A pointer to IBindCtx."""


LP_LP_IBindCtx = ctypes.POINTER(LP_IBindCtx)
"""A pointer to PIBindCtx or a pointer to a pointer to a IBindCtx."""
