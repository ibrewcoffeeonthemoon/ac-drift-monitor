from abc import ABCMeta, abstractmethod

from app.components.lib.chart import Chart


class Indicator(metaclass=ABCMeta):
    def __init__(
        self,
        chart: Chart,
        inverted_x_scale: bool,
        inverted_y_scale: bool,
        centered_x_scale: bool,
        centered_y_scale: bool,
    ) -> None:
        self._chart = chart
        self._x_pos = x_pos = chart.x_pos
        self._y_pos = y_pos = chart.y_pos
        self._width = width = chart.width
        self._height = height = chart.height
        self._inverted_x_scale = inverted_x_scale
        self._inverted_y_scale = inverted_y_scale
        self._centered_x_scale = centered_x_scale
        self._centered_y_scale = centered_y_scale

        # beginning coordinates
        self._begin = (
            x_pos+width//2 if centered_x_scale else x_pos+width if inverted_x_scale else x_pos,
            y_pos+height//2 if centered_y_scale else y_pos if inverted_y_scale else y_pos+height,
        )
        # magnitude of coordinate offset if value is 100%
        self._magnitude = (
            width//2 if centered_x_scale else width,
            height//2 if centered_y_scale else height,
        )
        # direction factor (y scale is flipped to convert from monitor direction to human direction)
        self._direction = (
            -1 if self._inverted_x_scale else +1,
            +1 if self._inverted_y_scale else -1,
        )

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...
