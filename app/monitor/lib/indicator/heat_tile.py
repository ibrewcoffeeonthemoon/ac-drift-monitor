from app.lib.color import *
from app.lib.number import num
from app.monitor.lib.canvas import Region
from app.monitor.lib.gl.shape import rectangle

from ._base import Indicator


class HeatTile(Indicator):
    def __init__(
        self,
        region: Region,
        low: float,
        high: float,
        alpha: float = 0.2,
        midpoint: float = 0.5,
    ) -> None:
        super().__init__(region=region)
        self._low = low
        self._high = high
        self._alpha = alpha
        self._midpoint = midpoint
        self._scale = high-low

    def _green_yellow_red_scale(self, val: float) -> Color:
        val = num(val).shift(-self._low).normalize(self._scale).clip(0, 1).f
        r = val*2 if val < self._midpoint else 1.0
        g = 1.0 if val < self._midpoint else 1.0 - ((val-self._midpoint)*2)
        b = 0.0
        return Color(r, g, b, self._alpha)

    def plot(self, val: float) -> None:
        color = self._green_yellow_red_scale(val)
        rectangle(
            self._region.corner_top_left,
            self._width,
            self._height,
            color,
        )
