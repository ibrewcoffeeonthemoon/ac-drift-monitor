from ._base import Text


def big_text(
    text: str,
    x_pos: int,
    y_pos: int,
    width: int,
    height: int,
    font_color: 'tuple[float, float, float, float]',
    expected_text_len: int,
) -> Text:
    shrink_factor = 1.0 - (expected_text_len - 1) * 0.25
    shrink_factor = max(0.5, min(1.0, shrink_factor))

    font_size = round(min(width, height)*shrink_factor)
    font_size_vertical_offset = height//2-font_size*3//4
    return Text(
        text=text,
        font_size=font_size,
        font_color=font_color,
        font_alignment='center',
        size=(width, height),
        position=(x_pos, y_pos+font_size_vertical_offset,),
    )
