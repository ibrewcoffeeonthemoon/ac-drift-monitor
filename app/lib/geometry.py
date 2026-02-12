"""
NOTE: on python 3.3.5, tuple subclass is roughly 2.5x to 3x slower than native tuple
"""


class ValuePair:
    __slots__ = ('x', 'y')

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x = x
        self.y = y

    @property
    def f(self) -> 'tuple[float, float]':
        return self.x, self.y

    @property
    def i(self) -> 'tuple[int, int]':
        return round(self.x), round(self.y)


class Vertex(ValuePair):
    pass


class Size(ValuePair):
    pass


class Position(ValuePair):
    pass
