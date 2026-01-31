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
        self.arrow_on_top = arrow_on_top

        # value
        self.value = 0
        self.old_value = 0

        # indicator position
        self.ind_pos = 0

        # labels
        ac.setPosition(ac.addLabel(window, name), x_pos, y_pos)
        self.value_label = ac.addLabel(window, "0.0g")
        ac.setPosition(self.value_label, x_pos+50, y_pos)

    def set_value(self, value: float) -> None:
        # clip value
        self.value = min(max(value, -self.maxG), self.maxG)

        # smooth value
        weight = 0.2
        self.value = self.old_value*weight + self.value*(1-weight)

        # round value
        self.value = round(self.value*100)/100

        # display
        ac.setText(self.value_label, "{0}g".format(abs(self.value)))
        if (abs(self.value) < 0.1):
            self.value = 0
            ac.setText(self.value_label, "0.0g")

        # calc indicator position
        self.ind_pos = self.value/self.maxG

        # draw triangle
        if self.arrow_on_top:
            self.draw_upper_triangle(167 + (self.ind_pos*(self.bar_len/2)))
        else:
            self.draw_lower_triangle(167 + (self.ind_pos*(self.bar_len/2)))

    def draw_upper_triangle(self, x: float) -> None:
        w = self.triangle_width
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 104)
        ac.glVertex2f(x-(w/2), 104-w)
        ac.glVertex2f(x+(w/2), 104-w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 104-(w + w/2), w, w/2)

    def draw_lower_triangle(self, x: float) -> None:
        w = self.triangle_width
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 109)
        ac.glVertex2f(x-(w/2), 109+w)
        ac.glVertex2f(x+(w/2), 109+w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 109+w, w, w/2)

    def draw_bar(self) -> None:
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(0, 55, 300, 7)
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(148, 45, 4, 27)
