class ReadWrite():
    def __init__(self, pickle, Image, ImageTk):
        self.pickle = pickle
        self.Image = Image
        self.ImageTk = ImageTk
    def readP(self, file):
        try:
            openFile = open(file, "rb")
        except:
            return False
        fileData = self.pickle.load(openFile)
        openFile.close()
        return fileData

    def writeP(self, data, file):
        openFile = open(file, "wb")
        self.pickle.dump(data, openFile)
        openFile.close()

    def imageTk(self, src, w, h):
        openImage = self.Image.open(src)
        width, height = openImage.size
        if width-w > 100 or height-h > 100:
            print("second way")
            resizedImage = openImage.resize((int(w*2), int(h*2)))
            resizedImage = resizedImage.resize((int(w), int(h)), self.Image.ANTIALIAS)
        else:    
            resizedImage = openImage.resize((int(w), int(h)), self.Image.ANTIALIAS)
        tkImage = self.ImageTk.PhotoImage(resizedImage)

        return tkImage
    
