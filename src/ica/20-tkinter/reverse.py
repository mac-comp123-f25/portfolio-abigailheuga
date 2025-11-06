import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Reverse Strings")

        instrLabel = tk.Label(self.mainWin, text="Type a phrase to reverse:")
        instrLabel.grid(row=0, column=0)

        self.entryBox = tk.Entry(self.mainWin, width=30)
        self.entryBox.grid(row=1, column=0)

        self.resultLabel = tk.Label(self.mainWin, text="")
        self.resultLabel.grid(row=2, column=0)

        quitButton = tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)
        quitButton.grid(row=3, column=0)

        self.entryBox.bind("<Return>", self.entry_response)
        self.entryBox.bind("<Tab>", self.entry_response)

    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        text = self.entryBox.get()
        reversed_text = text[::-1]
        self.resultLabel.config(text=reversed_text)

# ----- Main program -----
myGui = BasicGui()
myGui.run()