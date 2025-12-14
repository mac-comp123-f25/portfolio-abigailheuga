import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Canvas")

        self.myCanvas = tk.Canvas(self.mainWin, bg="lightblue", width=400, height=300)
        self.myCanvas.grid(row=0, column=0)

        self.textID = self.myCanvas.create_text(
            200, 150,
            text="Hello Minnesota :)",
            fill="darkblue",
            font=("Arial", 20, "bold")
        )

        self.mainWin.bind("w", self.move_callback)
        self.mainWin.bind("a", self.move_callback)
        self.mainWin.bind("s", self.move_callback)
        self.mainWin.bind("d",self.move_callback)

        self.mainWin.bind("<Up>", self.move_callback)
        self.mainWin.bind("<Down>", self.move_callback)
        self.mainWin.bind("<Left>", self.move_callback)
        self.mainWin.bind("<Right>", self.move_callback)

        quit_button = tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)
        quit_button.grid(row=1, column=0)

    def move_callback(self, event):
        key_pressed = event.keysym
        print("Key pressed", key_pressed)

        if key_pressed in ("w", "Up"):
            self.myCanvas.move(self.textID, 0, -10)
        elif key_pressed in ("s", "Down"):
            self.myCanvas.move(self.textID, 0, 10)
        elif key_pressed in ("a", "Left"):
            self.myCanvas.move(self.textID, -10, 0)
        elif key_pressed in ("d", "Right"):
            self.myCanvas.move(self.textID, 10, 0)

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()