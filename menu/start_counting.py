from tkinter import filedialog
from os import system as command
from datetime import datetime
from copy import deepcopy
from menu.yolo_counting import yoloCounting
from ui_util import printLine

def getVideoFile():
    command('cls')
    print('Pilih file...')
    videoFile = filedialog.askopenfilename()
    if not videoFile:
        print('Pilih filenya dong :(')
        input('Tekan enter untuk kembali...')
        return None
    command('cls')
    print(f"File OK\n{videoFile}")
    return videoFile

def getDateAndLocation():
    printLine()
    print('Format tanggal: 12/12/2024')
    printLine()
    tanggal = str(input('Tanggal \t\t\t: '))
    lokasi = str(input('Lokasi \t\t\t\t: '))
    return tanggal, lokasi

def getCountingMode():
    printLine()
    mode = int(input('Mode (1=silent, 2=video)\t: '))
    return mode == 2

def countingProcess(videoFile, tanggal, lokasi, mode):
    try:
        _output = yoloCounting(videoFile, mode)
        return {
            'tanggal': tanggal.strftime('%d/%m/%Y'),
            'lokasi': lokasi,
            'data': _output
        }
    except ValueError:
        input("Format tanggal salah. Harus dd/mm/yy")
        return None

def UI_startCounting() -> any:
    videoFile = getVideoFile()
    if not videoFile:
        return None

    tanggal, lokasi = getDateAndLocation()
    mode = getCountingMode()

    command('cls')
    print('Perhitungan dimulai...')
    
    try:
        return deepcopy(countingProcess(videoFile, datetime.strptime(tanggal, "%d/%M/%Y"), lokasi, mode))
    except Exception as e:
        command('cls')
        input(e)
        return None
