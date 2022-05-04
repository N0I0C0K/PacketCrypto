import sys
from typing import Union
from pydantic import BaseModel

__all__ = ['COLOR', 'set_color','EncryptData']


color_support = True


class EncryptData(BaseModel):
    data: str
    sign: str
    key: str
    nonce: str


class COLOR:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    DEFAULT = '\033[39m'


if sys.platform == "win32":
    try:
        # https://stackoverflow.com/questions/36760127/...
        # how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console
        from ctypes import windll
        kernel32 = windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:  # pragma: no cover
        color_support = False


def set_color(s: str, color: COLOR) -> str:
    if color_support:
        return f"{color}{s}{COLOR.DEFAULT}"
    return s
