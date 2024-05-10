import time

import matplotlib.pyplot as plp
import numpy
import skimage


class Pic:
    def __init__(self, pic: numpy.array):
        if len(pic.shape) not in (2, 3):
            raise ""

        self._pic = pic
        self._height, self._width = pic.shape[0:2]

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width



    def displayPicNumpy(self):
        plp.imshow(self._pic)
        plp.show()


def load_pic(path_to_pic: str) -> Pic:
    pic = skimage.io.imread(path_to_pic)
    return Pic(pic)


def load_pics(paths_to_pictures) -> list[Pic]:
    pics = skimage.io.imread_collection(paths_to_pictures)
    return pics


if __name__ == "__main__":
    start = time.time()
    ski_pic = skimage.data.camera()
    print(ski_pic.shape)
    Pic(ski_pic)
    print(time.time() - start)

