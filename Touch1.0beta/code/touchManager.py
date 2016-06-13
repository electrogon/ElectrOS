from Tkinter import *
import canvasFuncs

class DetectClicks():               
    def click_detect(self, event):
        self.canvasFuncs = canvasFuncs.CanvasFuncs()
        self.clickX = event.x
        self.clickY = event.y
        
        print(self.canvasFuncs.icons)
        for icon in self.canvasFuncs.icons:
            print(icon)



