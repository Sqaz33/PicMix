import copy

import matplotlib.pyplot as plt
import numpy as np
import skimage


class Pic:
    def __init__(self, pic: np.array, color="Greys"):
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

    #TODO: подумать над названием (получение среднего пикселя из диапазона)
    def get_average_pixel_from_range(self, ):
        pass

    #TODO: переделать вычисление среднего пикселя
    def get_average_pixel(self):
        sm = 0 if self._is_monochrome else np.zeros((1, 3), dtype=self._pic.dtype)
        for row in self._pic:
            for col in row:
                for p in col:
                    sm += p
        return sm / (self._width * self._height)

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


if __name__ == "__main__":
    snipers = skimage.io.imread("photo_2024-05-10_10-18-08.jpg")
    snipers_pic = Pic(snipers)
    print(snipers_pic.get_average_pixel())