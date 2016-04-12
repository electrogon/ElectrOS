#Welware, 2016
#run in Python 2 not 3

import ImageTk
from Tkinter import *
from PIL import Image
import pickle
import thread
import time

tk = Tk()

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()

canvas = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

tk.overrideredirect(1)
#show loading screen
class loading():
    def start(self):
        canvas.config(bg="white")
        logo = Image.open("icons/logo.png")
        logo = logo.resize((w/5, w/5), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(logo)

        canvas.create_image((w/2)-((w/5)/2), (h/2)-((w/5)/2), anchor=NW, image=logo1)
        tk.update()
        

ldg = loading()
ldg.start()


#read all pickle files

image = Image.open("backgrounds/default.png")
image = image.resize((w, h), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

#canvas.create_image(0, 0, image=img, anchor=NW)

def thread1():
    for x in range(0, 100):
        canvas.create_rectangle(x, 0, x+50, 50)
        tk.update()
        time.sleep(0.01)
def thread2():
    for y in range(0, 100):
        canvas.create_rectangle(y, 200, y+50, 250)
        tk.update()
        time.sleep(0.01)
        
thread.start_new_thread( thread1, () )
thread.start_new_thread( thread2, () )

tk.update()
