#Welware, 2016
#run in Python 2 not 3

import ImageTk
from Tkinter import *
from PIL import Image
import pickle
import thread
import time
#import modules

tk = Tk()

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()
# get the screen width and height to make it fullscreen

canvas = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

#create an empty canvas without border

tk.overrideredirect(1)
#remove topBar


class keyBoard():
    def __init__(self):
        self.boxes = []
        #empty array to store textboxes
    def onTextClick(self, event):
        print("clicked")
        for x in self.boxes:
            currentCoords = canvas.coords(x)
            if event.x >= currentCoords[0] and event.y >= currentCoords[1] and event.x <= currentCoords[2] and event.y <= currentCoords[3]:
                print("done")
        
                                  
    def textBox(self, x, y, width, height):
                                  
        self.boxes.append(canvas.create_rectangle(x, y, x+width, y+height, fill="white"))
        
        
        

class loading():
    def start(self):
        canvas.config(bg="white")
        logo = Image.open("icons/logo.png")
        logo = logo.resize((w/5, w/5), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(logo)

        canvas.create_image((w/2)-((w/5)/2), (h/2)-((w/5)/2), anchor=NW, image=logo1)
        tk.update()
        
class readData():
    def read(self):
        try:
            load_file = open('save.dat', 'rb')
        except:
            
            homeInfo = {"background":"default.png"}

ldg = loading()
#store the loading class into a variable

keys = keyBoard()
#store the keyboard class into a variable

keys.textBox(50, 50, 100, 30)
#create a new textbox

canvas.bind_all('<Button-1>', keys.onTextClick)
#detect clicks and call the onTextclick function when something is pressed

ldg.start()
#start the loading screen



image = Image.open("backgrounds/default.png")
image = image.resize((w, h), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

#add the background image

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

    #threading test (not important to be deleted)
        
thread.start_new_thread( thread1, () )
thread.start_new_thread( thread2, () )

tk.update()
