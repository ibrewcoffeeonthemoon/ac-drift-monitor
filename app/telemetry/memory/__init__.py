import os
import platform
import sys

import ac


def _init1():
    app_dir = os.path.dirname(__file__)
    sysdir = os.path.join(app_dir, 'dll', 'stdlib64')
    sys.path.insert(0, sysdir)
    os.environ['PATH'] = os.environ['PATH'] + ";."
    ac.log(sysdir)
    # print: apps/python/ac-drift-monitor\app\telemetry\memory\dll\stdlib64
    from .lib.sim_info import info
    return info


def _init2():
    app_dir = os.path.dirname(__file__)

    if platform.architecture()[0] == "64bit":
        sysdir = os.path.join(app_dir, 'dll', 'stdlib64')
    else:
        sysdir = os.path.join(app_dir, 'dll', 'stdlib')
    # Python looks in sys.path for modules to load, insert new dir first in line.
    sys.path.insert(0, sysdir)
    os.environ['PATH'] = os.environ['PATH'] + ";."

    ac.log(sysdir)
    # print: apps/python/ac-drift-monitor\app\telemetry\memory\dll\stdlib64

    from .lib.sim_info import info

    return info


info = _init1()


class Memory:
    @property
    def maxRpm(self) -> int:
        return info.static.maxRpm
