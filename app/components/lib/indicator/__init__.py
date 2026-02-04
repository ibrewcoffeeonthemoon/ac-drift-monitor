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
        self._x_pos = self._chart.x_pos
        self._y_pos = self._chart.y_pos
        self._width = self._chart.width
        self._height = self._chart.height
        self._inverted_x_scale = inverted_x_scale
        self._inverted_y_scale = inverted_y_scale
        self._centered_x_scale = centered_x_scale
        self._centered_y_scale = centered_y_scale

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...

    @property
    def _begin(self):
        # type: () -> tuple[int, int]
        x = self._x_pos+self._width//2 if self._centered_x_scale \
            else self._x_pos+self._width if self._inverted_x_scale else self._x_pos
        y = self._y_pos+self._height//2 if self._centered_y_scale \
            else self._y_pos+self._height if self._inverted_y_scale else self._y_pos
        return x, y

    @property
    def _magnitude(self):
        # type: () -> tuple[int, int]
        x = self._width//2 if self._centered_x_scale else self._width
        y = self._height//2 if self._centered_y_scale else self._height
        return x, y

    @property
    def _direction(self):
        # type: () -> tuple[int, int]
        x = -1 if self._inverted_x_scale else 1
        y = -1 if self._inverted_y_scale else 1
        return x, y
