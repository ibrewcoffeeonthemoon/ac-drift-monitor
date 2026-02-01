import ac
import acsys


class Indicator:
    maxG = 2
    bar_len = 322
    triangle_width = 10

    def __init__(
        self,
        window: int,
        x_pos: int,
        y_pos: int,
        name: str,
        arrow_on_top: bool,
    ) -> None:
        self.name = name
        self._arrow_on_top = arrow_on_top

        # value
        self._value = 0.0
        self._old_value = 0.0

        # indicator position
        self._ind_pos = 0.0

        # labels
        self._name_label = ac.addLabel(window, name)
        self._value_label = ac.addLabel(window, "0.0g")
        ac.setPosition(self._name_label, x_pos, y_pos)
        ac.setPosition(self._value_label, x_pos+50, y_pos)

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        # clip value
        self._value = min(max(value, -self.maxG), self.maxG)

        # smooth value
        weight = 0.2
        self._value = self._old_value*weight + self._value*(1-weight)

        # round value
        self._value = round(self._value*100)/100

        # display
        ac.setText(self._value_label, "{0}g".format(abs(self._value)))
        if (abs(self._value) < 0.1):
            self._value = 0
            ac.setText(self._value_label, "0.0g")

        # calc indicator position
        self._ind_pos = self._value/self.maxG

        # draw triangle
        if self._arrow_on_top:
            self._draw_upper_triangle(167 + (self._ind_pos*(self.bar_len/2)))
        else:
            self._draw_lower_triangle(167 + (self._ind_pos*(self.bar_len/2)))

    def _draw_upper_triangle(self, x: float) -> None:
        w = self.triangle_width
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 104)
        ac.glVertex2f(x-(w/2), 104-w)
        ac.glVertex2f(x+(w/2), 104-w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 104-(w + w/2), w, w/2)

    def _draw_lower_triangle(self, x: float) -> None:
        w = self.triangle_width
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 109)
        ac.glVertex2f(x-(w/2), 109+w)
        ac.glVertex2f(x+(w/2), 109+w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 109+w, w, w/2)

    def _draw_bar(self) -> None:
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(0, 55, 300, 7)
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(148, 45, 4, 27)
