#Welware, 2016
#run in Python 2 not 3

import ImageTk
from Tkinter import *
from PIL import Image
import pickle
import thread
import time
import tkFont
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

currentCoords = ""
buttonsDone = False

class keyBoard():
    def __init__(self):
        self.boxes = []
        self.cursor = ""
        self.current = 0
        self.cursorMargin = 5;
        self.active = False

        self.textBoxKeys = []
        self.textBoxCode = []
        self.textBoxText  = []

        self.defText = []

        self.width = 0
        
        #empty array to store textboxes
    def onTextClick(self, event):
        print("clicked")
        # called when screen is clicked
        counnter=0
        for box in self.boxes:
            #check every textbox
            self.currentCoords = canvas.coords(box)
            # get the coordinates of the current textbox
           
            if event.x >= self.currentCoords[0] and event.y >= self.currentCoords[1] and event.x <= self.currentCoords[2] and event.y <= self.currentCoords[3]:
                # if the mouseclick was inside a textbox
                if self.cursor:
                    #if a text-cursor is already present one the screen
                    canvas.delete(self.cursor)
                    #delete it(otherwise there are two cursors on the screen
                
                
        
                try:
                    self.current = self.textBoxCode.index(box)
                    # if the textbox has already been clicked
                    font = tkFont.Font(family="Helvetica", size=h/60)
                    wText, hText = font.measure(self.textBoxKeys[self.current]),font.metrics("linespace")
                    print("this",wText)
                    print(self.textBoxText[self.current])

        
                    #canvas.delete(self.cursor)
                    self.cursorMargin = wText+5
                except:
                    self.textBoxCode.append(box)
                    # add the textbox to the textboxcode array to indicate it has already been clicked
                    self.textBoxText.append(canvas.create_text(self.currentCoords[0]+5, self.currentCoords[1]+5, text=""))
                    #add an empty text function to store all of the text that is typed in the textbox 
                    
                    self.current = self.textBoxCode.index(box)
                    #get the array index of the current textbox to access other arrays
                    print(self.current)
                    self.textBoxKeys.append("")
                    font = tkFont.Font(family="Helvetica", size=h/60)
                    wText, hText = font.measure(""),font.metrics("linespace")
                    

        
                    #canvas.delete(self.cursor)
                self.cursorMargin = wText+5
                    
                
                while True:
                    # add

                    for cursors in range(0, 100):
                        self.cursor = canvas.create_line(self.currentCoords[0]+self.cursorMargin, self.currentCoords[1]+5, self.currentCoords[0]+self.cursorMargin, self.currentCoords[3]-5)
                        # create a line cursor
                        tk.update()
                    
                        time.sleep(0.005)
                        canvas.delete(self.cursor)
                    
                    canvas.delete(self.cursor)
                    tk.update()
                    time.sleep(0.5)

    def onTextType(self, event):
        font = tkFont.Font(family="Helvetica", size=h/60)
        

        text = event.char.split('')
        
        if len(self.textBoxKeys) != 0:
            font.measure(self.textBoxKeys[self.current])
            if event.keysym == "BackSpace":
                self.textBoxKeys[self.current]=self.textBoxKeys[self.current][:-1]
            elif len(event.char) > 2 or font.measure(self.textBoxKeys[self.current]) >= self.width-10 or len(text) > 1:
                pass
            else:
                self.textBoxKeys[self.current]=self.textBoxKeys[self.current]+event.char
            
            try:
                canvas.delete(self.defText[self.current])
            except:
                pass
            canvas.delete(self.textBoxText[self.current])
        
            str1 = self.textBoxKeys[self.current]

        
            self.textBoxText[self.current] = canvas.create_text(int(self.currentCoords[0]+5), int(self.currentCoords[1]+5), anchor=NW, text=str1, font=("Helvetica", h/60))

        
            wText, hText = font.measure(str1),font.metrics("linespace")

        

        
            #canvas.delete(self.cursor)
            self.cursorMargin = wText+5
        
            #self.cursor = canvas.create_line(self.currentCoords[0]+self.cursorMargin, self.currentCoords[1]+5, self.currentCoords[0]+self.cursorMargin, self.currentCoords[3]-5)
           
    def getAll(self):
        alldata = []
        for keys in self.textBoxKeys:
            alldata.append(keys)
        return alldata
        
                

        
                                  
    def textBox(self, x, y, width, height, default):
        #create a text box
        self.width = width
        self.default = default
        self.x1 = x
        self.y1 = y
        self.height = height
        self.width = width
        
        self.boxes.append(canvas.create_rectangle(x, y, x+width, y+height, fill="white", outline="white"))
        self.defText.append(canvas.create_text(x+w/200, y+height/2, text=default, font=("Helvetica", height/3), anchor=W, fill="grey"))
        #add it to text box array

