import serial
import re

class scaleRead:
    SERIAL_PORT = "COM1"
    def __init__(self) -> None:
        pass

    def initialize(self):
        self.ser = serial.Serial(self.SERIAL_PORT, 9600)

    def destroy(self):
        self.ser.close()

    def read(self) -> float:
        self.ser.write(b'CAL\r\n')
        response = str(self.ser.read(10))
        response = float(re.findall(r'\d+\.\d+', response)[0])
        print("scale read:", response)
        return response

    
