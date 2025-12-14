import turtle

window = turtle.Screen()
window.bgcolor("lightyellow")

turt = turtle.Turtle()
turt.color("blue")
turt.pensize(2)

n = 6
side_length = 100

turt.begin_fill()

for x in range(n):
    turt.forward(side_length)
    turt.left(360/n)

turt.end_fill()

window.exitonclick()