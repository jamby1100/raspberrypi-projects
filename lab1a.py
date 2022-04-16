from gpiozero import LED
from time import sleep

led = LED(16)
led2 = LED(25)

delay = 1

while True:
    led.on()
    led2.off()
    print('led on')
    sleep(delay)
    led.off()
    led2.on()
    print('led off')
    sleep(delay)
