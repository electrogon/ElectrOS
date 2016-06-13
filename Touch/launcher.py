import home
from Tkinter import *

tk = Tk()
w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()

canvas=Canvas(tk, width=w, height=h)
canvas.pack()

h = home.Home()
h.start(canvas, tk)

