import ac
from acsys import CS

from ...lib.color import *
from ...lib.number import num
from ._base import Pedal


class HandbrakePedal(Pedal):
    color = cyan.a5
    data_key = CS.Brake  # dummy

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac.ext_getHandbrake(0)  # type: float

        # plot the indicators
        self._bar.plot(
            num(val).clip(0, 1).f
        )
