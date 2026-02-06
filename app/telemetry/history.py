from collections import deque
from itertools import islice


class History:
    def __init__(
        self,
        maxlen: int,
    ) -> None:
        self._maxlen = maxlen
        self._data = deque(maxlen=maxlen)  # type: deque[tuple[float, ...]]

    def append(self, val: 'tuple[float, ...]') -> None:
        self._data.append(val)

    @property
    def last(self) -> 'tuple[float, ...]':
        return self._data[-1]

    def sma(self, n: int) -> 'tuple[float, ...]':
        win = islice(self._data, self._maxlen-n, self._maxlen)
        avg = tuple(sum(series)/n for series in zip(*win))
        return avg
