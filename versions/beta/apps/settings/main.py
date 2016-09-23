from tkinter import *

tk = Tk()
screenWidth = tk.winfow_screenwidth()
screenHeight = tk.winfo_screenheight()

canvas = Canvas(tk, width=screenWidth, height=screenHeight)
canvas.pack()

class Options():
    def __init__(self):
        self.options = []

tk.mainloop()


