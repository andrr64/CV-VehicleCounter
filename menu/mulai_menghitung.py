from tkinter import filedialog
from os import system as command
from datetime import datetime
from ui_util import *
from menu.yolo_counting import *

def counting(fileURL, date: datetime, location) -> map:
    try:
        _output = yoloCounting(fileURL, date)
    except ValueError:
        print("Format tanggal salah. Harus dd/mm/yy")
        input()
        return None
    result = {
        'fileURL': fileURL,
        'date': date,
        'location': location,
        'in': _output[0],
        'out': _output[1],
    }
    return result

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
    tanggal = str(input('Tanggal \t: '))
    lokasi = str(input('Lokasi \t\t: '))
    printLine()
    command('cls')
    print('Perhitungan dimulai...')
    try:
        return counting(videoFile, datetime.strptime(tanggal, "%d/%M/%Y"), lokasi)
    except Exception as e:
        command('cls')
        input(e)
        return None