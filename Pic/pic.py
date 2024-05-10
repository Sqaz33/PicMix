import numpy
import skimage

from .pixel import *


class Pic:
    def __init__(self, pic: numpy.array):
        if pic.shape[-1] not in (1, 3):
            raise ValueError("An image with an unsupported color model was sent")

        self._pic = numpy.array([
            [
                Pixel(
                    color_model=ColorModelName.RGB_24BPP,
                    red=p[0], green=p[1], blue=p[2]
                )
                for p in line
            ]
            for line in pic
        ])
        self._height, self._width = pic.shape[0:2]

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


def load_pic(path_to_pic: str) -> Pic:
    pic = skimage.io.imread(path_to_pic)
    return Pic(pic)


def load_pics(paths_to_pictures) -> list[Pic]:
    pics = skimage.io.imread_collection(paths_to_pictures)
    return pics


