# Welware, 2016
# This is used to store the canvas(to draw) and stores functions like textBoxes and Buttons

import ImageTk
from Tkinter import *
from PIL import Image
import pickle

import time
import tkFont
import random


tk = Tk()
global w
global h

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()
canvas = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

#create an empty canvas without border

tk.overrideredirect(1)
#remove topBar

currentCoords = ""
buttonsDone = False
cursorStatus = True

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
        self.textBoxTypes = []
        self.cursorStatus = True

        self.defText = []

        self.width = 0
        
        #empty array to store textboxes
    def onTextClick(self, event):
       
        # called when screen is clicked
        counnter=0
        print(len(self.boxes))
        for box in self.boxes:
            #check every textbox
            self.currentCoords = canvas.coords(box)
            # get the coordinates of the current textbox
            print(self.boxes)
           
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
                    
                
                while self.cursorStatus:
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
    def endCursor(self):
        self.cursorStatus = False
        try:
            canvas.delete(self.cursor)
        except:
            pass
        self.cursor = ""

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

            if self.textBoxTypes[self.current] == 0:
                self.textBoxText[self.current] = canvas.create_text(int(self.currentCoords[0]+5), int(self.currentCoords[1]+5), anchor=NW, text=str1, font=("Helvetica", h/60))
            else:
                self.textBoxText[self.current] = canvas.create_text(int(self.currentCoords[0]+5), int(self.currentCoords[1]+5), anchor=NW, text="*"*len(str1), font=("Helvetica", h/60))
                str1 = "*"*len(str1)
        
            wText, hText = font.measure(str1),font.metrics("linespace")

        

        
            #canvas.delete(self.cursor)
            self.cursorMargin = wText+5
        
            #self.cursor = canvas.create_line(self.currentCoords[0]+self.cursorMargin, self.currentCoords[1]+5, self.currentCoords[0]+self.cursorMargin, self.currentCoords[3]-5)
           
    def getAll(self):
        alldata = []
        for keys in self.textBoxKeys:
            alldata.append(keys)
        return alldata
        
    def deleteAll(self):        
        self.textBoxKeys = []
        self.boxes = []
        self.textBoxCode = []
        self.textBoxText = []
        self.textBoxTypes = []
        self.defText = []
            

        
                                  
    def textBox(self, x, y, width, height, default, typeB):
        #create a text box
        self.width = width
        self.default = default
        self.x1 = x
        self.y1 = y
        self.height = height
        self.width = width
        self.textBoxTypes.append(typeB)
        
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
        canvas.create_text(int(x+(width/2)), int(y+(height/2)), text=text, font=("Helvetica", height/3, "bold"))
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
    def deleteAll(self):
        self.buttonsList = []
        self.hoverColor = []
        self.normalColor = []
        self.commands = []
        
    
    def checkHit(self, event):
        
        self.xMouse, self.yMouse = event.x, event.y
        x =0
        for allButtons in self.buttonsList:
            try:
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
            except:
                pass
               
        
going =  True
b= Buttons()

class Notify():
    def __init__(self):
        self.messages = []
        self.messageTitle = []
        self.messageText = []
        self.messageImg = []
    def Error(self, messageP):
        if len(self.messages) == 0:
        
            self.messages.append(canvas.create_rectangle(0-(w/3), (h-50), 0, h-130, fill="#1a1a1a", outline="#1a1a1a"))

            self.messageTitle.append(canvas.create_text(0-(w/3)+10, h-110, text="Error", font=("Helvetica", int(len(messageP)/2)), anchor=W, fill="white"))
            self.messageText.append(canvas.create_text(0-(w/3)+10, h-75, text=messageP, font=("Helvetica", int(len(messageP)/2.5)), anchor=W, fill="grey"))

        

            messageImg = Image.open("system/Error.png")
            messageImg = messageImg.resize((40, 40), Image.ANTIALIAS)
            messageImg = ImageTk.PhotoImage(messageImg)
            self.messageImg.append(canvas.create_image(0-70, h-110, anchor=NW, image=messageImg))

            currentBoxIndex = len(self.messages)-1
        
            pos1 = 0
            while True:
            
                currentMessagePos= canvas.coords(self.messages[currentBoxIndex])
                if currentMessagePos[0] < -5:
                    time.sleep(0.01)
                    canvas.move(self.messages[currentBoxIndex], 10, 0)
                    canvas.move(self.messageText[currentBoxIndex], 10, 0)
                    canvas.move(self.messageTitle[currentBoxIndex], 10, 0)
                    canvas.move(self.messageImg[currentBoxIndex], 10, 0)
                    pos1=pos1+5
                    tk.update()
                
                else:
                    break

            time.sleep(5)
            while True:
            
                currentMessagePos= canvas.coords(self.messages[currentBoxIndex])
                if currentMessagePos[2] > -5:
                    time.sleep(0.01)
                    canvas.move(self.messages[currentBoxIndex], -10, 0)
                    canvas.move(self.messageText[currentBoxIndex], -10, 0)
                    canvas.move(self.messageTitle[currentBoxIndex], -10, 0)
                    canvas.move(self.messageImg[currentBoxIndex],- 10, 0)
                    pos1=pos1+5
                    tk.update()
                
                else:
                    break
            self.messages = []
            self.messageText = []
            self.messageTitle = []
            self.messageImg = []
                                 
        
                
        

class loading():
    def __init__(self):
        self.going = True
    def start(self):
        canvas.config(bg="white")
        logo = Image.open("icons/logo.png")
        logo = logo.resize((w/5, w/5), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(logo)

        imglogo = canvas.create_image((w/2)-((w/5)/2), (h/2)-((w/5)/2), anchor=NW, image=logo1)
        
        tk.update()
    def fullScreenStart(self, text):
        message = canvas.create_text(w/2, h/2, text=text, font=("Segoe UI", w/27), fill="white")
        colors = ["#ffcc00", "#3399ff", "#66ff66", "#ff66ff", "#3333ff"]
        rColor = 100
        gColor = 100
        bColor = 100

        n1C = 1
        n2C = 1
        n3C = 1
        global going
        while going:
            

            
            n1 = random.randint(1, 2)
            n2 = random.randint(3, 4)
            n3 = random.randint(4, 5)

            rColor = rColor+(n1C*n1)
            gColor = gColor+(n2C*n2)
            bColor = bColor+(n3C*n3)

            if rColor >= 230:
                n1C = -1
            if gColor >= 230:
                n2C = -1
            if bColor >= 230:
                n3C = -1
                
            if rColor <= 30:
                n1C = 1
            if gColor <= 30:
                n2C = 1
            if bColor <= 30:
                n3C = 1
            
            
            #currentColor = colors[n1]
            currentColor = '#%02x%02x%02x' % (rColor, gColor, bColor)
            canvas.configure(bg=currentColor)
            tk.update()
            time.sleep(0.03)
        canvas.delete(message)
    def fullScreen(self, text):
        global going
        going= True
        ldg = loading()
        ldg.fullScreenStart(text)
        
        #loading screen must be in a thread so that other actions can take place at the same time
    def fullScreenStop(self):
        global going
        going = False
