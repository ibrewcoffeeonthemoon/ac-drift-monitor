import ac
import acsys

from app.window import window


class Indicator:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        max_value: float,
        name: str,
        arrow_on_top: bool = True,
        triangle_width: int = 10,
    ) -> None:
        self.name = name
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._max_value = max_value
        self._arrow_on_top = arrow_on_top
        self._bar_len = width
        self._triangle_width = triangle_width

        # value
        self._value = 0.0
        self._old_value = 0.0

        # labels
        self._name_label = ac.addLabel(window, name)
        self._value_label = ac.addLabel(window, '')
        y_label_pos = y_pos+height-40 if arrow_on_top else y_pos+20
        ac.setPosition(self._name_label, x_pos+20, y_label_pos)
        ac.setPosition(self._value_label, x_pos+50, y_label_pos)

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        # clip value
        self._value = min(max(value, -self._max_value), self._max_value)

        # smooth value
        weight = 0.2
        self._value = self._old_value*weight + self._value*(1-weight)

        # deadzone
        if (abs(self._value) < 0.1):
            self._value = 0

        # display
        ac.setText(self._value_label, "{:.2f}g".format(abs(self._value)))

        # calc indicator percentage position
        pct = self._value/self._max_value

        # draw triangle
        if self._arrow_on_top:
            self._draw_upper_triangle(self._width//2 + (pct*(self._bar_len/2)))
        else:
            self._draw_lower_triangle(self._width//2 + (pct*(self._bar_len/2)))

    def _draw_upper_triangle(self, x: float) -> None:
        w = self._triangle_width
        y = self._y_pos + self._height
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, y)
        ac.glVertex2f(x-(w/2), y-w)
        ac.glVertex2f(x+(w/2), y-w)
        ac.glEnd()
        ac.glQuad(x-(w/2), y-(w + w/2), w, w/2)

    def _draw_lower_triangle(self, x: float) -> None:
        w = self._triangle_width
        y = self._y_pos
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, y)
        ac.glVertex2f(x-(w/2), y+w)
        ac.glVertex2f(x+(w/2), y+w)
        ac.glEnd()
        ac.glQuad(x-(w/2), y+w, w, w/2)
