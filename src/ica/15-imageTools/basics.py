from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

file_path = Picture("../SampleImages/mightyMidway.jpg")
pic_copy = duplicatePicture(pic)

num_pixels = getWidth(img) * getHeight(img)
print("Number of pixels in the image:", num_pixels)

pic_copy = duplicatePicture(pic)

width = getWidth(pic_copy)
height = getHeight(pic_copy)

setColor(getPixel(pic_copy, 0, 0), red)
setColor(getPixel(pic_copy, 1, 0), red)
setColor(getPixel(pic_copy, 0, 1), red)
setColor(getPixel(pic_copy, 1, 1), red)

setColor(getPixel(pic_copy, width-1, 0), red)
setColor(getPixel(pic_copy, width-2, 0), red)
setColor(getPixel(pic_copy, width-1, 1), red)
setColor(getPixel(pic_copy, width-2, 1), red)

setColor(getPixel(pic_copy, 0, height-1), red)
setColor(getPixel(pic_copy, 1, height-1), red)
setColor(getPixel(pic_copy, 0, height-2), red)
setColor(getPixel(pic_copy, 1, height-2), red)

setColor(getPixel(pic_copy, width-1, height-1), red)
setColor(getPixel(pic_copy, width-2, height-1), red)
setColor(getPixel(pic_copy, width-1, height-2), red)
setColor(getPixel(pic_copy, width-2, height-2), red)

savePicture(pic_copy, "mightyMidway-redCorners.jpg")

explore(pic_copy)
