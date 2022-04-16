from gpiozero import PWMLED, MCP3008
from time import sleep

pot = MCP3008(0)

led = PWMLED(17)
led2 = PWMLED(21)
led3 = PWMLED(16)

while True:
    print(pot.value)
    
    if pot.value < 0.001:
        led.value = 0
        led2.value = 0
        led3.value = 0
    elif pot.value < 0.3333:
        led.value = pot.value * 3
        led2.value = 0
        led3.value = 0
    elif pot.value >= 0.333 and pot.value < 0.666:
        led.value = 0.9999
        led2.value = (pot.value - 0.3333) * 3
        led3.value = 0      
    elif pot.value > 0.666:
        led.value = 0.99999
        led2.value = 0.99999
        led3.value = (pot.value - 0.67) * 3

    
    sleep(0.1)
