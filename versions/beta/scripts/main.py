from tkinter import *
import pickle
import time
import _thread
import queue

#ElectrOS modules
import readwrite
import home
import bootScreen
import bootUp

from PIL import ImageTk
from PIL import Image as ImagePIL

tk = Tk()
#tk.overrideredirect(1)#fullscreen!

queue = queue.Queue(0)


screenWidth = tk.winfo_screenwidth()
screenHeight = tk.winfo_screenheight()

canvas = Canvas(tk, width=screenWidth, height=screenHeight, highlightthickness=0)
canvas.pack() #New Canvas

readWrite = readwrite.ReadWrite(pickle, ImagePIL, ImageTk)

_thread.start_new_thread(bootUp.BootUp, (queue,))#start background booting

bt = bootScreen.BootStart(canvas, tk, readWrite, time, queue) #start screen booting
bt.start()

canvas.delete("all") #when the screen is done booting...

h = home.Home(canvas, tk, readWrite, time) #prep home menu

tk.mainloop()
