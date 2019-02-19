# python.exe
# python -c pip install pyserial
# IDLE
--------------------------------

import serial

s = serial.Serial("COM*")

print( s.readline() )

input = s.readline()

--------------------------------

# process the input
# chunks = input.split(";")
# for x in chunk: x.split(",")
# each x represents
