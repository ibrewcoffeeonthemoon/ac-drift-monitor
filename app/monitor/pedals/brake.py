from acsys import CS

from ...lib.color import *
from ._base import Pedal


class BrakePedal(Pedal):
    color = red.a5
    data_key = CS.Brake
