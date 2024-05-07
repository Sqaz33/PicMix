import numpy


class Pic:
    def __init__(self, pic: numpy.array):
        self._pic = pic
        self._height, self._width = pic.shape[0:2]

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


    def


def from_permanent_memory(path_to_pic: str) -> Pic:
    pass
