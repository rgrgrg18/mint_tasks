import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac_numbers = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac_numbers, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc():
    
    for i in range(256):
        temp = dec2bin(i)
        GPIO.output(dac_numbers, temp)
        input_val = GPIO.input(comp)
        sleep(0.01)
        if input_val:
            return i
    return 0

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256
        if i: print(voltage)
finally:
    GPIO.output(dac_numbers, 0)
    GPIO.cleanup()
