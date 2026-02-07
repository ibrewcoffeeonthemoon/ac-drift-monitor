from functools import lru_cache


class Color(tuple):
    def __new__(
        cls,
        r: float,
        g: float,
        b: float,
        a: float = 1.0
    ) -> 'Color':
        return super().__new__(cls, (r, g, b, a))

    @lru_cache()
    def alpha(self, a: float) -> 'Color':
        r, g, b, _ = self
        return Color(r, g, b, a)

    @property
    def full(self) -> 'Color': return self.alpha(1)
    @property
    def a9(self) -> 'Color': return self.alpha(.9)
    @property
    def a8(self) -> 'Color': return self.alpha(.8)
    @property
    def a7(self) -> 'Color': return self.alpha(.7)
    @property
    def a6(self) -> 'Color': return self.alpha(.6)
    @property
    def a5(self) -> 'Color': return self.alpha(.5)
    @property
    def a4(self) -> 'Color': return self.alpha(.4)
    @property
    def a3(self) -> 'Color': return self.alpha(.3)
    @property
    def a2(self) -> 'Color': return self.alpha(.2)
    @property
    def a1(self) -> 'Color': return self.alpha(.1)
    @property
    def transparent(self) -> 'Color': return self.alpha(0)


def color(r: float, g: float, b: float, a: float = 1.0) -> Color:
    return Color(r, g, b, a)


# basic colors
white = Color(1, 1, 1)
black = Color(0, 0, 0)
red = Color(1, 0, 0)
yellow = Color(1, 1, 0)
green = Color(0, 1, 0)
cyan = Color(0, 1, 1)
blue = Color(0, 0, 1)
magenta = Color(1, 0, 1)
