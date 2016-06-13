import pickle #pickle module for storing information on computer, desktop backgrounds, themes, etc..

class Io():
    def __init__(self):
        self.defUsers = [
            {"user": "unnamed pi", "icon": ""}
            ]
    def check(self):  
        try:
            #Check if this is the first time the user has opened the ELectrOS
            users_file = open('data/users.et', 'rb')
            return users_file
        except:
            # if not return 0 to indicate that the file is not present
            return 0
            

    def write(self, fileName, storeData):
        users_file = open('data/'+fileName, 'wb')

        
