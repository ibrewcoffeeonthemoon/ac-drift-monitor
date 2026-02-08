"""
NOTE: on python 3.3.5, tuple subclass is roughly 2.5x to 3x slower than native tuple
"""


class Tuple2i(tuple):
    # fixed slots, no __dict__ for this object, saves memory footprint
    __slots__ = ()

    def __new__(cls, x: int, y: int,) -> 'Tuple2i':
        return super().__new__(cls, (x, y))


def tuple2i(x: int, y: int) -> Tuple2i:
    return Tuple2i(x, y)


Vertex = Tuple2i
vertex = tuple2i
