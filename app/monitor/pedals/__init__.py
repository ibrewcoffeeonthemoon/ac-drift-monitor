from acsys import CS

import config

from ...lib.color import *
from .._base import Monitor
from ._base import PedalMonitor
from .brake import BrakePedal
from .clutch import ClutchPedal
from .gas import GasPedal
from .turbo_boost import TurboBoostPedal

# _specs = (
#     (blue.a5, CS.Clutch, True),
#     (red.a5, CS.Brake, False),
#     (green.a5, CS.Gas, False),
#     (yellow.a5, CS.TurboBoost, False),
# )


class PedalsMonitor(Monitor):
    # data_keys = tuple(m[1] for m in _specs)
    data_keys = (CS.Clutch, CS.Gas, CS.TurboBoost, CS.Brake)
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

        # dt = width//len(_specs)
        # self._components = [
        #     PedalMonitor(
        #         x_pos+i*dt, 0, dt, height,
        #         color, data_key, inverted
        #     )
        #     for i, (color, data_key, inverted) in enumerate(_specs)
        # ]  # type: list[Component]
        self._components_cls = [
            ClutchPedal, BrakePedal, GasPedal, TurboBoostPedal,
        ]  # type: list[type[PedalMonitor]]
        # self._components = [
        #     ClutchPedal(x_pos+0*dt, 0, dt, height),
        #     BrakePedal(x_pos+1*dt, 0, dt, height),
        #     GasPedal(x_pos+2*dt, 0, dt, height),
        #     TurboBoostPedal(x_pos+3*dt, 0, dt, height),
        # ]  # type: list[PedalMonitor]
        dt = width//len(self._components_cls)
        self._components = [
            cls(x_pos+i*dt, y_pos, dt, height)
            for i, cls in enumerate(self._components_cls)
        ]  # type: list[PedalMonitor]

    @property
    def width(self) -> int: return self._width
    @property
    def height(self) -> int: return self._height

    def render(self) -> None:
        for component in self._components:
            component.render()
