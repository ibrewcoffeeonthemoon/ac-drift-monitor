from app.components.lib.indicator import Indicator
from app.components.lib.rectangle import Rectangle
from app.data import telemetry


class AccG_Bar:

    def __init__(self) -> None:
        # shapes
        self._line = Rectangle(0, 99, 333, 5)

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
