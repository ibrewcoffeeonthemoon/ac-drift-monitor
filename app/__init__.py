import ac

from app.components.accG_grid import AccG_Grid
from app.components.slip_grid import Slip_Grid
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
            x_pos=width//4,
            y_pos=0,
            width=width//2,
            height=height,
            dot_size=30,
            max_value=1.20,
        )
        self.slipRatio_grid = Slip_Grid(
            i_slipRatio=2,
            x_pos=0,
            y_pos=height//2,
            width=width//4,
            height=height//2,
            dot_size=15,
            max_value=1.0,
        )

        # init
        self._car_id = ac.getFocusedCar()

    def render(self) -> None:
        # set indicator values
        self.accG_grid.render()
        self.slipRatio_grid.render()


# export
app = _App(
    width=600,
    height=300,
)
