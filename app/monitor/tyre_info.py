import config

from ..lib.color import *
from ..telemetry import ac_mem
from ._base import Component, Monitor
from .lib.canvas import Chart, Region
from .lib.text import BigText


class _TyreMonitor(Component):
    def __init__(
        self,
        i: int,
        name: str,
        region: Region,
    ) -> None:
        self._i = i

        self._region = region
        # BigText(self._region, name, white.a1, 5, 'center')
        self._temperature_text = BigText(
            region=self._region.top,
            text='',
            font_color=white.full,
            expected_text_len=3,
        )
        BigText(self._region.top.right.right, '°c', white.a7, 3, 'left')
        self._pressure_text = BigText(
            region=self._region.bottom,
            text='',
            font_color=white.full,
            expected_text_len=3,
        )
        BigText(self._region.bottom.right.right, 'psi', white.a7, 3, 'left')

    def render(self) -> None:
        # fetch telemetry
        temperature = ac_mem.physics.tyreCoreTemperature[self._i]  # type: float
        pressure = ac_mem.physics.wheelsPressure[self._i]  # type: float

        # plot the indicators
        temperature_text = str(round(temperature, 1))
        self._temperature_text.expected_text_len = len(temperature_text)-1
        self._temperature_text.text = temperature_text
        pressure_text = str(round(pressure, 1))
        self._pressure_text.expected_text_len = len(pressure_text)-1
        self._pressure_text.text = pressure_text


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
        self._chart = Chart(
            self._region,
            x_axis_color=white.a7,
            y_axis_color=white.a7,
        )
        self._tyre_monitors = [
            _TyreMonitor(i, name, region)
            for i, (name, region) in enumerate((
                ('FL', self._region.top_left),
                ('FR', self._region.top_right),
                ('RL', self._region.bottom_left),
                ('RR', self._region.bottom_right),
            ))
        ]

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def render(self) -> None:
        self._chart.draw_axes()
        for monitor in self._tyre_monitors:
            monitor.render()
