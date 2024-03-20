import RPi.GPIO as GPIO

GPIO.setwarnings(False)

dac_numbers = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_numbers, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    while True:
        number = input('Type the number in range [0, 255]: ')
        try:
            number = int(number)
            print(number)
            if 0 <= number <= 255:
                GPIO.output(dac_numbers, dec2bin(number))
                voltage = float(number) / 256.0 * 3.3
                print(f"Output voltage: {voltage} ")
            else:
                print('Number is out of range')
        except Exception:
            if number == 'q': break
            print('Incorrect number!!!')

finally:
    GPIO.output(dac_numbers, 0)
    GPIO.cleanup()