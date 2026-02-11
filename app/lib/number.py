import math


class Number:
    # fixed slots, no __dict__ for this object, saves memory footprint
    __slots__ = ('_val', )

    def __init__(self, val: float) -> None:
        self._val = val

    @property
    def f(self) -> float:
        return self._val

    @property
    def i(self) -> int:
        return round(self._val)

    def shift(self, offset: float) -> 'Number':
        self._val = self._val + offset
        return self

    def amplify(self, magnitude: float) -> 'Number':
        self._val = self._val * magnitude
        return self

    def normalize(self, scale: float) -> 'Number':
        self._val = self._val/scale
        return self

    def clip(self, lower: float, upper: float) -> 'Number':
        self._val = min(max(self._val, lower), upper)
        return self

    def degree(self) -> 'Number':
        self._val = self._val * 180/math.pi
        return self

    def radian(self) -> 'Number':
        self._val = self._val * math.pi/180
        return self


def num(val: float) -> Number:
    return Number(val)
