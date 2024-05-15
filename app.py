from os import system as command
from tkinter import filedialog
from menu.mulai_menghitung import UI_mulaiMenghitung
from ui_util import *

def UI_menuUtama():
    command('cls')
    printLine()
    printCenter('Universitas BSI')
    printCenter('Ujian Akhir Semester - Pengolahan Citra')
    printCenter('Program Penghitung Kendaraan')
    printLine()
    printLeft("1. Mulai Menghitung")
    printLeft("2. Data Kendaraan")
    printLeft("3. Grafis ")
    printLeft("e. Keluar")
    printLine()

while True:
    UI_menuUtama()
    _input = str(input('Command: ')).lower()
    if (_input == 'e'):
        break
    elif(_input == '1'):
        _output = UI_mulaiMenghitung()
        command('cls')
        if  _output is not None:
            print(_output)
            input('Tekan enter untuk kembali...')
        else:
            print(_output)
            input()
command('cls')