import time
from src.ica.helpers.dummyWindow import *

from random import randrange


def get_rand_bg():
    pic = makeEmptyPicture(100, 100)

    r = randrange(256)
    g = randrange(256)
    b = randrange(256)

    c = makeColor(r, g, b)

    setAllPixels(pic, c)

    return pic


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
