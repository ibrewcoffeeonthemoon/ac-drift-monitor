from ....lib.color import Color
from ....lib.geometry import Position, Size
from ....lib.number import num
from ..canvas.region import Region
from ._base import Text


class BigText(Text):
    def __init__(
        self,
        region: Region,
        text: str,
        font_color: Color,
        expected_text_len: int,
    ) -> None:
        super().__init__()
        self._x_pos = region.x_pos
        self._y_pos = region.y_pos
        self._width = region.width
        self._height = region.height
        self._expected_text_len = None  # type: 'int | None'
        # init label
        self.text = text
        self.font_color = font_color
        self.font_alignment = 'center'
        self.size = Size(self._width, self._height)
        self.expected_text_len = expected_text_len

    @property
    def _shrink_factor(self) -> float:
        if not self.expected_text_len:
            return 1.0
        return num(1.0 - (self.expected_text_len - 1) * 0.25).clip(0.5, 1.0).f

    @property
    def expected_text_len(self) -> 'int | None':
        return self._expected_text_len

    @expected_text_len.setter
    def expected_text_len(self, val: int) -> None:
        if self._expected_text_len == val:
            return
        self._expected_text_len = val
        # consequential adjustments
        self.font_size = round(min(self._width, self._height)*self._shrink_factor)
        vertical_offset = round(self._height/2-self._font_size*3/4)
        self.position = Position(self._x_pos, self._y_pos+vertical_offset)


def big_text(
    region: Region,
    text: str,
    font_color: Color,
    expected_text_len: int,
) -> BigText:
    return BigText(
        region,
        text=text,
        font_color=font_color,
        expected_text_len=expected_text_len,
    )
