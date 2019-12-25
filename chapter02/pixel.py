class Pixel:

    def __init__(self, x=0, y=0, r=0, g=0, b=0):
        self._x = x
        self._y = y
        self._red = r
        self._green = g
        self._blue = b

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg_color = (self._red + self._green + self._blue) / 3
        self._red = self._green = self._blue = int(avg_color)

    def print_pixel_info(self):
        print(f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})', end='')
        if 0 < self._red and 0 == self._green and 0 == self._blue:
            print(' Red')
        elif 0 == self._red and 0 < self._green and 0 == self._blue:
            print(' Green')
        elif 0 == self._red and 0 == self._green and 0 < self._blue:
            print(' Blue')
        else:
            print()


def main():
    pixel = Pixel(5, 6, 250)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()


if __name__ == '__main__':
    main()
