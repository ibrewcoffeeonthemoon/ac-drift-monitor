from ._base import Component
from .gforce_monitor import GForceMonitor
from .slip_ratio_monitor import SlipRatioMonitor
from .speed_monitor import SpeedMonitor

MONITOR_CLASSES = (
    GForceMonitor,
    SlipRatioMonitor,
    SpeedMonitor,
)  # type: tuple[type[Component], ...]

__all__ = [
    'Component',
    'GForceMonitor',
    'SlipRatioMonitor',
    'SpeedMonitor',
    'MONITOR_CLASSES',
]
