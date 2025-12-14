from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def red_channel(picture):
    """
    Returns a new picture containing only the red channel.
    Green and blue are set to 0
    """
    new_pic = picture.copy()

    for (x,y) in picture:
        (r, g, b) = picture.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))

    return new_pic

def green_channel(picture):
    """
    Returns a new picture containing only the green channel.
    Red and blue are set to 0
    """
    new_pic = picture.copy()

    for (x,y) in picture:
        (r, g, b) = picture.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))

    return new_pic

def blue_channel(picture):
    """
    Returns a new picture containing only the blue channel.
    Red and green are set to 0.
    """
    new_pic = picture.copy()

    for (x,y) in picture:
        (r, g, b) = picture.getColor(x, y)
        new_pic.setColor(x, y, (0, 0, b))

    return new_pic


def main():
    astilbe = Picture("../SampleImages/astilbe.jpg")
    astilbe.show()

    astilbe_red = red_channel(astilbe)
    astilbe_red.show()

    astilbe_green = green_channel(astilbe)
    astilbe_green.show()

    astilbe_blue = blue_channel(astilbe)
    astilbe_blue.show()

    keep_windows_open()

if __name__ == '__main__':
    main()
