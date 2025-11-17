from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1, pic2):
    width = pic1.getWidth()
    height = pic1.getHeight()

    new_pic = Picture(width, height)

    for x in range(width):
        new_pic.show()

        for y in range(height):
            p1 = pic1.getPixel(x, y)
            p2 = pic2.getPixel(x, y)

            r1, g1, b1 = p1.getRed(), p1.getGreen(), p1.getBlue()
            r2, g2, b2 = p2.getRed(), p2.getGreen(), p2.getBlue()

            avg_r = (r1 + r2) // 2
            avg_g = (g1 + g2) // 2
            avg_b = (b1 + b2) // 2

            out_pixel = new_pic.getPixel(x, y)
            out_pixel.setRed(avg_r)
            out_pixel.setGreen(avg_g)
            out_pixel.setBlue(avg_b)

    return new_pic


p1 = Picture("../SampleImages/daylilies.jpg")
p2 = Picture("../SampleImages/wildColumbine.jpg")
p3 = simple_blend(p1, p2)

keep_windows_open()