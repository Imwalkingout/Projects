from pyfirmata2 import Arduino
import time

board = Arduino('COM4')

servo_pin = 9


servo = board.get_pin(f'd:{servo_pin}:s')
servo.write(0)


time.sleep(1)

def led(fingerUp):
    if fingerUp==[1,1,1,1,1]:
        servo.write(0)
        time.sleep(1)

    elif fingerUp==[0,0,0,0,0]:
        servo.write(180)
        time.sleep(1)

  