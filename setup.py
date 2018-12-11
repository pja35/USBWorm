"""Fichier d'installation."""

from cx_Freeze import setup, Executable
import os.path

'''
Création des .exe
'''

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


optimize = 1

options ={
    'build_exe':{
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            'scripts'
        ],
        'optimize': optimize,
    },
}

setup(
    name = "buzz",
    version = "1.0",
    description = "Ce programme vous cherche une cle USB",
    options = options,
    executables = [
        Executable("intrusion.py"), Executable("boot.py"),
        Executable("bypass.py"), Executable("copytoPC.py")
    ],
)