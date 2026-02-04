from app.components.lib.chart import Chart
from app.components.lib.gl.shape import quadrilateral
from app.components.lib.indicator import Indicator


class QuadBar(Indicator):
    def __init__(
        self,
        chart: Chart,
        color4f: tuple = (1, 0, 0, 1),
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = True,
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

    def plot(
        self,
        val: float,
    ) -> None:
        scale = self._height
        quadrilateral(
            (self._x_pos, self._y_pos+self._height-val*scale),
            (self._x_pos+self._width, self._y_pos+self._height-val*scale),
            (self._x_pos+self._width, self._y_pos+self._height),
            (self._x_pos, self._y_pos+self._height),
            color4f=self._color4f,
        )
