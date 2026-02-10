from ._base import Monitor
from .gear import GearMonitor
from .gforce import GForceMonitor
from .pedals import PedalsMonitor
from .slip_angle import SlipAngleMonitor
from .slip_ratio import SlipRatioMonitor
from .speed import SpeedMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    SlipRatioMonitor,
    SpeedMonitor,
    GearMonitor,
    PedalsMonitor,
    SlipAngleMonitor,
)  # type: tuple[type[Monitor], ...]

__all__ = [
    'Monitor',
    'GForceMonitor',
    'SlipRatioMonitor',
    'SpeedMonitor',
    'GearMonitor',
    'PedalsMonitor',
    'SlipAngleMonitor',
    'MONITOR_CLASSES',
]
