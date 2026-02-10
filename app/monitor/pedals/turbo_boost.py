from acsys import CS

from ...lib.color import *
from ._base import Pedal


class TurboBoostPedal(Pedal):
    color = yellow.a5
    data_key = CS.TurboBoost

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
