
class Dialogs():
    def __init__(self, canvas, width, height, readWrite, multiUseIcons, screenInfo):
        self.canvas=canvas
        self.icoIms = []
        self.groups = []

        self.screenWidth = width
        self.screenHeight = height

        self.readWrite = readWrite
        self.multiUseIcons = multiUseIcons

        self.screenInfo = screenInfo
        
    def remove(self, group):
        print(group)
        for item in group:
            self.canvas.delete(item)
    def optionDialog(self, options):
        try:
            backgroundColor = options["background-color"]
            foregroundColor = options["foreground-color"]
            textColor = options["text-color"]
            items = options["list"]
        except:
            return "Invalid Arguments"
        
        background = self.canvas.create_rectangle((self.screenWidth/2)-(self.screenWidth/4), (self.screenHeight/2)-(self.screenHeight/4), (self.screenWidth/2)+(self.screenWidth/4), (self.screenHeight/2)+self.screenHeight/4, fill=backgroundColor, outline=backgroundColor)
        titleBG = self.canvas.create_rectangle((self.screenWidth/2)-(self.screenWidth/4), (self.screenHeight/2)-(self.screenHeight/4), (self.screenWidth/2)+(self.screenWidth/4), (self.screenHeight/2)-((self.screenHeight/100)*15), fill=foregroundColor, outline=foregroundColor)
        title = self.canvas.create_text((self.screenWidth/2)-(self.screenWidth/4)+(self.screenWidth/50), (self.screenHeight/2)-(self.screenHeight/4)+(((self.screenHeight/4)-((self.screenHeight/100)*15))/2), text="New", font=("Roboto", int(self.screenWidth/50)), fill=textColor, anchor="w")

        close = self.readWrite.imageTk(self.multiUseIcons["close"], self.screenWidth/30, self.screenWidth/30)
        self.icoIms.append(close)
        closeImg = self.canvas.create_image((self.screenWidth/2)+(self.screenWidth/4)-(self.screenWidth/50), (self.screenHeight/2)-(self.screenHeight/4)+(((self.screenHeight/4)-((self.screenHeight/100)*15))/2), image=self.icoIms[len(self.icoIms)-1], anchor="e")
        self.icoIms.append(closeImg)

        itemCounter=0

        addArray = [background, titleBG, title, closeImg]
        
        for item in items:
            y1 = (self.screenHeight/2)-((self.screenHeight/100)*15)+((self.screenHeight/100)*15)*itemCounter
            diff = ((self.screenWidth/2)-(self.screenWidth/4))-y1
            
            item1 = self.canvas.create_rectangle((self.screenWidth/2)-(self.screenWidth/4), y1, (self.screenWidth/2)+(self.screenWidth/4), y1+diff, outline=foregroundColor)
            addArray.append(item1)
            folder=self.readWrite.imageTk(self.multiUseIcons["folder"], self.screenWidth/30, self.screenWidth/30)
            addArray.append(folder)
            self.icoIms.append(folder)
            
            currIco = self.canvas.create_image((self.screenWidth/2)-(self.screenWidth/4)+self.screenWidth/50, (y1*2+diff)/2, image=self.icoIms[len(self.icoIms)-1], anchor="w")
            self.icoIms.append(currIco)
            addArray.append(currIco)

            titleText = self.canvas.create_text((self.screenWidth/2)-(self.screenWidth/4)+self.screenWidth/50+self.screenWidth/20, (y1*2+diff)/2, text="Folder", font=("Roboto", int(self.screenWidth/60)), fill=self.screenInfo["window-secondary"], anchor="w")
            addArray.append(titleText)
            itemCounter+=1

        self.canvas.tag_bind(closeImg, '<ButtonPress-1>', lambda event, grp=addArray: self.remove(grp))

