from tkinter import filedialog
from os import system as command
from datetime import datetime
from ui_util import *
from menu.yolo_counting import *
from copy import deepcopy

def counting(fileURL, date: datetime, location, mode) -> map:
    try:
        _output = yoloCounting(fileURL, mode)
        return {
            'tanggal': date.strftime('%d/%m/%Y'),
            'lokasi': location,
            'data': _output
        }
    except ValueError:
        input("Format tanggal salah. Harus dd/mm/yy")
        return None

def UI_mulaiMenghitung() -> any:
    command('cls')
    print('Pilih file...')
    videoFile = filedialog.askopenfilename()
    if (not len(videoFile)):
        print('Pilih filenya dong :(')
        input('Tekan enter untuk kembali...')
        return None
    command('cls')
    print(f"File OK\n{videoFile}")
    printLine()
    print('Format tanggal: 12/12/2024')
    printLine()
    tanggal = str(input('Tanggal \t\t\t: '))
    lokasi = str(input('Lokasi \t\t\t\t: '))
    mode = int(input('Mode (1=silent, 2=video)\t: '))
    printLine()
    command('cls')
    print('Perhitungan dimulai...')
    try:
        return deepcopy(counting(videoFile, datetime.strptime(tanggal, "%d/%M/%Y"), lokasi, mode == 2))
    except Exception as e:
        command('cls')
        input(e)
        return None