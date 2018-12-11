"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup

setup(
    name = "buzz",
    version = "0.1",
    description = "Ce programme vous cherche une cle USB",
    options = {'': {'init_script' : 'install'}},
    executables = [Executable("thread.py"), Executable("boot.py"), Executable("bypass.py")],
)