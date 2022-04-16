from gpiozero import LED, Button
from signal import pause

led = LED(25)
led2 = LED(16)
button = Button(2)

def pressed():
    led.on()
    led2.off()

def released():
    led.off()
    led2.on()

button.when_pressed = pressed
button.when_released = released

pause()
