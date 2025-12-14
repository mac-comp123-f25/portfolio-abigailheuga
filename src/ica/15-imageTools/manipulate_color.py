from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def change_red(picture, factor):
    """
    Multiply the red channel of every pixel by the factor.
    """
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        new_red = red * factor
        picture.setColor(x, y, (new_red, grn, blu))

def change_blue(picture, factor):
    """
    Multiply the blue channel of every pixel by the factor.
    """
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        new_blue = blu * factor
        picture.setColor(x, y, (red, grn, new_blue))

def remove_blue(picture):
    """
    Sets the blue channel of every pixel to 0.
    """
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, grn, 0))

def fix_green(picture, value):
    """
    Sets the green channel of every pixel in the picture to the given value (0-255)
    """
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, value, blu))

def main():
    fruit_pic = Picture("../SampleImages/raspberries.jpg")
    fruit_pic.show()
    change_red(fruit_pic, 2.0)
    fruit_pic.show()

    sky_pic = Picture("../SampleImages/bryceCanyon.jpg")
    sky_pic.show()
    change_blue(sky_pic, 0.5)
    sky_pic.show()

    remove_blue_pic = Picture("../SampleImages/bryceCanyon.jpg")
    remove_blue_pic.show()
    remove_blue(remove_blue_pic)
    remove_blue_pic.show()

    green_pic = Picture("../SampleImages/canadianRockies.jpg")
    green_pic.show()
    fix_green(green_pic, 255)
    green_pic.show()

    keep_windows_open()

if __name__ == "__main__":
    main()