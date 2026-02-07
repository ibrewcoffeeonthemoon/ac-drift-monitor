from ._base import Text


class BackgroundBigText(Text):
    def __init__(
        self,
        text: str,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        font_size = min(width, height)
        font_size_vertical_offset = height//2-font_size*3//4
        super().__init__(
            text=text,
            font_size=font_size,
            font_color=(1, 1, 1, 0.1),
            font_alignment='center',
            size=(width, height),
            position=(x_pos, y_pos+font_size_vertical_offset,),
        )
