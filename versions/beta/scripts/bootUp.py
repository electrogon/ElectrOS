import time
#Bootup completes all the necessary work during bootup

class BootUp():
    def __init__(self, queue):
        self.queue = queue
        print("test")
        self.run()
    def run(self):
        time.sleep(10)
        self.queue.put("cleanup")
