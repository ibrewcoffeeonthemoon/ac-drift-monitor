import ac

from app.components.accG_grid import AccG_Grid
from app.settings import settings
from app.window import window


class _App:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        # set layouts, styles
        ac.setSize(window, width, height)
        ac.setTitle(window, '')
        ac.setIconPosition(window, 0, -10000)
        ac.drawBorder(window, False)

        # create components
        self.accG_grid = AccG_Grid(
            x_pos=0,
            y_pos=0,
            width=width,
            height=height,
            dot_size=30,
            max_value=1.20,
        )

        # button with whole area, click to toggle settings
        btn = ac.addButton(window, '')
        ac.setPosition(btn, 0, 0)
        ac.setSize(btn, width, height)
        ac.addOnClickedListener(btn, on_click)

    def render(self) -> None:
        # set indicator values
        self.accG_grid.render()


def on_click(name: str, state: int) -> None:
    # handler must be a root scoped funciton with two args
    settings.toggle_visible()


# export
app = _App(
    width=300,
    height=300,
)
