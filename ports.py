import winreg
import re

def get_usb_devices():
    '''
    Récupérer la liste des périphériques de stockage USB, connectés ou pas
    '''
    liste = []
    ddevs = [dev for dev in get_mounted_devices() if 'DosDevices' in dev[0]]
    for d in ddevs:
        if (re.search(r"USBSTOR", regbin2str(d[1]))) != None:
            liste.append(d[0][-2:] + "\\")
    return liste

def get_mounted_devices():
    '''
    Récupérer la liste des périphériques, connectés ou pas
    '''
    devs = []
    mounts = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\MountedDevices')
    for i in range(winreg.QueryInfoKey(mounts)[1]):
        devs += [winreg.EnumValue(mounts, i)]
    return devs

def regbin2str(bin):
    '''
    Décode le registre binaire en string
    '''
    str = ''
    for i in range(0, len(bin), 2):
        if bin[i] < 128:
            str += chr(bin[i])
    return str
