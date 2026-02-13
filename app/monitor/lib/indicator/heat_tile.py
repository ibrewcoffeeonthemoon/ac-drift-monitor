from ....lib.color import *
from ....lib.number import num
from ..canvas import Region
from ..gl.shape import rectangle
from ._base import Indicator


class HeatTile(Indicator):
    def __init__(
        self,
        region: Region,
        low: float,
        high: float,
        alpha: float = 0.2,
    ) -> None:
        super().__init__(region=region)
        self._low = low
        self._high = high
        self._alpha = alpha
        self._scale = high-low

    def _green_yellow_red_scale(self, val: float) -> Color:
        val = num(val).shift(-self._low).normalize(self._scale).clip(0, 1).f
        if val < 0.5:
            # First half: Green (0,1,0) to Yellow (1,1,0)
            # We multiply by 2 because the transition happens over 0.5 units
            r = val * 2.0
            g = 1.0
        else:
            # Second half: Yellow (1,1,0) to Red (1,0,0)
            r = 1.0
            g = 1.0 - ((val - 0.5) * 2.0)

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
