import ac

import config
from app.components import Component
from app.components.gforce_monitor import GForceMonitor
from app.components.slip_ratio_monitor import SlipRatioMonitor
from app.window import window


class _App:
    def __init__(
        self,
        width: int,
    ) -> None:
        # create components
        self._components = [
            SlipRatioMonitor(
                x_pos=0,
                y_pos=0,
            ),
            GForceMonitor(
                x_pos=width//2,
                y_pos=0,
            ),
        ]  # type: list[Component]

        # TODO: dynamically resolve width and height from the component above, no hard code
        # set layouts, styles
        ac.setSize(
            window,
            round(sum(c.width for c in self._components)),
            config.App.height,
        )
        ac.setTitle(window, '')
        ac.setIconPosition(window, 0, -10000)
        ac.drawBorder(window, False)

    def render(self) -> None:
        for component in self._components:
            component.render()


# export
app = _App(
    width=config.App.height*2,
)
