from acsys import CS

from ...lib.color import *
from ...lib.number import num
from ...telemetry import ac_api
from ._base import PedalMonitor


class ClutchPedal(PedalMonitor):
    color = blue.a5
    data_key = CS.Clutch

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        super().__init__(
            x_pos,
            y_pos,
            width,
            height,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac_api[self.data_key].last[0]

        # plot the indicators
        self._bar.plot(
            num(1-val).clip(0, 1).f
        )
