from gpiozero import LED, Button
from signal import pause

led = LED(25)
led2 = LED(16)
button = Button(2)

button.when_pressed = led.on
button.when_pressed = led2.on
button.when_released = led.off
button.when_released = led2.off

pause()
