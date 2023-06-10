import pyqtgraph as pg
import serial
import sys
import glob

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == '__main__':
    ports = serial_ports()
    print(ports)
    port = input("Choose Teensy port: ")
    print("Selected " + str(port))

    ser = serial.Serial(port)
    ser.flushInput()
    file = open("laps.csv", "wb")
    header = "state,total time (s),lap (#),lap time (s)\n"

    file.write(header.encode('utf-8'))
    while True:
        line = ser.readline()
        print(line)
        file.write(line)

file.close()

