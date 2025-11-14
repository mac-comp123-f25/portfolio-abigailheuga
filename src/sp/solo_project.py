import turtle
import random

petal_colors = ["red", "pink", "orange", "purple", "blue", "magenta", "yellow"]

# Functions
def draw_flower(x, y, petal_color, center_color, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(petal_color)

    #Draw petals
    for i in range(6):
        turtle.begin_fill()
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.end_fill()
        turtle.left(60)

    # Draw flower center
    turtle.penup()
    turtle.goto(x + size * 0.2, y)
    turtle.pendown()
    turtle.color(center_color)
    turtle.begin_fill()
    turtle.circle(size/4)
    turtle.end_fill()

def draw_stem(x,y,length):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("green")
    turtle.pensize(3)
    turtle.forward(length)

def draw_grass():
    turtle.penup()
    turtle.goto(-400,-275)
    turtle.color("limegreen")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    turtle.setheading(0)

def draw_sun():
    turtle.penup()
    turtle.goto(250,150)
    turtle.pendown()
    turtle.color("gold")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_bush(x,y, color, size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(10):
        turtle.circle(size)
        turtle.left(36)
    turtle.end_fill()

def garden_scene(num_flowers, flower_color):
    turtle.speed(0)
    turtle.bgcolor("skyblue")
    draw_grass()
    draw_sun()

    for i in range(num_flowers):
        x = random.randint(-300, 300)
        ground_y = -275
        stem_length = random.randint(70, 120)
        size = random.randint(10, 18)

        # Pick flower color
        if flower_color == "random":
            this_flower_color = random.choice(petal_colors)
        else:
            this_flower_color = flower_color

        draw_stem(x, ground_y, stem_length)
        draw_flower(x, ground_y + stem_length, this_flower_color, "yellow", size)

    # adding a few bushes
    for bx in [-250,50,350]:
        draw_bush(bx, -275, "forestgreen", 20)

    turtle.hideturtle()
    turtle.done()


# User Input
print("Welcome to the Turtle Meadow!")

num_flowers = int(input("How many flowers would you like to draw? "))

flower_color = input("Choose a color for the petals (red, pink, orange, purple, blue, magenta, yellow) or type 'random' for multiple colors: ").strip().lower()
if flower_color == "":
    flower_color = "orange"

# run the scene
garden_scene(num_flowers, flower_color)