from ..chart import Chart
from ..gl.shape import quadrilateral
from ._base import Indicator


class QuadBar(Indicator):
    def __init__(
        self,
        chart: Chart,
        color4f: 'tuple[float, float, float, float]' = (1, 0, 0, 1),
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
        self._color4f = color4f

    def _coordinates(self, val: float) -> 'tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]':
        x_begin, y_begin = self._begin
        x_mag, y_mag = self._magnitude
        x_dir, y_dir = self._direction
        return (
            (self._x_pos, round(y_begin + val*y_mag*y_dir)),
            (self._x_pos+self._width, round(y_begin + val*y_mag*y_dir)),
            (self._x_pos+self._width, y_begin),
            (self._x_pos, y_begin),
        )

    def plot(self, val: float, color4f: 'tuple[float, float, float, float] | None' = None) -> None:
        quadrilateral(
            *self._coordinates(val),
            color4f=color4f or self._color4f
        )
