from tkinter import filedialog
from os import system as command
from datetime import datetime
from copy import deepcopy
from function.yolo import yoloCounting
from ui_util import printLine
import cv2

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
    tanggal = str(input('Tanggal (Default: Hari Ini)\t: '))
    lokasi = str(input('Lokasi \t\t\t\t: '))
    return tanggal, lokasi

def getCountingMode():
    printLine()
    mode = int(input('Mode (1=silent, 2=video)\t: '))
    return mode == 2

def countingProcess(videoFile, tanggal, lokasi, mode, region):
    try:
        _output = yoloCounting(videoFile, mode, region)
        return {
            'tanggal': tanggal.strftime('%d/%m/%Y'),
            'lokasi': lokasi,
            'data': _output
        }
    except ValueError:
        input("Format tanggal salah. Harus dd/mm/yy")
        return None


def getRegionCoordinate(videoFile) -> list:
    cap = cv2.VideoCapture(videoFile)

    if not cap.isOpened():
        print("Error: Tidak dapat membuka video.")
        return None

    ret, frame = cap.read()
    if not ret:
        print("Error: Tidak dapat membaca frame dari video.")
        cap.release()
        return None

    height, width, _ = frame.shape
    default_y = (height // 2) + 100
    x1, y1 = 0, (height // 2)
    x2, y2 = width, (height // 2)
    x3, y3 = 0, default_y
    x4, y4 = width, default_y

    while True:
        # Menampilkan koordinat default
        print(f'Koordinat Persegi Default: ({x1},{y1}), ({x2},{y2}), ({x3},{y3}), ({x4},{y4})')

        adjust_y = input('Masukkan penyesuaian y1, y2, y3, dan y4 (misal: -10, 20, -10, 20) atau tekan Enter untuk default: ')
        if adjust_y.strip():
            adjust_y = adjust_y.split(',')
            y1 += int(adjust_y[0])
            y2 += int(adjust_y[1])
            y3 += int(adjust_y[2])
            y4 += int(adjust_y[3])

        # Gambar persegi pada frame
        frame_with_region = frame.copy()
        cv2.rectangle(frame_with_region, (x1, y1), (x4, y4), (0, 255, 0), 2)

        # Tampilkan frame dengan persegi
        cv2.imshow('Frame with Region', frame_with_region)

        # Tunggu pengguna untuk menekan tombol, lalu lanjutkan atau keluar
        key = cv2.waitKey(0)
        if key == 27:  # ESC untuk keluar
            cap.release()
            cv2.destroyAllWindows()
            if str.lower(input('Sudah tepat? (y/n): ')) == 'y':
                break

    return [(x1, y1), (x2, y2), (x4, y4), (x3, y3)]
def UI_startCounting() -> any:
    videoFile = getVideoFile()
    if not videoFile:
        return None

    tanggal, lokasi = getDateAndLocation()
    mode = getCountingMode()
    region = getRegionCoordinate(videoFile);

    command('cls')
    print('Perhitungan dimulai...')
    
    try:
        if len(tanggal) == 0:
            tanggal = datetime.now().strftime("%d/%M/%Y");
        return deepcopy(countingProcess(videoFile, datetime.strptime(tanggal, "%d/%M/%Y"), lokasi, mode, region))
    except Exception as e:
        command('cls')
        input(e)
        return None
