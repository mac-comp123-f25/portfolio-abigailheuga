from stringprep import b1_set

from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1, pic2):
    """
    Takes two pictures of the same size and returns a new picture
    that is the pixel-wise average of the two.
    """
    width = pic1.getWidth()
    height = pic1.getHeight()

    new_pic = Picture(width, height)
    new_pic.show()

    for (x,y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        ave_r = (r1 + r2) / 2
        ave_g = (g1 + g2) / 2
        ave_b = (b1 + b2) / 2

        new_pic.setColor(x, y, (ave_r, ave_g, ave_b))

        if (x + y) % 500 == 0:
            new_pic.show()

    return new_pic

def blend2(pic1, pic2):
    """
    Blends two pictures of potentially different sizes by only blending the
    overlapping region (min width x max height).
    """
    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())

    new_pic = Picture(new_width, new_height)
    new_pic.show()

    for (x,y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        ave_r = (r1 + r2) / 2
        ave_g = (g1 + g2) / 2
        ave_b = (b1 + b2) / 2

        new_pic.setColor(x, y, (ave_r, ave_g, ave_b))

        if (x + y) % 500 == 0:
            new_pic.show()

    return new_pic

def weighted_blend(pic1, pic2, wgt1):
    """
    Blends two pictures using a weighted average.
    wgt1 is the weight for pic1 (between 0.0 and 1.0).
    The weight for pic2 is computed as 1.0 - wgt1.
    """
    wgt2 = 1.0 - wgt1

    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())

    new_pic = Picture(new_width, new_height)
    new_pic.show()

    for (x,y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        ave_r = wgt1 * r1 + wgt2 * r2
        ave_g = wgt1 * g1 + wgt2 * g2
        ave_b = wgt1 * b1 + wgt2 * b2

        new_pic.setColor(x, y, (ave_r, ave_g, ave_b))

        if (x + y) % 500 == 0:
            new_pic.show()

    return new_pic


def main():
    p1 = Picture("../SampleImages/daylilies.jpg")
    p2 = Picture("../SampleImages/wildColumbine.jpg")
    p3 = simple_blend(p1, p2)
    p3.show()

    p4 = Picture("../SampleImages/muirWoods.jpg")
    p5 = Picture("../SampleImages/peony.jpg")
    p6 = blend2(p4, p5)
    p6.show()

    p7 = weighted_blend(p4, p5, 0.0)
    p7.show()

    p8 = weighted_blend(p4, p5, 0.25)
    p8.show()

    p9 = weighted_blend(p4, p5, 0.5)
    p9.show()

    p10 = weighted_blend(p4, p5, 0.75)
    p10.show()

    p11 = weighted_blend(p4, p5, 1.0)
    p11.show()

    keep_windows_open()

if __name__ == '__main__':
    main()