class Home():
    def __init__(self, canvas, tk, readWrite, time):
        self.canvas = canvas
        self.tk = tk

        self.time = time

        self.appsFile = "../apps/appManifest.jdat"
        self.screenFile = "../assets/dat/screenManifest.jdat"
        self.logoLocation = "../assets/img/et/logo.png"

        self.deviceIco = "../assets/img/toolbar/ic_devices_3x.png"
        self.addIco =  "../assets/img/toolbar/ic_note_add_3x.png"
        self.searchIco = "../assets/img/toolbar/ic_search_3x.png"

        self.multiUseIcons = {
            "close":"../assets/img/os/ic_close_white_64dp.png",
            "folder":"../assets/img/os/ic_folder_black_48dp.png",
            "back":"../assets/img/os/ic_keyboard_return_3x.png"
            }
        
        self.readWrite = readWrite

        self.screenWidth = self.tk.winfo_screenwidth()
        self.screenHeight = self.tk.winfo_screenheight()

            
        self.appActualSize = self.screenWidth/8+60 # size of 1x1 app icon for reference
        self.appMargin = self.screenWidth/40 # distance between icons

        self.maxSize = (self.appActualSize+self.appMargin)*int((self.screenWidth/(self.appActualSize+self.appMargin)))
        
        self.groupMargin = (self.screenWidth-self.maxSize)/2
        self.topMargin=self.screenHeight/4


        self.prepFiles()

        self.appInfo = self.readWrite.readP(self.appsFile) # read apps file
        self.screenInfo = self.readWrite.readP(self.screenFile) # read screen file

        self.Dialogs = Dialogs(self.canvas, self.screenWidth, self.screenHeight, self.readWrite, self.multiUseIcons, self.screenInfo)

        self.icons = []
        self.ovIms =[]
        self.ovTk = []
        self.ovs = []
        self.icoIms = []

        self.canvas.configure(bg=self.screenInfo["bg"])
        self.createTaskBar()
        self.createIcons()

    def prepFiles(self): #ONLY for first-time use

        if self.readWrite.readP(self.appsFile) == False:
            self.appInfo = {
                "apps":[
                    {"type":"launcher", "title":"Camera", "iconSrc":"../apps/camera/assets/img/iconxxl.png", "exeComm":"echo 'app doesn't exist yet'", "size":[1, 1]},
                    {"type":"launcher", "title":"Photos", "iconSrc":"../apps/photos/assets/img/iconxxl.png", "exeComm":"", "size":[1, 1]},
                    {"type":"launcher", "title":"Settings", "iconSrc":"../apps/settings/assets/img/iconxxl.png", "exeComm":"", "size":[1, 1]},
                    {"type":"launcher", "title":"Calculator", "iconSrc":"../apps/calculator/assets/img/iconxxl.png", "exeComm":"", "size":[1, 1]},
                    {"type":"frame", "fillerCommand":None, "size":[3, 1]}
                ],
                "appBG":"#4caf50",
                "appSize":1
                }
            self.readWrite.writeP(self.appInfo, self.appsFile)

        if self.readWrite.readP(self.screenFile) == False:
            self.screenInfo = {
                "windows":"#E0E0E0",
                "window-secondary":"#212121",
                "outlines":"#BBDEFB",
                "button-inside":"#E3F2Fd",
                "button-text":"#8BC34A",
                "text-color":"#f5f5f5",
                "bg":"#1a1a1a",
                "taskBG":"#4caf50",
                }
            self.readWrite.writeP(self.screenInfo, self.screenFile)

    def createTaskBar(self):
        self.taskbarComps = [] # Taskbar components
        
        self.taskBarHeight = self.screenHeight/8 # task bar height
        self.taskIcoSize = self.taskBarHeight*0.5
        
        self.taskbarComps.append(self.canvas.create_rectangle(self.screenWidth, 0, self.screenWidth+self.screenWidth, self.taskBarHeight, fill=self.screenInfo["taskBG"], outline=self.screenInfo["taskBG"]))
        
        self.logoImg = self.readWrite.imageTk(self.logoLocation, self.taskBarHeight*1.3, self.taskBarHeight*1.3) #prep ET logo
        self.taskBarIco = self.canvas.create_image(self.screenWidth+50, self.taskBarHeight, image=self.logoImg, anchor="w") # add logo to taskbar
        self.taskbarComps.append(self.taskBarIco)

        self.taskBarIcoMargin = self.screenWidth/20

        self.searchImg = self.readWrite.imageTk(self.searchIco, self.taskIcoSize, self.taskIcoSize)
        self.taskbarComps.append(self.canvas.create_image(self.screenWidth+self.screenWidth-self.taskIcoSize-self.taskBarIcoMargin, self.taskBarHeight/2, image=self.searchImg, anchor="w"))

        self.deviceImg = self.readWrite.imageTk(self.deviceIco, self.taskIcoSize, self.taskIcoSize)
        self.taskbarComps.append(self.canvas.create_image(self.screenWidth+self.screenWidth-self.taskIcoSize*2-self.taskBarIcoMargin*1.5, self.taskBarHeight/2, image=self.deviceImg, anchor="w"))

        self.addImg = self.readWrite.imageTk(self.addIco, self.taskIcoSize, self.taskIcoSize)
        self.taskbarComps.append(self.canvas.create_image(self.screenWidth+self.screenWidth-self.taskIcoSize*3-self.taskBarIcoMargin*2, self.taskBarHeight/2, image=self.addImg, anchor="w"))
        self.canvas.tag_bind(self.taskbarComps[len(self.taskbarComps)-1], '<ButtonPress-1>', self.new)

        count=0
        speed=30
        while count<self.screenWidth:
            for task in self.taskbarComps: # get the taskbar into position
                self.canvas.move(task, -speed, 0)
            count+=speed
            self.tk.update()

    def new(self, event):
        dialogInfo = {
            "title":"New",
            "background-color":self.screenInfo["windows"],
            "foreground-color":self.screenInfo["window-secondary"],
            "text-color":self.screenInfo["text-color"],
            "list":[
                {"img":self.multiUseIcons["folder"], "title":"Folder", "onclick":None}
                ]
            }
        self.Dialogs.optionDialog(dialogInfo)
    def openApp(self, command):
        print("clicked @%s" %command)
        
    def createIcons(self):
        appX = 0
        appY = 0

        appSize = self.appInfo["appSize"]
        appBG = self.appInfo["appBG"]

        time1=self.time.time()
        
        for app in self.appInfo["apps"]:
            width = app["size"][0]*self.appActualSize
            height = app["size"][1]*self.appActualSize

            if app["type"] == "launcher":
                currOv = self.canvas.create_oval(self.groupMargin+appX*(width+self.appMargin), self.screenHeight+self.topMargin+appY*(height+self.appMargin), self.groupMargin+appX*(width+self.appMargin)+width, self.screenHeight+self.topMargin+appY*(height+self.appMargin)+height, width=0, fill=appBG, outline=appBG)

                ovIm = self.readWrite.imageTk(app["iconSrc"], width/2, height/2)
                self.ovIms.append(ovIm)

                
                imTk = self.canvas.create_image(self.groupMargin+appX*(width+self.appMargin)+width/2, self.screenHeight+self.topMargin+appY*(height+self.appMargin)+height/2-height/10, image=ovIm)                               
                self.ovTk.append(imTk)
                
                icotxt = self.canvas.create_text(self.groupMargin+appX*(width+self.appMargin)+width/2, self.screenHeight+self.topMargin+appY*(height+self.appMargin)+height/1.2-height/10, text=app["title"], font=("Roboto", int(width/10)), fill="white")
                    
                self.icons.append(currOv)
                appX+=1
                print(app)

                self.canvas.tag_bind(self.icons[len(self.icons)-1], '<ButtonPress-1>', lambda event, app=app: self.openApp(app["exeComm"]))
                
                count=0
                speed=30
                while count < self.screenHeight:
                    self.canvas.move(currOv, 0, -speed)
                    self.canvas.move(imTk, 0, -speed)
                    self.canvas.move(icotxt, 0, -speed)
                    count += speed
                    self.tk.update()

                
            if appX*(width+self.appMargin) >= self.maxSize:
                appX=0
                appY+=1

            self.tk.update()

        totTime = self.time.time()-time1

        print("App Load Time %s" % totTime)
                
