from .....lib.color import *
from ...chart import Chart
from ...gl.line import line
from ._base import AngleIndicator


class AngleLine(AngleIndicator):
    def __init__(
        self,
        chart: Chart,
        color: Color = yellow.full,
    ) -> None:
        super().__init__(chart=chart)
        self._color = color

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        line(
            *self._edge_intercepts(val),
            color=color or self._color
        )
