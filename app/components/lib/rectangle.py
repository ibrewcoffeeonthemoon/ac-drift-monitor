import ac


class Rectangle:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        color: tuple = (1, 1, 1, 1),
    ) -> None:
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._color = color

    def render(self) -> None:
        ac.glColor4f(*self._color)
        ac.glQuad(self._x_pos, self._y_pos, self._width, self._height)
