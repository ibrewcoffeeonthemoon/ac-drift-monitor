from abc import ABCMeta, abstractmethod

from ..canvas import Region


class Indicator(metaclass=ABCMeta):
    def __init__(
        self,
        region: Region,
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = False,
        centered_x_scale: bool = False,
        centered_y_scale: bool = False,
    ) -> None:
        self._region = region
        self._x_pos = x_pos = region.x_pos
        self._y_pos = y_pos = region.y_pos
        self._width = width = region.width
        self._height = height = region.height
        self._inverted_x_scale = inverted_x_scale
        self._inverted_y_scale = inverted_y_scale
        self._centered_x_scale = centered_x_scale
        self._centered_y_scale = centered_y_scale

        # beginning coordinates
        self._begin = (
            x_pos+width/2 if centered_x_scale else x_pos+width if inverted_x_scale else x_pos,
            y_pos+height/2 if centered_y_scale else y_pos if inverted_y_scale else y_pos+height,
        )
        # magnitude of coordinate offset if value is 100%
        self._magnitude = (
            width/2 if centered_x_scale else width,
            height/2 if centered_y_scale else height,
        )
        # direction factor (y scale is flipped to convert from monitor direction to human direction)
        self._direction = (
            -1 if self._inverted_x_scale else +1,
            +1 if self._inverted_y_scale else -1,
        )

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...
