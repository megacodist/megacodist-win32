#
# Copyright notice goes in here...
#
"""Exposes APIs to work with Windows ole32.dll file."""

import ctypes


# Windows basic types ===============================================
from ctypes import HRESULT
from ctypes.wintypes import LPVOID


_ole32 = ctypes.OleDLL('ole32')


def CoInitialize(ll: LPVOID) -> HRESULT:
    """Initializes the COM library on the current thread and identifies
    the concurrency model as single-thread apartment (STA).
    """
    pass
CoInitialize = _ole32.CoInitialize
CoInitialize.argtypes = (LPVOID,)
CoInitialize.restype = HRESULT
