from model.data import Data, sort_by_date, sort_by_in, sort_by_out
from ui_util import *
from os import system as command
import json
__COLUMNLENGTH = 10
__PANJANG_STRING_LOKASI = 55
__PANJANG_KESELURUHAN = 100

def columnString(sumX, str_length = __COLUMNLENGTH):
    return str(sumX).ljust(str_length)

def __printDataAsRow(i: int, data: Data):
    printLeft(f'{str(i+1).ljust(4)}| {columnString(data.sum_in)}| {columnString(data.sum_out)}| {columnString(data.lokasi, __PANJANG_STRING_LOKASI)}| {columnString(data.tanggal)}', length=__PANJANG_KESELURUHAN)

def __getData() -> list[Data]:
    data = []
    with open('data.json', 'r') as file:
        data = json.load(file)
    formatted_data = [Data(x['tanggal'], x['lokasi'], x['data']) for x in data]
    return formatted_data

def UI_sortBy():
    command('cls')
    printLine()
    printLeft('1. Tanggal')
    printLeft('2. Jumlah Kendaraan Masuk (in)')
    printLeft('3. Jumlah Kendaraan Keluar (out)')
    printLine()
    _input = str(input('Command: '))
    if (_input == '1'):
        return sort_by_date(__getData())
    elif(_input == '2'):
        return sort_by_in(__getData())
    elif(_input == '3'):
        return sort_by_out(__getData())
    return None

def UI_detailData(data: Data):
    data_kendaraan = data.data
    while True:
        command('cls')
        printLine()
        printCenter('Detail Data')
        printLine()
        printLeft(f'Tanggal      : {data.tanggal}')
        printLeft(f'Lokasi       : {data.lokasi}')
        printLeft(f'Panjang Data : {data.data_length}')
        printLeft(f'Total Kend.  : {data.sum_all}')
        printLine()
        for (i, key) in enumerate(data.data.keys()):
            printLeft(f'{i+1}. {key}: in={data.data[key]['IN']} out={data.data[key]['OUT']}')
        printLine()
        printCenter('e: Kembali')
        printLine()
        _input = str(input('Command : ')).lower()
        if (_input == 'e'):
            break

def UI_viewData() :
    try:
        counts = sort_by_date(__getData())
        data_length = len(counts)
        if (len(counts) == 0):
            command('cls')
            printLine()
            printCenter('Data Kosong :(')
            printLine()
            input('')
            return None
        while True:
            command('cls')
            printLine(__PANJANG_KESELURUHAN)
            printCenter('Data', length=__PANJANG_KESELURUHAN)
            printLine(__PANJANG_KESELURUHAN)
            printLeft(f'{"No".ljust(4)}| {columnString('Masuk')}| {columnString('Keluar')}| {columnString('Lokasi', __PANJANG_STRING_LOKASI)}| {columnString('Tanggal')}', length=__PANJANG_KESELURUHAN)
            for (i, data) in enumerate(counts):
                __printDataAsRow(i, data)
            printLine(__PANJANG_KESELURUHAN)
            printCenter('ketik nomor data untuk detail', length=__PANJANG_KESELURUHAN)
            printCenter('', length=__PANJANG_KESELURUHAN)
            printCenter('e: Exit | r: refresh data', length=__PANJANG_KESELURUHAN)
            printCenter('s: urutkan berdasarkan | x: reverse urutan', length=__PANJANG_KESELURUHAN)
            printLine(__PANJANG_KESELURUHAN)
            _input = str(input('Command\t: ')).lower()
            if (_input == 'e'):
                return 0
            elif(_input == 'r'):
                counts = __getData()
            elif(_input == 's'):
                _output = UI_sortBy()
                if (_output is not None):
                    counts = _output
            elif(_input == 'x'):
                counts.reverse()
            else:
                try:
                    _index = int(_input)-1
                    if (0 <= _index < data_length):
                        UI_detailData(counts[_index])
                except Exception as e:
                    input(e)
    except Exception as e:
        input(e)