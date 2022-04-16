from gpiozero import LED
from time import sleep

led = LED(23)
led2 = LED(24)

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
from gpiozero import LED
from time import sleep


led = LED(23)
led.on()
