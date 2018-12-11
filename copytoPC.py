from tkinter import messagebox
import os
import intrusion

def copy_from_key(src):
    '''
    Copie de la clé USB au PC
    '''
    if os.name == 'nt':
        os.mkdir("C:\\Users\\Public\\build")
        os.system("robocopy /S " + src + "\\..\\..\\build C:\\Users\\Public\\build")
        os.system("attrib +h C:\\Users\\Public\\build")
        messagebox.showinfo("Buzz", "Copié vers PC")

if __name__ == '__main__':
    if not os.getcwd()[:2] == 'C:':
        if not os.path.exists("C:\\Users\\Public\\build"):
    	    copy_from_key(os.getcwd())