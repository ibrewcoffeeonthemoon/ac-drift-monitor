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
        self._accG_grid = AccG_Grid(
            x_pos=width//4,
            y_pos=0,
            width=width//2,
            height=height,
            dot_size=30,
            max_value=1.20,
        )
        self._slipRatio_grids = [
            Slip_Grid(
                i_slipRatio=i,
                x_pos=x_pos,
                y_pos=y_pos,
                width=width//4,
                height=height//2,
                dot_size=20,
                max_value=3.0,
            )
            for i, (x_pos, y_pos) in enumerate((
                (0, 0),
                (width//4*3, 0),
                (0, height//2),
                (width//4*3, height//2),
            ))
        ]

        # init
        self._car_id = ac.getFocusedCar()

    def render(self) -> None:
        self._accG_grid.render()
        for slipRatio_grid in self._slipRatio_grids:
            slipRatio_grid.render()


# export
app = _App(
    width=600,
    height=300,
)
