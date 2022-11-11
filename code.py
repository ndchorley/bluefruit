from adafruit_circuitplayground import cp
import time


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

OFF = (0, 0, 0)


def american(pixels):
    for i in range(len(pixels)):
        if (i % 3 == 0):
            pixels[i] = RED
        elif (i % 3 == 1):
            pixels[i] = WHITE
        else:
            pixels[i] = BLUE

        time.sleep(0.5)


def all_green(pixels):
    for i in range(len(pixels)):
        pixels[i] = GREEN


while True:
    if cp.button_a:
        american(cp.pixels)
    elif cp.button_b:
        all_green(cp.pixels)
