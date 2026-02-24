from abc import ABCMeta, abstractmethod

import ac

from app.lib.color import Color
from app.lib.geometry import Position, Size
from app.window import window


class Text(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        self._label = ac.addLabel(window, '')

    ''''''
    @property
    def text(self) -> 'str | None':
        return self._text

    @text.setter
    def text(self, val: str) -> None:
        self._text = val
        ac.setText(self._label, val)

    ''''''
    @property
    def font_size(self) -> 'int | None':
        return self._font_size

    @font_size.setter
    def font_size(self, val: int) -> None:
        self._font_size = val
        ac.setFontSize(self._label, val)

    ''''''
    @property
    def font_color(self) -> 'Color | None':
        return self._font_color

    @font_color.setter
    def font_color(self, val: Color) -> None:
        self._font_color = val
        ac.setFontColor(self._label, val.r, val.g, val.b, val.a)

    ''''''
    @property
    def font_alignment(self) -> 'str | None':
        return self._font_alignment

    @font_alignment.setter
    def font_alignment(self, val: str) -> None:
        self._font_alignment = val
        ac.setFontAlignment(self._label, val)

    ''''''
    @property
    def size(self) -> 'Size | None':
        return self._size

    @size.setter
    def size(self, val: Size) -> None:
        self._size = val
        ac.setSize(self._label, val.width, val.height)

    ''''''
    @property
    def position(self) -> 'Position | None':
        return self._position

    @position.setter
    def position(self, val: Position) -> None:
        self._position = val
        ac.setPosition(self._label, val.x_pos, val.y_pos)
