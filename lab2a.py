from gpiozero import LED, Button
from signal import pause

led = LED(25)
led2 = LED(16)
button = Button(2)

while True:
    if button.is_pressed:
        led.on
        led2.off

    if button.is_pressed:
        led.off
        led2.on

    pause()
