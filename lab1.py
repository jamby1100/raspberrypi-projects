from gpiozero import LED
from time import sleep

led = LED(16)

delay = 1

while True:
    led.on()
    print('led on')
    sleep(delay)
    led.off()
    print('led off')
    sleep(delay)
