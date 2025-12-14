from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *

def draw_something():
    pic = Picture(300, 300)

    pic.drawOval(50, 50, 250, 250, outlineColor = "black", fillColor = "yellow")

    pic.drawOval(95, 110, 125, 140, outlineColor = "black", fillColor = "black")
    pic.drawOval(175, 110, 205, 140, outlineColor="black", fillColor = "black")

    pic.drawArc(95, 130, 205, 230, startAngle=20, endAngle=160, style="arc", outlineColor="black")

    pic.drawLine(150, 145, 150, 170, color="black", width=2)

    pic.drawText(150, 260, "smiley face", color = "blue")

    return pic


def main():
    drawing = draw_something()
    drawing.show()
    keep_windows_open()


if __name__ == "__main__":
    main()
