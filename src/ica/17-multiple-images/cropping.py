from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(image, start_x, start_y, crop_width, crop_height):
    cropped = Picture(crop_width, crop_height)

    for x in range(crop_width):
        for y in range(crop_height):
            original_x = start_x + x
            original_y = start_y + y
            color = image.getColor(original_x,original_y)
            cropped.setColor(x, y, color)

    return cropped

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

keep_windows_open()