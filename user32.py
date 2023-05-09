#
# 
#
"""Exposes APIs to work with Windows user32.dll file.

Dependencies:
1. Windows XP or later
"""
from __future__ import annotations
import ctypes

# Windows basic types ===============================================
from win_basic_types import BOOL, HICON


# Loading DLL object ================================================
_user32 = ctypes.OleDLL('user32')


# DLL functions =====================================================
def DestroyIcon(hIcon: HICON) -> BOOL:
    """Destroys an icon and frees any memory the icon occupied.
    """
    pass
DestroyIcon = _user32.DestroyIcon
DestroyIcon.argtypes = (HICON,)
DestroyIcon.restype = BOOL
