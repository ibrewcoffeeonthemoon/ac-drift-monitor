import ac

import config
from app.components.gforce_monitor import GForceMonitor
from app.components.slip_ratio_monitor import SlipRatioMonitor
from app.window import window


class _App:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        # create components
        self._slip_ratio_monitor = SlipRatioMonitor(
            x_pos=0,
            y_pos=0,
            width=width//2,
            height=height,
        )
        self._gforce_monitor = GForceMonitor(
            x_pos=width//2,
            y_pos=0,
            width=width//2,
            height=height,
        )

        # TODO: dynamically resolve width and height from the component above, no hard code
        # set layouts, styles
        ac.setSize(window, width, height)
        ac.setTitle(window, '')
        ac.setIconPosition(window, 0, -10000)
        ac.drawBorder(window, False)

    def render(self) -> None:
        self._gforce_monitor.render()
        self._slip_ratio_monitor.render()


# export
app = _App(
    width=config.App.height*2,
    height=config.App.height,
)
