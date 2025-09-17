""" There are several layers of circles that when put together look like a flower. The background is light blue, the base layer of circles is green, the layer on top of that is red, the middle dot is purple, and there is a stamp of a yellow turtle in the middle.
"""

import turtle
import math

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

sepalTurtle.up()                    # TODO: Step 2: start here
sepalTurtle.goto(0, 0)
sepalTurtle.down()
for reps in range (5):
    sepalTurtle.left(72)
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()

petalTurtle.up()
petalTurtle.goto(0, 0)
petalTurtle.down()
for reps in range (5):
    petalTurtle.left(72)
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()

centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(0, 220)
sepalTurtle.down()
for reps in range (5):
    sepalTurtle.left(72)
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()

petalTurtle.up()
petalTurtle.goto(0, 220)
petalTurtle.down()
for reps in range (5):
    petalTurtle.left(72)
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(220, 0)
sepalTurtle.down()
for reps in range (5):
    sepalTurtle.left(72)
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()

petalTurtle.up()
petalTurtle.goto(220, 0)
petalTurtle.down()
for reps in range (5):
    petalTurtle.left(72)
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(0, -220)
sepalTurtle.down()
for reps in range (5):
    sepalTurtle.left(72)
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()

petalTurtle.up()
petalTurtle.goto(0, -220)
petalTurtle.down()
for reps in range (5):
    petalTurtle.left(72)
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(-220, 0)
sepalTurtle.down()
for reps in range (5):
    sepalTurtle.left(72)
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()

petalTurtle.up()
petalTurtle.goto(-220, 0)
petalTurtle.down()
for reps in range (5):
    petalTurtle.left(72)
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()