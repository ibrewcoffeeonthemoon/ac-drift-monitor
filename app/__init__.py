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

        # init
        self._car_id = ac.getFocusedCar()

    def render(self) -> None:
        # set indicator values
        self.accG_grid.render()


# export
app = _App(
    width=300,
    height=300,
)
