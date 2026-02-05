from app.components import Component
from app.components.lib.chart import Chart
from app.components.lib.indicator.quad_bar import QuadBar
from app.data import telemetry
from app.lib.stats import MovingAverage


class _TyreSlipRatioMonitor:
    def __init__(
        self,
        i_slipRatio: int,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        self._i_slipRatio = i_slipRatio
        self._slipRatio = MovingAverage(scale=3.0)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color4f=(0, 0, 0, 0.0),
            axis_segment_count=4,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.2,
            bg_char='S',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
            centered_y_scale=True,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        slipRatio = telemetry.slipRatio[self._i_slipRatio]

        # updadte buffer
        self._slipRatio.update(slipRatio)

        # plot the indicators
        self._quad_bar.plot(self._slipRatio.weighted_average)


class SlipRatioMonitor(Component):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        self._tyres_slip_ratio_monitors = [
            _TyreSlipRatioMonitor(
                i_slipRatio=i,
                x_pos=_x_pos,
                y_pos=_y_pos,
                width=width//2,
                height=height//2,
            )
            for i, (_x_pos, _y_pos) in enumerate((
                (x_pos, y_pos),
                (x_pos+width//2, y_pos),
                (x_pos, y_pos+height//2),
                (x_pos+width//2, y_pos+height//2),
            ))
        ]

    def render(self) -> None:
        for monitor in self._tyres_slip_ratio_monitors:
            monitor.render()
