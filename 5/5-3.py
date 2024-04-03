import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac_numbers = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2 , 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac_numbers, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

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

def volume(val):
    val = int(val / 256 * 10)
    list = [0] * 8
    for i in range(val - 1):
        list[i] = 1
    return list

try:
    while True:
        i = adc()
        if i:
            volume_num = volume(i)
            GPIO.output(led, volume_num)
            print(3.3 * i / 255)
finally:
    GPIO.output(dac_numbers, 0)
    GPIO.cleanup()
