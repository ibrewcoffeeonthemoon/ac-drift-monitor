from acsys import CS

import config

from ...lib.color import *
from ...lib.number import num
from ...telemetry import ac_api
from .._base import Component, Monitor
from ..lib.chart import Chart
from ..lib.indicator import QuadBar

_specs = (
    (blue.a5, CS.Clutch, True),
    (red.a5, CS.Brake, False),
    (green.a5, CS.Gas, False),
    (yellow.a5, CS.TurboBoost, False),
)


class _PedalMonitor(Component):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        color: Color,
        data_key: int,
        inverted: bool,
    ) -> None:
        self._color = color
        self._data_key = data_key
        self._inverted = inverted
        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color=white.transparent,
            axis_segment_count=8,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.4,
            bg_char='',
        )
        self._bar = QuadBar(
            chart=self._chart,
            color=self._color,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac_api[self._data_key].last[0]

        # plot the indicators
        val = 1-val if self._inverted else val
        self._bar.plot(
            num(val).clip(0, 1).f
        )


class PedalsMonitor(Monitor):
    data_keys = tuple(m[1] for m in _specs)
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

        dt = width//len(_specs)
        self._components = [
            _PedalMonitor(
                x_pos+i*dt, 0, dt, height,
                color, data_key, inverted
            )
            for i, (color, data_key, inverted) in enumerate(_specs)
        ]  # type: list[Component]

    @property
    def width(self) -> int: return self._width
    @property
    def height(self) -> int: return self._height

    def render(self) -> None:
        for component in self._components:
            component.render()
