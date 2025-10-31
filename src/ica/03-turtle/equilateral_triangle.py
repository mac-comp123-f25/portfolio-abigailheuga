import turtle

window = turtle.Screen()
window.bgcolor("lightblue")

turt = turtle.Turtle()
turt.color("green")
turt.pensize(3)

turt.begin_fill()

for x in range(3):
    turt.forward(120)
    turt.left(120)

turt.end_fill()

window.exitonclick()