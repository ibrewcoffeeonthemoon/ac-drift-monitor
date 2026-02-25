class Color:
    __slots__ = ('r', 'g', 'b', 'a')

    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a


class ColorPreset:
    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        self._r = r
        self._g = g
        self._b = b
        self._a = a
        # presets
        self.full = Color(r, g, b, 1.0)
        self.a9 = Color(r, g, b, 0.9)
        self.a8 = Color(r, g, b, 0.8)
        self.a7 = Color(r, g, b, 0.7)
        self.a6 = Color(r, g, b, 0.6)
        self.a5 = Color(r, g, b, 0.5)
        self.a4 = Color(r, g, b, 0.4)
        self.a3 = Color(r, g, b, 0.3)
        self.a2 = Color(r, g, b, 0.2)
        self.a1 = Color(r, g, b, 0.1)
        self.transparent = Color(r, g, b, 0.0)

    def alpha(self, a: float) -> Color:
        return Color(self._r, self._g, self._b, a)


# basic color presets
white = ColorPreset(1, 1, 1)
black = ColorPreset(0, 0, 0)
red = ColorPreset(1, 0, 0)
yellow = ColorPreset(1, 1, 0)
green = ColorPreset(0, 1, 0)
cyan = ColorPreset(0, 1, 1)
blue = ColorPreset(0, 0, 1)
magenta = ColorPreset(1, 0, 1)
