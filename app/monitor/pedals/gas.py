from acsys import CS

from app.lib.color import *

from ._base import Pedal


class GasPedal(Pedal):
    color = green.a5
    data_key = CS.Gas
