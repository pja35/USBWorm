import os

def copy_from_key():
    '''
    Copie de la clé USB au PC
    '''
    if os.name == 'nt':
        os.system("fsutil hardlink create setupypypyp.py setup.py")

copy_from_key()