import copy
from typing import Any

import matplotlib.pyplot as plt
import numpy
import numpy as np
import skimage


class Pic:
    """
    Class for a picture.

    Attributes:
        pic (np.array): The picture presented as a numpy array.
        color (str): The color of the monochrome picture.
        is_monochrome (bool): Whether the picture is monochrome.
        height (int): The height of the picture.
        width (int): The width of the picture.
    """
    def __init__(self, pic: np.array, color="Greys"):
        """
        Create the new Pic object.
        :param pic (np.array): Picture as a NumPy array.
        :param color (str): Monochrome picture color as a string.
        """
        if len(pic.shape) not in (2, 3):
            raise "required color model RGB or monochromatic with 8 bits per channel"

        self._monochrome_color = color
        self._is_monochrome = len(pic.shape) == 2
        self._pic = pic
        self._height, self._width = pic.shape[0:2]

    def copy(self) -> 'Pic':
        return copy.deepcopy(self)

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def monochrome_color(self) -> str:
        return self._monochrome_color

    def is_monochrome(self) -> bool:
        return self._is_monochrome

    def set_pixel_at(self, x: int, y: int, value):
        if x >= self._width or y >= self._height:
            raise "pixel position is larger than the pic size"
        if x < 0 or y < 0:
            raise "pixel position less than zero"
        if ((not type(value) is type(self._pic[0][0])) or
                (type(value) is int and not self._is_monochrome) or
                (type(value) is np.array and value.shape[0] != self._pic.shape[-1])):
            raise "The color model of the picture and the installed pixel are different"
        self._pic[y][x] = value

    def add_rows(self, number: int):
        assert number > 1, "the number of rows must be more than one"
        r = number
        c = self._pic.shape[1]
        size = (r, c) if self.is_monochrome() else (r, c, self._pic.shape[-1])
        new_rows = np.zeros(size, dtype=self._pic.dtype)
        self._pic = np.vstack([self._pic, new_rows])

    def add_columns(self, number: int):
        assert number > 1, "the number of columns must be more than one"
        r = self._pic.shape[0]
        c = number
        size = (r, c) if self.is_monochrome() else (r, c, self._pic.shape[-1])
        new_rows = np.zeros(size, dtype=self._pic.dtype)
        self._pic = np.hstack([self._pic, new_rows])

    def get_average_pixel_from_rectangle(self, top_left_corner: (int, int), bottom_right_corner: (int, int)) -> Any:
        el_slice = 1 if self._is_monochrome else self._pic.shape[-1]
        sub_array = self._pic[
                    top_left_corner[0]:bottom_right_corner[0] + 1,
                    top_left_corner[1]:bottom_right_corner[1] + 1,
                    0:el_slice
                    ]
        sm = np.sum(np.sum(sub_array, axis=0), axis=0)
        average = sm / ((bottom_right_corner[0]+1) * (bottom_right_corner[1]+1))
        return np.ceil(average).astype(self._pic.dtype)

    def get_average_pixel(self) -> Any:
        return self.get_average_pixel_from_rectangle(
            (0, 0),
            (self._height-1, self._width-1)
        )

    def display_pic_pyplot(self):
        if self._is_monochrome:
            plt.imshow(self._pic, cmap=self._monochrome_color)
        else:
            plt.imshow(self._pic)
        plt.imshow(self._pic)
        plt.show()


def load_pic(path_to_pic: str) -> Pic:
    pic = skimage.io.imread(path_to_pic)
    return Pic(pic)


def load_pics(paths_to_pictures) -> list[Pic]:
    pics = skimage.io.imread_collection(paths_to_pictures)
    return pics


import unittest


class TestPic(unittest.TestCase):
    def test_test(self):
        snipers = skimage.io.imread("photo_2024-05-10_10-18-08.jpg")
        snipers_pic = Pic(snipers)
        print(snipers_pic.get_average_pixel())


if __name__ == "__main__":
    unittest.main()
