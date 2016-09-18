import urllib
import hashlib
import pickle
import time
import sys

class sudoUser():
    def addUser(self, Username, Password, ldg, version, notify):
        def store():
            global done1
            password = hashlib.md5()
            password.update(Password)
            password = password.hexdigest()
            #md5 hashing to store passwords
        
            userData = {
                0: {
                    "username": Username,
                    "password": password,
                }
            }
            pickle.dump( userData, open( "Userdata/users.p", "wb" ) )
            ldg.fullScreenStop()
            time.sleep(0.1)
            version_file = open('Version.txt')
            version_file = version_file.read()
            print(version_file == version)
            if version_file == version:
                ldg.fullScreen("All Set")
            elif version_file != version:
                ldg.fullScreen("Copying Data")
        try:
            urllib.urlretrieve ("https://raw.github.com/welware/ElectrOS/master/OS/Version.txt", "Version.txt")
            store()
        except:
            #cannot upgrade
            ldg.fullScreenStop()
            time.sleep(0.1)
            done1 = True
            print(done1, "n")
            
        
        

        
        #store username and password

        

        
        
