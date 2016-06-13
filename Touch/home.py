import pickle
from Tkinter import *
import ImageTk
from PIL import Image
import tkFont
import time

tk = Tk()
w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()

canvas=Canvas(tk, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()
tk.overrideredirect(1)

fullScreen = 0


def go():
    canvas.delete("all")
    b = canvas.create_rectangle(0, 0, 50, 50)
    for x in range(0, 50):
        canvas.move(b, 5, 0)
        tk.update()
        time.sleep(0.05)

class Data():
    def check(self):
        #function to return user information and create user information if it doesn't exist
        try:
            dataFile = open("UserData.ET", "r")
            data = pickle.load(dataFile)
            dataFile.close()
            return data
        except:
            small = w/8
            med = w/6
            large = w/4
            
            
            data = {"bg":"default.png",
                    "screen1":{
                        "icons":["icons1.png", "icons2.png", "icons3.png", "icons4.png", "icons5.png"],
                        "size":[small, small, small, small, small], "launcher":[go, go, go, go, go],
                        "action":["icons1select.png", "icons2select.png", "icons3select.png", "icons4select.png", "icons5select.png"]},
                    "screen2":{
                        "icons":["icons1.png", "icons2.png", "icons3.png"],
                        "size":[small, small, small], "launcher":[go, go, go],
                        "action":["icons1select.png", "icons2select.png", "icons3select.png"]},
                    "profile": "unknown.png",
                    "user":"Guest"}
            dataFile = open("UserData.ET", "wb")
            pickle.dump(data, dataFile)
            dataFile.close()
            
            return data

class Home():
    def __init__(self):
        self.iconsList = []
        self.dataSize = []
        self.commands = []
        self.actions = []
        self.x = []
        self.y = []
        self.iconsImages = []
        self.howMany = 0
        self.going = True
        self.textTitles = []

        self.categories = ["Games", "Apps", "Movies"]
        self.screens = ["screen1", "screen2", "screen3"]
        self.Currenthome = 0
        self.Defhome = "screen1"
        self.screenLocations = []
        self.totalText=""
    def clear(self):
        
        self.iconsList = []
        self.dataSize = []
        self.commands = []
        self.actions = []
        self.x = []
        self.y = []
        self.iconsImages = []
        

        
    def click(self, event):
        xClick = event.x
        yClick = event.y
        
        counter=0
        
        try:

            for iconFile in self.iconsList:
                iconCoords = canvas.coords(iconFile)
            
                if xClick >= iconCoords[0] and yClick >= iconCoords[1] and xClick <= iconCoords[0]+self.dataSize[counter] and yClick <= iconCoords[1]+self.dataSize[counter]:
                    clicked =Image.open("Icons/%s" % self.actions[counter])
                    
                    clicked = clicked.resize((self.dataSize[counter], self.dataSize[counter]), Image.ANTIALIAS)
                    clicked = ImageTk.PhotoImage(clicked)
                
                    canvas.itemconfig(iconFile, image=clicked)
                
                    tk.update()
                    time.sleep(0.1)
                    self.commands[counter]()
                    time.sleep(0.1)
                    canvas.itemconfig(iconFile, image=self.iconsImages[counter])
                    self.clear()
                    tk.mainloop()
                
                    
              
                counter=counter+1
            textCounter=0
                
            for text in self.textTitles:
                
                t = canvas.coords(text)
                
                
                Textfont = tkFont.Font(family="Helvetica", size=h/25)
                tLen, tHeight = Textfont.measure(self.categories[textCounter]),Textfont.metrics("linespace")
                
                if xClick >= t[0] and yClick >= t[1] and xClick <= t[0]+tLen and yClick <= t[1]+tHeight:
                    if textCounter > self.Currenthome:
                        for transition in range(0, w/90):
                            for q in self.iconsList:
                                canvas.move(q, -(w/(w/90)), 0)
                            tk.update()
                        self.Currenthome=self.Currenthome+1
                    elif textCounter < self.Currenthome:
                        for transition in range(0, w/90):
                            for q in self.iconsList:
                                canvas.move(q, (w/(w/90)), 0)
                            tk.update()
                        self.Currenthome=self.Currenthome-1
                    print(self.Currenthome)
                    textDelcount = 0

                    font = tkFont.Font(family="Helvetica", size=h/25)
                    totalTextw, totalTexth = font.measure(self.totalText),font.metrics("linespace")

                
                    
                    for text in self.textTitles:
                        canvas.delete(self.textTitles[textDelcount])
                        self.textTitles[textDelcount] = ""
                        textDelcount = textDelcount+1
                        
                    for text in self.categories:
                        textw, texth = font.measure(text),font.metrics("linespace")
            
                        if Textcounter == self.Currenthome:
                            self.textTitles.append(canvas.create_text(centeredText+textOffset, int((h/2)-(h/3)), text=text+"   ", font=("Helvetica", h/25, "bold"), fill="#1a1a1a", anchor=NW))
                        else:
                            self.textTitles.append(canvas.create_text(centeredText+textOffset, int((h/2)-(h/3)), text=text+"   ", font=("Helvetica", h/25), fill="#1a1a1a", anchor=NW))
                        textOffset=textOffset+textw+50
                        Textcounter=Textcounter+1
                        
                textCounter=textCounter+1
                
        except:
            print(sys.exc_info())
            pass
                
            
        
    def start(self):
        print("home has started")
        w = tk.winfo_screenwidth()
        h = tk.winfo_screenheight()
        # get the width and height of the User's screen

        DataCheck = Data()
        data = DataCheck.check()
        #get all the data about them (apps, username, passwor, etc)
        
        background = Image.open("Backgrounds/%s" % data["bg"])
        background = background.resize((w, h), Image.ANTIALIAS)
        background = ImageTk.PhotoImage(background)

        imgBackground = canvas.create_image(0, 0, anchor=NW, image=background)
        # add the background image the user chose or default

        dataApps = data[self.screens[self.Currenthome]]
        profile = data["profile"]
        dataIcons = dataApps["icons"]

        
        self.dataSize = dataApps["size"]
        self.commands = dataApps["launcher"]
        self.actions = dataApps["action"]


        

        for b in self.categories:     
            self.totalText = self.totalText+b
        # combine all the category text into one string for measurement purposes


        font = tkFont.Font(family="Helvetica", size=h/25)
        totalTextw, totalTexth = font.measure(self.totalText),font.metrics("linespace")
        #measure the length of the categories
        totalTextw=totalTextw+50

        centeredText = (w/2)-(totalTextw/2)
        textOffset = 0
        Textcounter=0

        Profileicon = Image.open("profiles/%s" % profile)
        Profileicon = Profileicon.resize((int(w/15), int(w/15)), Image.ANTIALIAS)
        Profileicon = ImageTk.PhotoImage(Profileicon)
        # add the users' usericon

        canvas.create_image(int(w-(w/15+w/40)), int(w/40), image=Profileicon, anchor=NW)

        Logoicon = Image.open("Icons/logo.png")
        Logoicon = Logoicon.resize((int(w/12), int(w/12)), Image.ANTIALIAS)
        Logoicon = ImageTk.PhotoImage(Logoicon)

        canvas.create_image(w/50, w/50, image=Logoicon, anchor=NW)
        # add the ElectrOS logo in the top left corner

        for text in self.categories:
            textw, texth = font.measure(text),font.metrics("linespace")
            
            if Textcounter == self.Currenthome:
                self.textTitles.append(canvas.create_text(centeredText+textOffset, int((h/2)-(h/3)), text=text+"   ", font=("Helvetica", h/25, "bold"), fill="#1a1a1a", anchor=NW))
            else:
                self.textTitles.append(canvas.create_text(centeredText+textOffset, int((h/2)-(h/3)), text=text+"   ", font=("Helvetica", h/25), fill="#1a1a1a", anchor=NW))
            textOffset=textOffset+textw+50
            Textcounter=Textcounter+1
        # generate all the text for the categories at the top of the screen
        
        
        
        for g in range(0, len(data)-3):
            self.screenLocations.append("screen"+str(g))
        print(self.screens)

        for dataCount in range(0, len(data)-3):
            iconsImages = []
            maximum = 4
            counter=0
            defx = (w-(self.dataSize[maximum]+(self.dataSize[maximum]/6)))/4
            defy = (h/2)-(h/5)
            x = defx+(w*dataCount)
            y = defy
            print(len(data)-3)
            dataApps = data[self.screens[self.Currenthome]]
            dataIcons = dataApps["icons"]
            
        
            for icon in range(0, len(dataIcons)):
                counter=counter+1
            
                Currenticon = Image.open("Icons/%s" % dataIcons[icon])
                Currenticon = Currenticon.resize((self.dataSize[icon], self.dataSize[icon]), Image.ANTIALIAS)
                self.iconsImages.append(ImageTk.PhotoImage(Currenticon))

                self.iconsList.append(canvas.create_image(x, y, anchor=NW, image=self.iconsImages[icon]))
                self.x.append(x)
                self.y.append(y)
                if counter >= maximum:
                    x=defx+(w*dataCount)
                    y=y+self.dataSize[icon]+(self.dataSize[icon]/6)
                else:
                    x=x+self.dataSize[icon]+(self.dataSize[icon]/6)
        canvas.bind_all('<Button-1>', self.click)
        
            

        tk.mainloop()

Home().start()
