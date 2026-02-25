from acsys import CS

from app.lib.color import *

from ._base import Pedal


class TurboBoostPedal(Pedal):
    color = yellow.a5
    data_key = CS.TurboBoost
