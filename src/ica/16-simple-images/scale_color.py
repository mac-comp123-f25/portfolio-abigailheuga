from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

def weighted_scale(pic, w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r * w1) + (g * w2) + (b * w3)
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic

if __name__ == '__main__':
    pic = Picture("../SampleImages/antiqueTractors.jpg")
    gray_pic = grayscale(pic)

    weighted1 = weighted_scale(pic, 0.5, 0.25, 0.25)
    weighted2 = weighted_scale(pic, 0.2, 0.7, 0.1)
    weighted3 = weighted_scale(pic, 0.1, 0.1, 0.8)

    gray_pic.show()
    weighted1.show()
    weighted2.show()
    weighted3.show()

    keep_windows_open()