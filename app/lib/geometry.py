"""
NOTE: on python 3.3.5, tuple subclass is roughly 2.5x to 3x slower than native tuple
"""


class Vertex(tuple):
    def __new__(cls, x: int, y: int,) -> 'Vertex':
        return super().__new__(cls, (x, y))


def vertex(x: int, y: int) -> Vertex:
    return Vertex(x, y)
