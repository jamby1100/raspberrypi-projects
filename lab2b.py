from gpiozero import Button, LED
from signal import pause

led = LED(16)
led2 = LED(25)

led2.on()
print("RELEASED! No car in driveway")
print('========')
    
def say_hello():
    led.on()
    led2.off()
    print("PRESSED! Car is using driveway")
    print('========')

def say_hi():
    led.off()
    led2.on()
    print("RELEASED! No car in driveway")
    print('========')

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_hi
pause()
