import os
import platform
import sys

_app_dir = os.path.dirname(os.path.abspath(__file__))
_dll_dir_32 = os.path.join(_app_dir, 'dll', 'stdlib')
_dll_dir_64 = os.path.join(_app_dir, 'dll', 'stdlib64')
_dll_dir = _dll_dir_64 if platform.architecture()[0] == '64bit' else _dll_dir_32
sys.path.insert(0, _dll_dir)

# append dll_dir before this import
from .sim_info import info as memory  # noqa: no auto sorting

__all__ = [
    'memory',
]
