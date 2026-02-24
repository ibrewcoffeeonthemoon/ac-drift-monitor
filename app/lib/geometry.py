'''
NOTE: on python 3.3.5, tuple subclass is roughly 2.5x to 3x slower than native tuple
'''


class Vertex:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Size:
    __slots__ = ('width', 'height')

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Position:
    __slots__ = ('x_pos', 'y_pos')

    def __init__(self, x_pos: float, y_pos: float) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
