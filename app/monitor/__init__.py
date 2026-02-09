from ._base import Monitor
from .gear import GearMonitor
from .gforce import GForceMonitor
from .pedals import PedalsMonitor
from .slip_ratio import SlipRatioMonitor
from .speed import SpeedMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    SlipRatioMonitor,
    SpeedMonitor,
    GearMonitor,
    PedalsMonitor,
)  # type: tuple[type[Monitor], ...]

__all__ = [
    'Monitor',
    'GForceMonitor',
    'SlipRatioMonitor',
    'SpeedMonitor',
    'GearMonitor',
    'PedalsMonitor',
    'MONITOR_CLASSES',
]
