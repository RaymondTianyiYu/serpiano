import serial
import time

print ('hello')

ser=serial.Serial(port='COM4')

time.sleep(2)

n=ser.write('1'.encode())
n=ser.write('2'.encode())
n=ser.write('3'.encode())
n=ser.write('4'.encode())


print ('after write')
print ('n')

def run():
    action = "aaa"
    while action != "q":
        print 'select which tone do you want to play ? 1,2,3,4,q and others for quit'
        action = input("> ")
        if action == "1":
            ser.write('1'.encode())
        elif action == "2":
            ser.write('2'.encode())
        elif action == "3":
            ser.write('3'.encode())
        elif action == "4":
            ser.write('4'.encode)
        else :
            return

run()
