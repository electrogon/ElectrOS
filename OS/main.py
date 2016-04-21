#Welware, 2016
#run in Python 2 not 3

import ImageTk
from Tkinter import *
from PIL import Image
import pickle
import thread
import time
import tkFont
import random
#import modules

from tools import *



class firstTime():
    def start(self):
        
        image = Image.open("backgrounds/default.png")
        image = image.resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)


        canvas.create_image(0, 0, image=img, anchor=NW)
        #add the background image

        canvas.configure(bg="darkgreen")

        canvas.create_text(w/20, h/30, text="Create a New User Account", anchor=NW, font=("Helvetica", w/40), fill="white")
        canvas.create_text(w/20, h/10, text="This account will be used every time you login to your Raspberry Pi", anchor=NW, font=("Helvetica", w/100), fill="white")


        keys.textBox(w/20, (h/100)*25, (w/5), h/25, "Enter a Username", 0)
        keys.textBox(w/20, (h/100)*35, (w/5), h/25, "Enter a Password", 1)
        #create a new textbox

        canvas.create_text(w/20, (h/100)*70, text="I don't want to create an account", anchor=NW, font=("Helvetica", 12, "underline"), fill="white")

        b.button(w-400, h-100, 120, 40, "darkgreen", "white", 2, "Next", firsttime1.screen2)
        
        #allDatas = keys.getAll()
    def screen2(self):
        allInfo = keys.getAll()
        
        keys.deleteAll()
        b.deleteAll()
        canvas.delete("all")
        keys.endCursor()
        
        ldg.fullScreen("Storing Data")
        #store username and password
        userData = {
            0: {
                "username": allInfo[0],
                "password": allInfo[1],
                "bg": "default.png"
            }
        }
        
        time.sleep(2)
        ldg.fullScreenStop()
        time.sleep(0.1)
        ldg.fullScreen("Downloading Files")
        
        
            
            
        
        

class clickDistribute():
    def distribute(self, event):
        
        keys.onTextClick(event)
        b.click(event)
class readData():
    def read(self):
        try:
            load_file = open('save.dat', 'rb')
            return True
        except:
            return False


def thread1():
    canvas.bind_all('<Button-1>', distributor.distribute)
    #canvas.bind_all('<Button-1>', b.click)
    canvas.bind_all("<KeyPress>", keys.onTextType)
    canvas.bind_all('<Motion>', b.checkHit)
        
thread.start_new_thread( thread1, () )
#start a seperate thread to detect clicks


ldg = loading()
#store the loading class into a variable
keys = keyBoard()
#store the keyboard class into a variable
distributor = clickDistribute()

readdata = readData()

b = Buttons()


firsttime1 = firstTime()


if readdata.read():
    pass
else:
    ldg.start()
    #start the start screen
    time.sleep(3)


    firsttime1.start()



tk.mainloop()
time.sleep(10)


