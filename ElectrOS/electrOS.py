#ElectrOS, 2016

from tkinter import *

tk = Tk()

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()

canvas = Canvas(tk, width=w, height=h)
canvas.pack()

tk.overrideredirect(1)
