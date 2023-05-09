from ctypes import byref, sizeof, POINTER

from shellapi import LP_SHFILEINFOW, SHFILEINFOW
from shell32 import SHGetFileInfoW, SHGFI
from user32 import DestroyIcon
from winnt import FILE_ATTRIBUTE


def main() -> None:
    filename = input("Specify a file: ")
    psfi = SHFILEINFOW()
    SHGetFileInfoW(
        filename,
        0,
        byref(psfi),
        sizeof(psfi),
        SHGFI.USEFILEATTRIBUTES | SHGFI.TYPENAME | SHGFI.DISPLAYNAME)

    print(psfi.hIcon)
    print(psfi.iIcon)
    print(psfi.dwAttributes)
    print(psfi.szDisplayName)
    print(psfi.szTypeName)
    if psfi.hIcon:
        DestroyIcon(psfi.hIcon)


if __name__ == '__main__':
    main()
