import ac

import config

from .monitor import *
from .window import window


class _App:
    def __init__(self) -> None:
        # attach monitors
        self._monitors = []  # type: list[Monitor]
        for monitor_class in sorted(MONITOR_CLASSES, key=lambda cls: cls.col_index):
            self._attach(monitor_class)

        # set layouts, styles
        ac.setSize(
            window,
            round(sum(c.width for c in self._monitors)),
            config.App.height,
        )
        ac.setTitle(window, '')
        ac.setIconPosition(window, 0, -10000)
        ac.drawBorder(window, False)

    @property
    def _x_current(self) -> int:
        return sum(c.width for c in self._monitors)

    @property
    def _y_current(self) -> int:
        return 0

    def _attach(self, cls: 'type[Monitor]') -> None:
        if cls.enabled:
            self._monitors.append(cls(
                x_pos=self._x_current,
                y_pos=self._y_current
            ))

    def render(self) -> None:
        for monitor in self._monitors:
            monitor.render()


# export
app = _App()
