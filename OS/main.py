#Welware, 2016
#run in Python 2 not 3

#import all the modules
import ImageTk
from Tkinter import *
from PIL import Image
import pickle

import time
import tkFont
import random
import urllib
import hashlib
import zipfile

import thread

from tools import *
import sudo


version = "1.0"

class firstTime():
    def start(self):
        
        

        canvas.configure(bg="darkgreen")

        canvas.create_text(w/20, h/30, text="Create a New User Account", anchor=NW, font=("Helvetica", w/40), fill="white")
        canvas.create_text(w/20, h/10, text="This account will be used every time you login to your Raspberry Pi", anchor=NW, font=("Helvetica", w/100), fill="white")


        keys.textBox(w/20, (h/100)*25, (w/5), h/25, "Enter a Username", 0)
        keys.textBox(w/20, (h/100)*35, (w/5), h/25, "Enter a Password", 1)
        #create a new textbox


        b.button(w-400, h-100, 120, 40, "darkgreen", "white", 2, "Next", firsttime1.screen2)
        
        
        
        #allDatas = keys.getAll()
    def screen2(self):
        allInfo = keys.getAll()
        def success():
        
            keys.deleteAll()
            b.deleteAll()
            canvas.delete("all")
            keys.endCursor()
            sudo1 = sudo.sudoUser()
            global done
            done = False
            

            thread.start_new_thread(sudo1.addUser, (allInfo[0], allInfo[1], ldg, version, notify))
        
            ldg.fullScreen("Configuring Data")
        
       

        try:
            h= allInfo[0]
            h=allInfo[1]
            if allInfo[0] == "" or allInfo[1] == "":
                notify.Error("No Username or Password was Entered")
                raise SyntaxError("E")
            success()
            
        except:
           
            notify.Error("Username or Password was left blank")

            
            
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

ldg = loading()
#store the loading class into a variable
keys = keyBoard()
#store the keyboard class into a variable


readdata = readData()

notify = Notify()

b = Buttons()

distributor = clickDistribute()
canvas.bind_all('<Button-1>', distributor.distribute)
canvas.bind_all("<KeyPress>", keys.onTextType)
canvas.bind_all('<Motion>', b.checkHit)



firsttime1 = firstTime()


if readdata.read():
    pass
else:
    ldg.start()
    #start the start screen
    time.sleep(3)


    firsttime1.start()

tk.mainloop()



