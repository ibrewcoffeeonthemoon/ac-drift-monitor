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
        line_height = 6
        self._line = Rectangle(
            x_pos=x_pos,
            y_pos=y_pos+height//2-line_height//2,
            width=width,
            height=line_height,
        )

        # create indicators
        self._latG = Indicator(
            x_pos=x_pos,
            y_pos=y_pos+62,
            max_value=1.5,
            bar_len=width,
            name="Lat.",
        )
        self._longG = Indicator(
            x_pos=x_pos,
            y_pos=y_pos+136,
            max_value=1.5,
            bar_len=width,
            name="Lon.",
            arrow_on_top=False
        )

    def render(self) -> None:
        self._line.render()
        self._latG.value, _, self._longG.value = telemetry.accG
