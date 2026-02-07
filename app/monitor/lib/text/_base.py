import ac

from ....window import window


class Text:
    def __init__(
        self,
        text: str,
        font_size: int,
        font_color: 'tuple[float, float, float, float]',
        font_alignment: str,
        size: 'tuple[int, int]',
        position: 'tuple[int, int]',
    ) -> None:
        self._label = ac.addLabel(window, text)
        self.text = text
        self.size = size
        self.position = position
        self.font_size = font_size
        self.font_color = font_color
        self.font_alignment = font_alignment

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, val: str) -> None:
        self._text = val
        ac.setText(self._label, val)

    @property
    def font_size(self) -> int:
        return self._font_size

    @font_size.setter
    def font_size(self, val: int) -> None:
        self._font_size = val
        ac.setFontSize(self._label, val)

    @property
    def font_color(self) -> 'tuple[float, float, float, float]':
        return self._font_color

    @font_color.setter
    def font_color(self, val: 'tuple[float, float, float, float]') -> None:
        self._font_color = val
        ac.setFontColor(self._label, *val)

    @property
    def font_alignment(self) -> str:
        return self._font_alignment

    @font_alignment.setter
    def font_alignment(self, val: str) -> None:
        self._font_alignment = val
        ac.setFontAlignment(self._label, val)

    @property
    def size(self) -> 'tuple[int, int]':
        return self._size

    @size.setter
    def size(self, val: 'tuple[int, int]') -> None:
        self._size = val
        ac.setSize(self._label, *val)

    @property
    def position(self) -> 'tuple[int, int]':
        return self._position

    @position.setter
    def position(self, val: 'tuple[int, int]') -> None:
        self._position = val
        ac.setPosition(self._label, *val)
