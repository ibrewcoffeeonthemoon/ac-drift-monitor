import ac
import acsys

from app.indicator import Indicator


class App:
    name = 'AC Drift Monitor'
    width = 333
    height = 173
    bg_img_path = 'apps/python/ac-drift-monitor/assets/bg.png'

    def __init__(self) -> None:
        # create app window
        self._window = win = ac.newApp(self.name)

        # set layouts, styles
        ac.setSize(win, self.width, self.height)
        ac.drawBorder(win, False)
        ac.setBackgroundOpacity(win, 0)
        ac.setBackgroundTexture(win, self.bg_img_path)

        # create indicators
        self._ind_latG = Indicator(
            win,
            x_pos=22,
            y_pos=62,
            max_value=1.5,
            name="Lat.",
        )
        self._ind_longG = Indicator(
            win,
            x_pos=22,
            y_pos=136,
            max_value=1.5,
            name="Lon.",
            arrow_on_top=False
        )

        # init
        self._car_id = ac.getFocusedCar()

    @property
    def window(self) -> int:
        return self._window

    def render(self) -> None:
        # fetch car state values
        x, y, z = ac.getCarState(self._car_id, acsys.CS.AccG)

        # set indicator values
        self._ind_latG.value = x
        self._ind_longG.value = z
