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

    def _window(self, n: int) -> 'islice[tuple[float, ...]]':
        return islice(self._data, self._maxlen-n, self._maxlen)

    def window(self, n: int) -> 'tuple[float, ...]':
        return tuple(*self._window(n))

    def sma(self, n: int) -> 'tuple[float, ...]':
        return tuple(
            sum(series)/n
            for series in zip(*self._window(n))
        )
