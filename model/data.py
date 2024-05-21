from dataclasses import dataclass
from datetime import datetime

@dataclass
class Data:
    tanggal: str
    lokasi: str
    data: dict
    sum_in: int
    sum_out: int
    dt: datetime

    def __init__(self, tanggal: str, lokasi: str, data: dict) -> None:
        self.tanggal = tanggal
        self.lokasi = lokasi
        self.data = data
        self.sum_in = sum(x['in'] for x in self.data.values())
        self.sum_out = sum(x['out'] for x in self.data.values())
        self.dt = datetime.strptime(tanggal, '%d/%M/%Y')

def sort_by_date(data_list: list[Data]) -> list[Data]:
    """
    Mengurutkan data berdasarkan tanggal.
    
    Parameter:
    data_list (List[Data]): Daftar objek Data.

    Returns:
    List[Data]: Daftar objek Data yang diurutkan berdasarkan tanggal.
    """
    return sorted(data_list, key=lambda x: x.dt)

def sort_by_in(data_list: list[Data]) -> list[Data]:
    """
    Mengurutkan data berdasarkan total 'in'.
    
    Parameter:
    data_list (List[Data]): Daftar objek Data.

    Returns:
    List[Data]: Daftar objek Data yang diurutkan berdasarkan total 'in' secara menurun.
    """
    return sorted(data_list, key=lambda x: x.sum_in, reverse=True)

def sort_by_out(data_list: list[Data]) -> list[Data]:
    """
    Mengurutkan data berdasarkan total 'out'.
    
    Parameter:
    data_list (List[Data]): Daftar objek Data.

    Returns:
    List[Data]: Daftar objek Data yang diurutkan berdasarkan total 'out' secara menurun.
    """
    return sorted(data_list, key=lambda x: x.sum_out, reverse=True)