import config

from ..lib.color import *
from ..telemetry import ac_mem
from ._base import Component, Monitor
from .lib.canvas import Region
from .lib.text import BigText


class _TyreMonitor(Component):
    def __init__(
        self,
        i: int,
        region: Region,
    ) -> None:
        self._i = i

        self._region = region
        self._temperature_text = BigText(
            region=self._region.top,
            text='',
            font_color=white.full,
            expected_text_len=4,
        )
        BigText(self._region.top.right.right, '°c', white.a7, 3, 'left')
        self._pressure_text = BigText(
            region=self._region.bottom,
            text='',
            font_color=white.full,
            expected_text_len=4,
        )
        BigText(self._region.bottom.right.right, 'psi', white.a7, 3, 'left')

    def render(self) -> None:
        # fetch telemetry
        temperature = ac_mem.physics.tyreCoreTemperature[self._i]  # type: float
        pressure = ac_mem.physics.wheelsPressure[self._i]  # type: float

        # plot the indicators
        self._temperature_text.text = str(round(temperature, 1))
        self._pressure_text.text = str(round(pressure, 1))


class TyreInfoMonitor(Monitor):
    data_keys = ()
    enabled = config.TyreInfoMonitor.enabled
    col_index = config.TyreInfoMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.TyreInfoMonitor.col_span
        self._height = height = config.App.height
        self._region = Region(x_pos, y_pos, width, height)

        self._tyre_monitors = [
            _TyreMonitor(i, region)
            for i, region in enumerate((
                self._region.top_left,
                self._region.top_right,
                self._region.bottom_left,
                self._region.bottom_right,
            ))
        ]

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def render(self) -> None:
        for monitor in self._tyre_monitors:
            monitor.render()
