import board
import neopixel
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


def turn_all_off(pixels):
    for i in range(len(pixels)):
        pixels[i] = OFF

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)


while True:
    american(pixels)
    time.sleep(1)
    turn_all_off(pixels)
    time.sleep(2)
