import serial
import sys
import glob

port = input("list port from discoverPorts.py: ")
print(port)


ser = serial.Serial(port)
ser.flushInput()
ser.write(b'a')

num = 0
file = open("data" + str(num) + ".csv", "wb")

while True:
    line = ser.readline()
    #print(line)
    if line == b'File:\r\n':
        num += 1
        print("new file!")
        file = open(("data" + str(num) + ".csv"), "wb")
    elif line == b'Done reading\r\n':
        print("exiting")
        break
    else:
        file.write(line)

file.close()
