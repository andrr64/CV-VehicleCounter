from os import system as command
from tkinter import filedialog

def printLine():
    print(f"+{'-'*50}+")
def printCenter(text: str):
    print("|"+ text.center(50) + "|")

def printLeft(text: str):
    print("| " + text.ljust(49) + "|")

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
        command('cls')
        print('Pilih file...')
        videoFile = filedialog.askopenfilename()
        printLine()
        if (not len(videoFile)):
            print('Pilih filenya dong :(')
            input('Tekan enter untuk kembali...')
            continue
        
command('cls')
