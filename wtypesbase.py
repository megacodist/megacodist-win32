#
# Copyright notice in here.
#
"""This header is used by multiple technologies. For more information, see:

Component Object Model (COM)
Windows Sockets 2
"""
import ctypes

# Windows types =====================================================
from win_basic_types import DWORD, PSHORT
from win_basic_types import ULONG, LPWSTR


class COAUTHIDENTITY(ctypes.Structure):
   """Contains a user name and password."""
   _fields_ = [
      ('User', PSHORT),
      ('UserLength', ULONG),
      ('Domain', PSHORT),
      ('DomainLength', ULONG),
      ('Password', PSHORT),
      ('PasswordLength', ULONG),
      ('Flags', ULONG)]


LP_COAUTHIDENTITY = ctypes.POINTER(COAUTHIDENTITY)
"""A pointer to a COAUTHIDENTITY."""


class COAUTHINFO(ctypes.Structure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pwszServerPrincName', LPWSTR),
        ('dwAuthnLevel', DWORD),
        ('dwImpersonationLevel', DWORD),
        ('pAuthIdentityData', LP_COAUTHIDENTITY),
        ('dwCapabilities', DWORD)]


LP_COAUTHINFO = ctypes.POINTER(COAUTHINFO)
"""A pointer to COAUTHINFO."""
