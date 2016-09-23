from tkinter import *
import sys

tk = Tk()
#tk.overrideredirect(1)

width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()

calcColor = "#1a1a1a"
calcBg = "white"

canvas = Canvas(tk, width=width, height=height, cursor="")
canvas.pack()

canvas.configure(bg=calcBg)
canvas.configure(cursor="")

class calcStorage():
    def __init__(self):
        self.equation = ""
        self.listEquations = []
    def clear(self):
        self.equation = ""
        self.listEquations.append(self.equation)

calcStr = calcStorage()

def totalC():
    try:
        canvas.itemconfig(textbox, text=eval(calcStr.equation))
        calcStr.clear()
    except:
        canvas.itemconfig(textbox, text="Err")


def addNum(num):
    calcStr.equation+=str(num)
    
    canvas.itemconfig(textbox, text=calcStr.equation)
    tk.update()

def run(text):
    if text == '=':
        predefined["="]()
    else:    
        try:
            predefined[text]()
        except:
            print(sys.exc_info())
            addNum(text)
    
                
buttons = [
    [7, 8, 9, "-"],
    [4, 5, 6, "/"],
    [1, 2, 3, "*"],
    [".", 0, "=", "+"],
    ]

predefined = {
    "PI":3.14159265358979323846,
    "=":totalC,
    }

def generate():
    xcount=0
    ycount=1
    for buttongroup in buttons:
        buttonWidthNum = width/len(buttongroup)
        buttonHeightNum = height/(len(buttons)+1)
        for button in buttongroup:
            currentRect = canvas.create_rectangle(xcount*buttonWidthNum, ycount*buttonHeightNum, (xcount+1)*buttonWidthNum, (ycount+1)*buttonHeightNum, fill=calcColor,outline=calcColor)
            currentText = canvas.create_text((xcount*buttonWidthNum+(xcount+1)*buttonWidthNum)/2, ((ycount*buttonHeightNum)+(ycount+1)*buttonHeightNum)/2, text=button, font=("Roboto", int(buttonHeightNum/2)), fill="white")
            
            canvas.tag_bind(currentRect, '<ButtonPress-1>', lambda event,text=button: run(text))
            canvas.tag_bind(currentText, '<ButtonPress-1>', lambda event,text=button: run(text))
            
            xcount+=1
        xcount=0
        ycount+=1

    return canvas.create_text(width, buttonHeightNum/2, text="", font=("Roboto", int(buttonHeightNum/2)), fill=calcColor, anchor="e")
textbox = generate()

tk.mainloop()
