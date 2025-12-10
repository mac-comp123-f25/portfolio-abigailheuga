import tkinter as tk
import turtle
import random       # adding to include randomness

def check_draw_tree(sz):
    """Tester function for the draw_tree"""

    # setup window
    win = tk.Tk()
    win.title(f"Tree Fractal {sz}")
    win_size = sz * 7
    cv = tk.Canvas(win, width=win_size, height=win_size)
    cv.pack()
    ts = turtle.TurtleScreen(cv)
    t = turtle.RawTurtle(ts)

    # set up turtle
    t.left(90)
    t.up()
    t.backward(sz * 3)
    t.down()
    t.speed(0)
    t.color("green")

    # draw the draw_tree
    draw_tree(sz, t)


def draw_tree(branch_len, turt):
    """The Interactive Textbook's draw_fractal_treedraw_fractal_tree drawing fractal function.
    Takes in the length of the main branch and a turtle, and it draws
    a symmetrical draw_fractal_treedraw_fractal_tree shape with branching to left and right. The fractal
    stops if the branch length gets to be less than or equal to 5"""

    """ Modified fractal tree function.
    
    Differences from the original draw_fractal_treedraw_fractal_tree function:
    - uses slightly different angles for each branch
    - right and left branches shrink by different amounts
    - adds small random variation to angle and branch size to make the tree look more natural / 'weeping' 
    """
    if branch_len > 5:
        # small random variation so each tree looks a bit different
        angle_right = 30 + random.randint(-5, 5)
        angle_left = 40 + random.randint(-5, 5)

        turt.forward(branch_len)

        # ---- Right branch ----
        turt.right(angle_right)
        draw_tree(branch_len - 10, turt)

        # ---- Left branch ----
        turt.left(angle_right + angle_left)
        draw_tree(branch_len - 20, turt)

        # Restore original heading and position
        turt.right(angle_left)
        turt.backward(branch_len)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # write tests below
    check_draw_tree(30)
    check_draw_tree(75)
    check_draw_tree(125)

    root.mainloop()

