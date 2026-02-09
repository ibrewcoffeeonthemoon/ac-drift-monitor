from ._base import Monitor
from .gear import GearMonitor
from .gforce import GForceMonitor
from .slip_ratio import SlipRatioMonitor
from .speed import SpeedMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    SlipRatioMonitor,
    SpeedMonitor,
    GearMonitor,
)  # type: tuple[type[Monitor], ...]

__all__ = [
    'Monitor',
    'GForceMonitor',
    'SlipRatioMonitor',
    'SpeedMonitor',
    'GearMonitor',
    'MONITOR_CLASSES',
]
