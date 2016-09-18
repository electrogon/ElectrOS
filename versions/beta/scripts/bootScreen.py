import random

class BootStart():
    def __init__(self, canvas, tk, readWrite, time, queue):
        self.canvas = canvas
        self.tk = tk
        self.readWrite = readWrite
        self.time = time
        self.queue = queue

        self.screenWidth = self.tk.winfo_screenwidth()
        self.screenHeight = self.tk.winfo_screenheight()

        self.logoLocation = "../assets/img/et/logo.png"


        self.defaultBG = "#1a1a1a"
        self.logo = self.readWrite.imageTk(self.logoLocation, self.screenWidth/5, self.screenWidth/5)

        self.logoExiting = False
        self.logoExitCount = 0

        self.speed = 40
        
    def start(self):
        self.canvas.configure(bg=self.defaultBG)
        self.startLogo = self.canvas.create_image(self.screenWidth/2, self.screenHeight/2, image=self.logo)

        while True:
            if self.logoExiting == True:
                if self.logoExitCount < (self.screenHeight/4)*3:
                    self.canvas.move(self.startLogo, 0, -self.speed)
                    self.logoExitCount+=self.speed
                else:
                    break
            elif self.queue.empty() == False:
                if self.queue.get() == "cleanup":
                    self.logoExiting = True
                    
                
            self.tk.update()
            self.tk.update_idletasks()
