from gpiozero import PWMLED
from gpiozero import LED, Button
from tkinter import *
from tkinter import Tk, Label, Entry, Button, StringVar, IntVar




def switch_led():
    if position_track.get() == 0:
        print('off => on')
        position_track.set(1)
        led2.on()
    else:
        print('on => off')
        position_track.set(0)
        led2.off()
    
def change_color(self):
    red.value = red_slider.get()
    green.value = green_slider.get()
    blue.value = blue_slider.get()
    print(self)

def close_window():
    window.destroy()

led2 = LED(16)
red = PWMLED(23)
green = PWMLED(24)
blue = PWMLED(25)

window = Tk()
window.title('rgb led')
window.geometry('300x400')


position_track = IntVar(window)
position_track.set(0)

red_slider = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label='Red', troughcolor='red', length=200, command=change_color)
red_slider.pack()

green_slider = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label='Green', troughcolor='green', length=200, command=change_color)
green_slider.pack()

blue_slider = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label='Blue', troughcolor='blue', length=200, command=change_color)
blue_slider.pack()

close_button = Button(window, text='close', command=close_window)
close_button.pack()

switch_button = Button(window, text='led', command=switch_led)
switch_button.pack()
