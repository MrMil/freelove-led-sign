import time
import board
import neopixel

LEDS_PER_STRIP = 109
SLEEP_TIME = 0.01
COLORS = [(255, 0, 0), (255, 0, 255), (128, 0, 128)]
BRIGHTNESS = 0.5


def run_color_on_stips(strips: list[neopixel.NeoPixel], color: tuple[int, int, int]):
    for strip in strips:
        for i in range(LEDS_PER_STRIP):
            strip[i] = color
            time.sleep(SLEEP_TIME)


def run_colors_on_strips(strips: list[neopixel.NeoPixel], colors: list[tuple[int, int, int]]):
    for color in colors:
        run_color_on_stips(strips, color)


def main():
    pixels1 = neopixel.NeoPixel(board.D18, LEDS_PER_STRIP, brightness=BRIGHTNESS)
    pixels2 = neopixel.NeoPixel(board.D21, LEDS_PER_STRIP, brightness=BRIGHTNESS)
    pixels1.fill((20, 20, 20))
    pixels2.fill((20, 20, 20))

    strips = [pixels1, pixels2]

    while True:
        run_colors_on_strips(strips, COLORS)


if __name__ == '__main__':
    main()
