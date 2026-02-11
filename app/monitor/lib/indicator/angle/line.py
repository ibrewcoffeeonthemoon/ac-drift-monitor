from .....lib.color import *
from ...gl.line import line
from ._base import AngleIndicator


class AngleLine(AngleIndicator):
    def plot(self, val: float, color: 'Color | None' = None) -> None:
        val = val * self._scale
        val = -val if self._reversed else val
        line(
            *self._edge_intercepts(val),
            color=color or self._color
        )
