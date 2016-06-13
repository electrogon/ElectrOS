import time
# this file keeps track of security files and makes sure that they are not changed by third party applications

class Master():
    
    def __init__(self):
        self.counter = 0
    def canvasCheck(self):
        #checks for canvas overloads(too many objects)
        self.r = True
        self.b=0
        while self.r:
            self.r = canvas.coords(x)
            self.b=b+1
        return self.b
    def repairCanvas(self):
        #removes canvas overloads(too many objects)
        self.r = True
        self.b=0
        while self.r:
            self.r = canvas.coords(x)
            self.b=b+1
        if self.b >= 500: # way too many objects!
            while self.b >= 500:
                canvas.delete(self.b-1)
                
    def security(self):
        # function to check all important system files and make sure they are not tampered with by any installed app
        security_file_first = open('sudo.py', 'rb') # open the important sudo file first in order to compare it to later files
        security_file_first = security_file_first.read()
        while True:
            try:
                self.counter=self.counter+1
                users_file = open('data/users.et', 'rb')
                if self.counter == 1:
                    users_file_first = users_file
                    
                if users_file_first.read() != users_file.read():
                    # an app is changing system files
                    return 10
                    print("alert")
                users_file.close()
            except:
                #This is the first time and the user has not yet chosen information
                pass
            security_file = open('sudo.py', 'rb')
            
            #make sure that no external app is tampering with security files
            if security_file.read() != security_file_first:
                print("Salert")
                
            security_file.close()
            
            time.sleep(1)
        

