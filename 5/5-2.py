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
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac_numbers, dec2bin(k))
        sleep(0.001)
        inp = GPIO.input(comp)
        if inp == 1:
            k -= 2**i
    return k


try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256
        if i: print(voltage)
finally:
    GPIO.output(dac_numbers, 0)
    GPIO.cleanup()
