import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(23, IO.OUT)
IO.setup(24, IO.OUT)
IO.setup(25, IO.OUT)
IO.setup(21, IO.OUT)
IO.setup(20, IO.OUT)
IO.setup(16, IO.OUT)
IO.setup(12, IO.OUT)

IO.output(23,1)
IO.output(24,1)
delay = 1

while True:
    IO.output(23,1)
    IO.output(24,1)
    IO.output(25,1)
    IO.output(21,1)
    IO.output(16,1)
    IO.output(12,1)
    sleep(delay)
