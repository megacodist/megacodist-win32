#
# 
#
"""This module offers basic data types used by Windows to define function
return values, function and message parameters, and structure members.
They define the size and meaning of these elements. For more information,
consult the underlying C/C++ documentation.
"""
from __future__ import annotations
import ctypes
import ctypes.wintypes
import enum


# Windows data types ===============================================
# BOOL ----------------------------------------------------
BOOL = ctypes.wintypes.BOOL
"""##### typedef int BOOL;
A Boolean variable (should be True or False).
"""
# BYTE ----------------------------------------------------
BYTE = ctypes.wintypes.BYTE
"""##### typedef unsigned char BYTE;
A byte (8 bits).
"""
# DWORD ---------------------------------------------------
DWORD = ctypes.wintypes.DWORD
"""##### typedef unsigned long DWORD;
A 32-bit unsigned integer. The range is 0 through 4,294,967,295 decimal.
"""
# LCID ----------------------------------------------------
LCID = ctypes.wintypes.LCID
"""##### typedef DWORD LCID;
A locale identifier.
"""
# PDWORD --------------------------------------------------
PDWORD = ctypes.POINTER(DWORD)
"""##### typedef DWORD *PDWORD;
A pointer to a DWORD."""
# DWORD_PTR -----------------------------------------------
DWORD_PTR = DWORD
"""##### typedef ULONG_PTR DWORD_PTR;
An unsigned long type for pointer precision. Use when casting a
pointer to a long type to perform pointer arithmetic. (Also commonly
used for general 32-bit parameters that have been extended to 64 bits
in 64-bit Windows.)
"""
# INT -----------------------------------------------------
INT = ctypes.wintypes.INT
"""##### typedef int INT;
A 32-bit signed integer. The range is -2,147,483,648 through 2,147,483,647
decimal.
"""
# SHORT ---------------------------------------------------
SHORT = ctypes.wintypes.SHORT
"""##### typedef short SHORT;
A 16-bit integer. The range is -32,768 through 32,767 decimal.
"""
# UINT ----------------------------------------------------
UINT = ctypes.wintypes.UINT
"""##### typedef unsigned int UINT;
An unsigned INT. The range is 0 through 4,294,967,295 decimal."""
# ULONG ---------------------------------------------------
ULONG = ctypes.wintypes.ULONG
"""##### typedef unsigned long ULONG;
An unsigned LONG. The range is 0 through 4,294,967,295 decimal."""
# USHORT --------------------------------------------------
USHORT = ctypes.wintypes.USHORT
"""##### typedef unsigned short USHORT;
An unsigned SHORT. The range is 0 through 65,535 decimal.
"""
# WCHAR ---------------------------------------------------
WCHAR = ctypes.wintypes.WCHAR
"""##### typedef wchar_t WCHAR;
A 16-bit Unicode character."""


# Windows pointer types =============================================
# LPCWSTR -------------------------------------------------
LPCWSTR = ctypes.wintypes.LPCWSTR
"""#ifdef UNICODE
 typedef LPCWSTR LPCTSTR; 
#else
 typedef LPCSTR LPCTSTR;
#endif

A pointer to a constant null-terminated string of 16-bit Unicode
characters.
"""
# LPCWSTR -------------------------------------------------
LPWSTR = ctypes.wintypes.LPWSTR
"""##### typedef WCHAR *LPWSTR;
A pointer to a null-terminated string of 16-bit Unicode characters.
"""
# PSHORT, LPSHORT, LP_SHORT -------------------------------
PSHORT = ctypes.POINTER(SHORT)
"""##### typedef SHORT *PSHORT;
A pointer to a SHORT.
"""
LPSHORT = PSHORT
"""A pointer to a SHORT."""
LP_SHORT = PSHORT
"""A pointer to a SHORT."""
# PUINT, LPUINT, LP_UINT ----------------------------------
PUINT = ctypes.POINTER(UINT)
"""##### typedef UINT *PUINT;
A pointer to a UINT."""
LPUINT = PUINT
"""A pointer to a UINT."""
LP_UINT = PUINT
"""A pointer to a UINT."""
# PULONG, LPULONG, LP_ULONG -------------------------------
PULONG = ctypes.POINTER(ULONG)
"""##### typedef ULONG *PULONG;
A pointer to a ULONG."""
LPULONG = PULONG
"""A pointer to a ULONG."""
LP_ULONG = PULONG
"""A pointer to a ULONG."""

# Windows HANDLE types ==============================================
# HANDLE --------------------------------------------------
HANDLE = ctypes.wintypes.HANDLE
"""##### typedef PVOID HANDLE;
A handle to an object.
"""
# HRESULT -------------------------------------------------
HRESULT = ctypes.HRESULT
"""##### typedef LONG HRESULT;
The return codes used by COM interfaces."""
# HWND ----------------------------------------------------
HWND = HANDLE
"""##### typedef HANDLE HWND;
A handle to a window.
"""
# HICON ---------------------------------------------------
HICON = ctypes.wintypes.HICON
"""##### typedef HANDLE HICON;
A handle to an icon."""


# Enumearations =====================================================
class DwordFlag(enum.IntFlag):
    @classmethod
    def from_param(cls, obj):
        return DWORD(obj)

class UintFlag(enum.IntFlag):
    @classmethod
    def from_param(cls, obj):
        return UINT(obj)


class UlongFlag(enum.IntFlag):
    @classmethod
    def from_param(cls, obj):
        return ULONG(obj)
