from app.components.lib.indicator import Indicator
from app.data import Telemetry


class AccG_Bar:
    def __init__(
        self,
        win: int,
        telemetry: Telemetry,
    ) -> None:
        self.telemetry = telemetry

        # create indicators
        self._latG = Indicator(
            win,
            x_pos=22,
            y_pos=62,
            max_value=1.5,
            name="Lat.",
        )
        self._longG = Indicator(
            win,
            x_pos=22,
            y_pos=136,
            max_value=1.5,
            name="Lon.",
            arrow_on_top=False
        )

    def render(self) -> None:
        # set indicator values
        self._latG.value, _, self._longG.value = self.telemetry.accG
