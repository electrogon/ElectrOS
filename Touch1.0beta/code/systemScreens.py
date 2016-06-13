import canvasFuncs #ElectrOS develop module for 2d graphics
import dataWriter # ElectrOS develop module to write to the internal memory
import keyboard # ElectrOS develop module for text boxes

import time
import random
import os
import winsound, sys
import tkFont
import loading

canvasFuncs = canvasFuncs.CanvasFuncs() #store Canvasfuncs class into Array

tk, canvas = canvasFuncs.newScreen() #create a new screen to draw on

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()


inOut = dataWriter.Io()

ldg = loading.loading()

class DefScreens():
    def __init__(self):
        self.current = 0
        self.colors = ["#006600", "#3366ff", "#9933ff" "#ff6600", "#ffff00", "#669999"]

        #loading screen variables
        self.gravity = -0.45
        self.speed =5

        self.sparks = []
        
    def boot_animation(self):
        canvas.configure(bg="black")
        circle = 0
        
        for x in range(0, 10):
            if circle != 0:
                canvas.delete(circle)
            color = self.colors[random.randint(0, len(self.colors)-1)]
            circle = canvas.create_oval((w/2)-(x*20)/2, (h/2)-(x*20)/2, (w/2)-(x*20)/2+(x*20), (h/2)-(x*20)/2+(x*20), fill=color, outline=color)
            tk.update()
            time.sleep(0.1/(x+1))
        time.sleep(0.3)
        
        while True:
            canvas.move(circle, 0, self.speed)
            self.speed=self.speed-self.gravity
               
            if canvas.coords(circle)[3] >= h:
                self.speed=self.speed*-1
                
                newColor = self.colors[random.randint(0, len(self.colors)-1)]
                
                canvas.itemconfig(circle, fill=newColor)
                canvas.itemconfig(circle, outline=newColor)
            if canvas.coords(circle)[1] <= h/3:
                

                canvasFuncs.createImage("images/logo/system/ElectrOS-Logo/logo.png", int(canvas.coords(circle)[0]), int(canvas.coords(circle)[1]), int(canvas.coords(circle)[2]-canvas.coords(circle)[0]), int(canvas.coords(circle)[3]-canvas.coords(circle)[1]))
                canvas.delete(circle)
                tk.update()

                winsound.PlaySound('sound/system/boot_screen.wav', winsound.SND_FILENAME)
                break

            tk.update()
            time.sleep(0.05)
        canvasFuncs.newScreen()

    def menu(self):
        if inOut.check() == 0:
            self.first_setup()
            #defData = {""}
            #inOut.write("data/users.et", defData)
        else:
            canvasFuncs.createImage("images/backgrounds/system/default.png", 0, 0, canvasFuncs.screenWidth, canvasFuncs.screenHeight)
            canvasFuncs.createImage("images/logo/system/ElectrOS-Logo/logo.png", 20, 20, canvasFuncs.screenWidth/10, canvasFuncs.screenWidth/10)
        
            currentIconX = 0
            currentIconY = 0

            iconWidth = h/10
            iconHeight = h/10

            iconCounter=0
        
            while currentIconX < (h/100)*70:
                while currentIconY < (w/100)*80:
                    iconCounter=iconCounter+1
                    canvasFuncs.createIcon("images/logo/system/iconLogo/icons"+str(iconCounter)+".png", currentIconX, currentIconY, iconWidth, iconHeight, "")

    def distribute(self, event):   
        canvasFuncs.onTextClick(event)
        canvasFuncs.click(event)

    def loop(self):
        canvas.bind_all('<Button-1>', self.distribute)
        canvas.bind_all("<KeyPress>", canvasFuncs.onTextType)
        canvas.bind_all('<Motion>', canvasFuncs.checkHit)
        tk.mainloop()


class FirstTime():
    def __init__(self):
        self.fontBig = tkFont.Font(family="Gill Sans MT",size=w/20 ,weight="normal")
        self.fontMediumBig = tkFont.Font(family="Gill Sans MT",size=w/40 ,weight="normal")
        self.fontMedium = tkFont.Font(family="Gill Sans MT",size=w/80 ,weight="normal")
        self.fontSmall = tkFont.Font(family="Gill Sans MT",size=w/100 ,weight="normal")

        
    def screen1(self, version):
        canvas.configure(bg="darkgreen")
        canvasFuncs.createText(w/2, (h/100)*50, "Welcome to ElectrOS!", "white", self.fontBig, False)
        canvasFuncs.createText(w/2, (h/100)*60, "Version " + str(version) + ", Agonis", "white", self.fontSmall, False)
            
        canvasFuncs.createButton(w-400, h-100, 120, 40, "darkgreen", "white", 2, "Next", self.screen2)
    def screen2(self):
        canvasFuncs.newScreen()
        print("peforming buttton wipe")
        #canvasFuncs.deleteAll()
        canvasFuncs.buttonsList = []
        canvasFuncs.hoverColor = []
        canvasFuncs.normalColor = []
        canvasFuncs.commands = []
        
        canvas.configure(bg="darkgreen")
        # turn the background green for the installation process

        canvasFuncs.createText(w/20, h/30, "Create a New User Account", "white", self.fontMediumBig, True)
        canvasFuncs.createText(w/20, h/10, "This account will be used every time you login to your Raspberry Pi", "white", self.fontSmall, True)

        canvasFuncs.textBox(w/20, (h/100)*25, (w/5), h/25, "Enter a Username", 0)
        canvasFuncs.textBox(w/20, (h/100)*35, (w/5), h/25, "Enter a Password", 1)
        #create a new textbox

        canvasFuncs.createButton(w-400, h-100, 120, 40, "darkgreen", "white", 2, "Next", self.screen3)
        
    def screen3(self):
        allInfo = canvasFuncs.getAll()
        
        def success():
            canvasFuncs.createText(w/20, (h/100)*50, "Success", "blue", self.fontMedium, True)
            canvasFuncs.deleteAll()
            #b.deleteAll()
            canvasFuncs.newScreen()
            canvasFuncs.endCursor()
            canvasFuncs.buttonsList = []
            canvasFuncs.hoverColor = []
            canvasFuncs.normalColor = []
            canvasFuncs.commands = []
            
            canvasFuncs.fullScreen("Configuring Data")
        
       

        try:
            if allInfo[0] == "" or allInfo[1] == "":
                canvasFuncs.createText(w/20, (h/100)*45, "Username or Password was left blank", "red", self.fontSmall, True)

            success()
                
        except:
            print(sys.exc_info())
            canvasFuncs.createText(w/20, (h/100)*45, "Username or Password was left blank", "red", self.fontSmall, True)

    

    
