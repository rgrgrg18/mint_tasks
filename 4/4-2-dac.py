import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)

dac_numbers = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_numbers, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

flag = 1
t = 0
x = 0

try:
    rest = float(input('Type a period time: '))
    while True:
        GPIO.output(dac_numbers, dec2bin(x))
        voltage = float(x) / 256.0 * 3.3
        print(voltage)

        if x == 0: flag = 1
        if x == 255: flag = 0

        if flag == 1:
            x += 1
        else:
            x -= 1
        sleep(rest / 512)
        t += 1

except ValueError:
    print('Incorrect value')

finally:
    GPIO.output(dac_numbers, 0)
    GPIO.cleanup()