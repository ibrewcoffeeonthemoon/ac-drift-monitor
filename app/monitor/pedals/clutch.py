from acsys import CS

from app.lib.color import *
from app.lib.number import num
from app.telemetry import ac_api

from ._base import Pedal


class ClutchPedal(Pedal):
    color = blue.a5
    data_key = CS.Clutch

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac_api[self.data_key].last[0]

        # plot the indicators
        self._bar.plot(
            num(1-val).clip(0, 1).f
        )
