from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def color_shuffle(picture):
    """
    Returns a new picture where the color channels are shuffled:
    new_red = old_blue
    new_green = old_red
    new_blue = old_green
    """
    new_pic = picture.copy()

    for (x,y) in picture:
        (r, g, b) = picture.getColor(x, y)
        new_pic.setColor(x, y, (b, r, g))

    return new_pic

def main():
    mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
    mushrooms0.show()

    mushrooms1 = color_shuffle(mushrooms0)
    mushrooms1.show()

    mushrooms2 = color_shuffle(mushrooms1)
    mushrooms2.show()

    keep_windows_open()

if __name__ == "__main__":
    main()