class Buttons():
    def __init__(self):
        self.buttonsList = []
        self.hoverColor = []
        self.normalColor = []
        self.commands = []
        
    def button(self, x, y, width, height, bcolor, fcolor, borderWidth, text, command):
        self.buttonsList.append(canvas.create_rectangle(x, y, x+width, y+height, fill=bcolor, outline=fcolor, width=borderWidth))
        canvas.create_text(x+(width/2), y+(height/2), text=text, font=("Helvetica", height/3, "bold"))
        self.hoverColor.append(fcolor)
        self.normalColor.append(bcolor)
        self.commands.append(command)
        print(self.buttonsList, "head")

    def click(self, event):
        self.xMouse, self.yMouse = event.x, event.y
        
        for allButtons in self.buttonsList:
            
            self.buttonCoords = canvas.coords(allButtons)
            if self.xMouse >= self.buttonCoords[0] and self.yMouse >= self.buttonCoords[1] and self.xMouse <= self.buttonCoords[2] and self.yMouse <= self.buttonCoords[3]:
                self.commands[self.buttonsList.index(allButtons)]()
                canvas.itemconfig(allButtons, fill="white")
                
            
        
    
    def checkHit(self, event):
        
        self.xMouse, self.yMouse = event.x, event.y
        x =0
        for allButtons in self.buttonsList:
            
            self.buttonCoords = canvas.coords(allButtons)
            try:
                if self.xMouse >= self.buttonCoords[0] and self.yMouse >= self.buttonCoords[1] and self.xMouse <= self.buttonCoords[2] and self.yMouse <= self.buttonCoords[3]:
                
                    canvas.itemconfig(allButtons, fill=self.hoverColor[self.buttonsList.index(allButtons)])
                    tk.config(cursor="hand2")
                else:
                    canvas.itemconfig(allButtons, fill=self.normalColor[self.buttonsList.index(allButtons)])
                    tk.config(cursor="")
            except:
                self.buttonsList.remove(self.buttonsList[x])
                self.hoverColor.remove(self.hoverColor[x])
                self.normalColor.remove(self.normalColor[x])
                self.commands.remove(self.commands[x])
            x=x+1
               
        

class loading():
    def start(self):
        canvas.config(bg="white")
        logo = Image.open("icons/logo.png")
        logo = logo.resize((w/5, w/5), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(logo)

        imglogo = canvas.create_image((w/2)-((w/5)/2), (h/2)-((w/5)/2), anchor=NW, image=logo1)
        
        tk.update()

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


        keys.textBox(w/20, (h/100)*25, (w/5), h/25, "Enter a Username")
        keys.textBox(w/20, (h/100)*35, (w/5), h/25, "Enter a Password")
        #create a new textbox

        canvas.create_text(w/20, (h/100)*70, text="I don't want to create an account", anchor=NW, font=("Helvetica", 12, "underline"), fill="white")

        b.button(w-400, h-100, 120, 40, "darkgreen", "white", 2, "Next", firsttime1.screen2)
        
        #allDatas = keys.getAll()
    def screen2(self):
        print(keys.getAll())
        #canvas.delete("all")        

class clickDistribute():
    def distribute(self, event):
        
        keys.onTextClick(event)
        b.click(event)
class readData():
    def read(self):
        try:
            load_file = open('save.dat', 'rb')
        except:
            
            homeInfo = {"background":"default.png"}


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

b = Buttons()


firsttime1 = firstTime()


ldg.start()
#start the start screen
time.sleep(3)


firsttime1.start()



tk.mainloop()
time.sleep(10)


