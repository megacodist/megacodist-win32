#
# 
#
"""This header is used by multiple technologies. For more information, see:

* The Windows Shell
* Windows Property System
"""
import ctypes

# Windows data types ======================================
from win_basic_types import DWORD
from win_basic_types import HICON
from win_basic_types import INT
from win_basic_types import WCHAR


class SHFILEINFOW(ctypes.Structure):
    """Contains information about a file object."""
    _fields_ = [
        ('hIcon', HICON,),
        ('iIcon', INT,),
        ('dwAttributes', DWORD,),
        ('szDisplayName', (WCHAR * 260),),
        ('szTypeName', (WCHAR * 80),),]
    
    @property
    def hIcon(self) -> HICON:
        """A handle to the icon that represents the file. You are
        responsible for destroying this handle with shell32.DestroyIcon
        when you no longer need it.
        """
        return self.hIcon
    
    @property
    def iIcon(self) -> INT:
        """The index of the icon image within the system image list."""
        return self.iIcon
    
    @property
    def dwAttributes(self) -> DWORD:
        """An array of values that indicates the attributes of the file
        object.
        """
        return self.dwAttributes
    
    @property
    def szDisplayName(self) -> str:
        """A string that contains the name of the file as it appears in
        the Windows Shell, or the path and file name of the file that
        contains the icon representing the file.
        """
        return self.szDisplayName
    
    @property
    def szTypeName(self) -> str:
        """A string that describes the type of file."""
        return self.szTypeName


LP_SHFILEINFOW = ctypes.POINTER(SHFILEINFOW)
"""A pointer to a SHFILEINFO structure to receive the file information."""
