from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def negative(picture):
    """
    Creates and returns a new picture that is the negative of the input picture.
    """
    neg_pic = picture.copy()
    for (x, y) in neg_pic:
        (r, g, b) = neg_pic.getColor(x, y)

        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b

        neg_pic.setColor(x, y, (new_r, new_g, new_b))

    return neg_pic

def main():
    pic = Picture("../SampleImages/butterfly.jpg")
    pic.show()

    neg = negative(pic)
    neg.show()

    keep_windows_open()

if __name__ == "__main__":
    main()