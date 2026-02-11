from ....lib.color import *
from ..chart import Chart
from ..gl.line import line
from ._base import AngleIndicator


class AngleLine(AngleIndicator):
    def __init__(
        self,
        chart: Chart,
        color: Color = yellow.full,
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = False,
        centered_x_scale: bool = False,
        centered_y_scale: bool = False,
    ) -> None:
        super().__init__(
            chart=chart,
            inverted_x_scale=inverted_x_scale,
            inverted_y_scale=inverted_y_scale,
            centered_x_scale=centered_x_scale,
            centered_y_scale=centered_y_scale,
        )
        self._color = color

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        line(
            *self._edge_intercepts(val),
            color=color or self._color
        )
