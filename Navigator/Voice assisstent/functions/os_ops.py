import os
import subprocess as sp

paths = {
    'notepad': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories",
    'word': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_word():
    os.startfile(paths['word'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])