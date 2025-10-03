import turtle

window = turtle.Screen()
window.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.shape("arrow")

def draw_star(size):
    for x in range(5):
        my_turtle.left(144)
        my_turtle.forward(size)

draw_star(100)

my_turtle.up()
my_turtle.goto(40,40)
my_turtle.down()

my_turtle.color("navy")
draw_star(50)

window.exitonclick()