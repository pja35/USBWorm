import intrusion, threading

class MonThread(threading.Thread):
    def __init__(self, liste, event):
        threading.Thread.__init__ (self)
        self.liste = liste
        self.event = event

    def run(self):
        while(1):
            intrusion.USBDetect()
        #print("\nUSB's Detected: %s\n" % self.liste)
        self.event.set()


event = threading.Event()
event.clear()
m = MonThread (intrusion.USBList, event)
m.start()
event.wait()