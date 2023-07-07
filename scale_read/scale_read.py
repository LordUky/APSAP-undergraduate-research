import serial
import re
import openpyxl as pyxl
import datetime

class scaleRead:
    _DEBUG = False

    def __init__(self, serial_port) -> None:
        self.ser = serial.Serial(serial_port, 9600)

    def read(self) -> float:
        if self._DEBUG:
            return 114.514
        else:
            response = str(self.ser.read(10))
            response = float(re.findall(r'\d+\.\d+', response)[0])
            print("scale read:", response)
            return response

    def write_to_file(self, weight: float, fp: str) -> None:
        wb = pyxl.Workbook()
        ws = wb.active

        ws['A1'] = "Index"
        ws['A2'] = 2
        ws['B1'] = "Time"
        ws['B2'] = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        ws['C1'] = "Weight"
        ws['C2'] = round(weight, 2)
        ws['D1'] = "Unit"
        ws['D2'] = "g"
        wb.save(fp)

    def __del__(self):
        self.ser.close()