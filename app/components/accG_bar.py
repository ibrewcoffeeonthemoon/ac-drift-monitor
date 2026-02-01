from app.components.lib.indicator import Indicator
from app.components.lib.rectangle import Rectangle
from app.data import telemetry


class AccG_Bar:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        # shapes
        self._line = Rectangle(x_pos, y_pos+height//2, width, 5)

        # create indicators
        self._latG = Indicator(
            x_pos=22,
            y_pos=62,
            max_value=1.5,
            name="Lat.",
        )
        self._longG = Indicator(
            x_pos=22,
            y_pos=136,
            max_value=1.5,
            name="Lon.",
            arrow_on_top=False
        )

    def render(self) -> None:
        self._line.render()
        self._latG.value, _, self._longG.value = telemetry.accG
