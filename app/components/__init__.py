from ._base import Component
from .gforce import GForceMonitor
from .slip_ratio import SlipRatioMonitor
from .speed import SpeedMonitor

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
