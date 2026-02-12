import math

from ....lib.geometry import Vertex


class Region:
    def __init__(
        self,
        x_pos: float,
        y_pos: float,
        width: float,
        height: float,
    ) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.corner_top_left = Vertex(x_pos, y_pos)
        self.corner_top_right = Vertex(x_pos+width, y_pos)
        self.corner_bottom_left = Vertex(x_pos, y_pos+height)
        self.corner_bottom_right = Vertex(x_pos+width, y_pos+height)
        self.corners = (
            self.corner_top_right,
            self.corner_top_left,
            self.corner_bottom_left,
            self.corner_bottom_right,
        )
        self.center = Vertex(x_pos+width/2, y_pos+height/2)
        self.diagonal_len = math.sqrt(width**2 + height**2)

    @property
    def top_half(self) -> 'Region':
        return type(self)(self.x_pos, self.y_pos, self.width, self.height/2)

    @property
    def bottom_half(self) -> 'Region':
        return type(self)(self.x_pos, self.center.y, self.width, self.height/2)

    @property
    def top_left(self) -> 'Region':
        return type(self)(self.x_pos, self.y_pos, self.width/2, self.height/2)

    @property
    def top_right(self) -> 'Region':
        return type(self)(self.center.x, self.y_pos, self.width/2, self.height/2)

    @property
    def bottom_left(self) -> 'Region':
        return type(self)(self.x_pos, self.center.y, self.width/2, self.height/2)

    @property
    def bottom_right(self) -> 'Region':
        return type(self)(self.center.x, self.center.y, self.width/2, self.height/2)
