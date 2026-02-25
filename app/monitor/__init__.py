from ._base import Monitor
from .gear import GearMonitor
from .gforce import GForceMonitor
from .pedals import PedalsMonitor
from .slip_angle import SlipAngleMonitor
from .speed import SpeedMonitor
from .tyre_info import TyreInfoMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    TyreInfoMonitor,
    SlipAngleMonitor,
    SpeedMonitor,
    GearMonitor,
    PedalsMonitor,
)  # type: tuple[type[Monitor], ...]

__all__ = [
    'Monitor',
    'GForceMonitor',
    'TyreInfoMonitor',
    'SlipAngleMonitor',
    'SpeedMonitor',
    'GearMonitor',
    'PedalsMonitor',
    'MONITOR_CLASSES',
]
