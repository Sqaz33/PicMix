from abc import ABC, abstractmethod
from enum import Enum


class ColorModelName(Enum):
    RGB_24BPP = 0


class ColorModel(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass


class RGB24Bpp(ColorModel):
    def __init__(self, red: int, green: int, blue: int):
        if red < 0 or red > 255:
            raise ValueError("Red value must be in range [0, 255]")
        if green < 0 or green > 255:
            raise ValueError("Green value must be in range [0, 255]")
        if blue < 0 or blue > 255:
            raise ValueError("Blue value must be in range [0, 255]")

        self._red = red
        self._green = green
        self._blue = blue

    def red(self) -> int:
        return self._red

    def green(self) -> int:
        return self._green

    def blue(self) -> int:
        return self._blue

    def __eq__(self, other):
        return (
                self._red == other.red() and
                self._green == other.green() and
                self._blue == other.blue()
        )

    def __lt__(self, other):
        return (
            self._red < other.red() and
            self._green < other.green() and
            self._blue < other.blue() and
            not self == other
        )

    def __str__(self) -> str:
        return f'{self._red}, {self._green}, {self._blue}'


class Pixel:
    def __init__(self, color_model: ColorModelName, **kwargs):
        if color_model == ColorModelName.RGB_24BPP:
            if any(c not in ('red', 'green', 'blue') for c in kwargs.keys()):
                raise ValueError("RGB24BPP color model requires red, green and blue values")

            self._value = RGB24Bpp(**kwargs)
            self._color_model = color_model

    def __str__(self) -> str:
        return f'{self._color_model.name}: {self._value}'