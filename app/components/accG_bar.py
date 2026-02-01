import ac

from app.components.lib.indicator import Indicator
from app.data import telemetry
from app.window import window


class AccG_Bar:
    bg_img_path = 'apps/python/ac-drift-monitor/assets/bg.png'

    def __init__(self) -> None:
        # set layouts, styles
        ac.setBackgroundTexture(window, self.bg_img_path)

        # create indicators
        self._latG = Indicator(
            window,
            x_pos=22,
            y_pos=62,
            max_value=1.5,
            name="Lat.",
        )
        self._longG = Indicator(
            window,
            x_pos=22,
            y_pos=136,
            max_value=1.5,
            name="Lon.",
            arrow_on_top=False
        )

    def render(self) -> None:
        # set indicator values
        self._latG.value, _, self._longG.value = telemetry.accG
