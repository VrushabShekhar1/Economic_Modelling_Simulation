from colorpoint import ColorPoint

class AdvancedColorPoint(ColorPoint):
    def _init_(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

new_point = AdvancedColorPoint(10, 10, "blue")
print(new_point)

print(new_point)



