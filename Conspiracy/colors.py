import logging

from _Framework.ButtonElement import Color


class BlinkColor(Color):
    def __init__(self, color1, color2, *a, **k):
        super(Color, self).__init__(color2, *a, **k)  # midi_value = color2
        self._color1 = color1
        self._color2 = color2

    def draw(self, interface):
        interface.send_value(self.midi_value)

    def blink_colors(self):
        return Color(self._color1), Color(self._color2)


class PadColors:
    BLACK = OFF = Color(0)
    RED = Color(1)
    RED_BLINK = BlinkColor(1, 25)  # Red | Purple
    GREEN = Color(2)
    GREEN_BLINK = BlinkColor(2, 26)  # Green | Lightblue
    BLUE = Color(3)
    BLUE_BLINK = BlinkColor(3, 26)  # Blue | Lightblue
    YELLOW = Color(8)
    PURPLE = Color(25)
    LIGHTBLUE = Color(26)
    WHITE = Color(27)


class TransportButtonColors:
    BLACK = OFF = Color(0)
    BLUE = Color(1)


class NavigationButtonColors:
    BLACK = OFF = Color(0)
    BLUE = Color(1)


class FButtonColors:
    BLACK = OFF = Color(0)
    RED = Color(1)
    GREEN = Color(2)
    YELLOW = Color(8)
