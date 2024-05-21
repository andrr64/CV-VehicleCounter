from os import system as command
from os import path
from tkinter import filedialog
from menu.start_counting import UI_startCounting
from ui_util import *
import json
from menu.view_data import UI_viewData

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

def writeData(new_data: dict):
    with open(DATA_FILENAME, 'r+') as file:
        data: list = json.load(file)
        data.append(new_data)
        file.seek(0)  # Kembali ke awal file
        json.dump(data, file, indent=4)
        file.truncate()  # Potong sisa file jika ada

DATA_FILENAME = 'data.json'

if not path.exists(DATA_FILENAME):
    with open(DATA_FILENAME, 'w') as file:
        json.dump([], file, indent=4)        

while True:
    try:
        UI_menuUtama()
        _input = str(input('Command: ')).lower()
        if (_input == 'e'):
            break
        elif(_input == '1'):
            _output = UI_startCounting()
            command('cls')
            if _output is not None:
                try:
                    writeData(_output)
                    input('Data berhasil ditulis\nTekan enter untuk kembali...')
                except Exception as e:
                    print(e)
                    input('Terjadi kesalahan saat menulis data...')
            else:
                continue
        elif(_input == '2'):
            _output = UI_viewData()

    except:
        continue
command('cls')