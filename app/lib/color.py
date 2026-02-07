class Color:
    def __init__(
        self,
        r: float,
        g: float,
        b: float,
        opacity: float = 1.0,
    ) -> None:
        self._r = r
        self._g = g
        self._b = b
        self._opacity = opacity

    @property
    def t(self) -> 'tuple[float, float, float, float]':
        return (self._r, self._g, self._b, self._opacity)

    def opacity(self, opacity: float) -> 'Color':
        self._opacity = opacity
        return self

    @property
    def full(self) -> 'Color': return self.opacity(1)
    @property
    def a9(self) -> 'Color': return self.opacity(.9)
    @property
    def a8(self) -> 'Color': return self.opacity(.8)
    @property
    def a7(self) -> 'Color': return self.opacity(.7)
    @property
    def a6(self) -> 'Color': return self.opacity(.6)
    @property
    def a5(self) -> 'Color': return self.opacity(.5)
    @property
    def a4(self) -> 'Color': return self.opacity(.4)
    @property
    def a3(self) -> 'Color': return self.opacity(.3)
    @property
    def a2(self) -> 'Color': return self.opacity(.2)
    @property
    def a1(self) -> 'Color': return self.opacity(.1)
    @property
    def transparent(self) -> 'Color': return self.opacity(0)


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
