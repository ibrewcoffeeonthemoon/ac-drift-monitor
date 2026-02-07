class Float:
    def __init__(self, val: float) -> None:
        self._val = val

    @property
    def value(self) -> float:
        return self._val

    def shift(self, offset: float) -> 'Float':
        self._val = self._val + offset
        return self

    def normalize(self, scale: float) -> 'Float':
        self._val = self._val/scale
        return self

    def clip(self, lower: float, upper: float) -> 'Float':
        self._val = min(max(self._val, lower), upper)
        return self
