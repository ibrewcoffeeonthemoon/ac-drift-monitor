from ._base import Monitor
from .gforce import GForceMonitor
from .slip_ratio import SlipRatioMonitor
from .speed import SpeedMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    SlipRatioMonitor,
    SpeedMonitor,
)  # type: tuple[type[Monitor], ...]

__all__ = [
    'Monitor',
    'GForceMonitor',
    'SlipRatioMonitor',
    'SpeedMonitor',
    'MONITOR_CLASSES',
]
