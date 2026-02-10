import config

from ...lib.color import *
from .._base import Monitor
from ._base import PedalMonitor
from .brake import BrakePedal
from .clutch import ClutchPedal
from .gas import GasPedal
from .turbo_boost import TurboBoostPedal

_selected_pedals = (
    ClutchPedal,
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
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.PedalsMonitor.col_span
        self._height = height = config.App.height

        dt = width//len(_selected_pedals)
        self._components = [
            cls(x_pos+i*dt, y_pos, dt, height)
            for i, cls in enumerate(_selected_pedals)
        ]  # type: list[PedalMonitor]

    @property
    def width(self) -> int: return self._width
    @property
    def height(self) -> int: return self._height

    def render(self) -> None:
        for component in self._components:
            component.render()
