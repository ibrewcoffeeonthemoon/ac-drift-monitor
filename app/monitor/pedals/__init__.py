import config

from ...lib.color import *
from .._base import Monitor
from ._base import Pedal
from .brake import BrakePedal
from .clutch import ClutchPedal
from .gas import GasPedal
from .handbrake import HandbrakePedal
from .turbo_boost import TurboBoostPedal

_selected_pedals = (
    ClutchPedal,
    HandbrakePedal,
    BrakePedal,
    GasPedal,
    TurboBoostPedal,
)


class PedalsMonitor(Monitor):
    data_keys = tuple(cls.data_key for cls in _selected_pedals)
    enabled = config.PedalsMonitor.enabled
    col_index = config.PedalsMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self.width = width = config.App.span_len*config.PedalsMonitor.col_span
        self.height = height = config.App.height

        dt = width/len(_selected_pedals)
        self._components = [
            cls(x_pos+i*dt, y_pos, dt, height)
            for i, cls in enumerate(_selected_pedals)
        ]  # type: list[Pedal]

    def render(self) -> None:
        for component in self._components:
            component.render()
