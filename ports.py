import winreg
import re

# Get USB devices (connected or not)
def get_usb_devices():
    liste = []
    ddevs = [dev for dev in get_mounted_devices() if 'DosDevices' in dev[0]]
    for d in ddevs:
        if (re.search(r"USBSTOR", regbin2str(d[1]))) != None:
            liste.append(d[0][-2:] + "\\")
    return liste

# Get all mounted devices (connected or not)
def get_mounted_devices():
    devs = []
    mounts = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\MountedDevices')
    for i in range(winreg.QueryInfoKey(mounts)[1]):
        devs += [winreg.EnumValue(mounts, i)]
    return devs

# Decode registry binary to readable string
def regbin2str(bin):
    str = ''
    for i in range(0, len(bin), 2):
        if bin[i] < 128:
            str += chr(bin[i])
    return str