from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def main():
    pic = Picture("../SampleImages/mightyMidway.jpg")

    w = pic.getWidth()
    h = pic.getHeight()
    num_pixels = w * h
    print(num_pixels)

    new_pic = pic.copy()
    red = (255, 0, 0)

    corners = [
        (0,0),
        (w-1, 0),
        (0, h-1),
        (w-1, h-1)
    ]

    for (x, y) in corners:
        new_pic.setColor(x, y, red)

    out_path = "../SampleImages/mightyMidway-redCorners.jpg"
    new_pic.save(out_path)

    new_pic.explore()

    keep_windows_open()

if __name__ == '__main__':
    main()