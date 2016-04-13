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
        # called when screen is clicked
        for box in self.boxes:
            #check every textbox
            currentCoords = canvas.coords(box)
            # get the coordinates of the current textbox
            if event.x >= currentCoords[0] and event.y >= currentCoords[1] and event.x <= currentCoords[2] and event.y <= currentCoords[3]:
                #if the current textbox is clicked
                print("done")
        
                                  
    def textBox(self, x, y, width, height):
        #create a text box
        self.boxes.append(canvas.create_rectangle(x, y, x+width, y+height, fill="white"))
        #add it to text box array
        
        
        

class loading():
    def start(self):
        canvas.config(bg="white")
        logo = Image.open("icons/logo.png")
        logo = logo.resize((w/5, w/5), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(logo)

        imglogo = canvas.create_image((w/2)-((w/5)/2), (h/2)-((w/5)/2), anchor=NW, image=logo1)
        #img2logo = canvas.create_image(0, 0, anchor=NW, image=logo1)
        tk.update()

class firstTime():
    def start(self):
        image = Image.open("backgrounds/default.png")
        image = image.resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)


        canvas.create_image(0, 0, image=img, anchor=NW)
        #add the background image

        keys.textBox((w/2)-(w/20), (h/2)-(w/100), (w/10), w/50)
        #create a new textbox
        
class readData():
    def read(self):
        try:
            load_file = open('save.dat', 'rb')
        except:
            
            homeInfo = {"background":"default.png"}

def thread1():
    canvas.bind_all('<Button-1>', keys.onTextClick)
        
thread.start_new_thread( thread1, () )
#start a seperate thread to detect clicks


ldg = loading()
#store the loading class into a variable
keys = keyBoard()
#store the keyboard class into a variable
firsttime1 = firstTime()


ldg.start()
#start the start screen
time.sleep(3)

firsttime1.start()

tk.mainloop()
time.sleep(10)


