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
        pass


#read all pickle files

image = Image.open("backgrounds/default.png")
image = image.resize((w, h), Image.ANTIALIAS) #The (250, 250) is (height, width)
img = ImageTk.PhotoImage(image)

canvas.create_image(0, 0, image=img, anchor=NW)

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
