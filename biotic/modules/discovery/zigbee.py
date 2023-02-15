import serial

ser = serial.Serial('/dev/tty16')
print(ser.name)
