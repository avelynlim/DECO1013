from microbit import *
import neopixel
import music

def range_map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

np = neopixel.NeoPixel(pin1, 30)
a_note = ['c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5']
b_note = ['c4:1', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5', 'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5']
c_note = ['c4:1', 'e', 'g', 'c5']
d_note = ['c5:1', 'g4', 'e4', 'c4']

while True:
    val = pin2.read_analog()
    mapped = range_map(val, 0, 1023, 0, 400)
    print((val, mapped))
    if button_a.is_pressed():
        music.play(a_note)

    elif button_b.is_pressed():
        music.play(b_note)

    for x in range(0, len(np)):

        red = (255, 20, 20)
        orange = (255, 128, 0)
        yellow = (255, 255, 0)
        green = (50, 255, 50)
        blue = (51, 153, 255)
        navy = (0, 0, 128)
        violet = (204, 0, 204)
        white = (255, 255, 255)
        black = (0, 0, 0)


        if mapped >= 0 and mapped < 40:
            np[x] = (black)
            np.show()

        elif mapped >= 40 and mapped < 80:
            np[x] = (red)
            np.show()

        elif mapped >= 80 and mapped < 120:
            np[x] = (orange)
            np.show()

        elif mapped >= 120 and mapped < 160:
            np[x] = (yellow)
            np.show()

        elif mapped >= 160 and mapped < 200:
            np[x] = (green)
            np.show()

        elif mapped >= 200 and mapped < 240:
            np[x] = (blue)
            np.show()

        elif mapped >= 240 and mapped < 280:
            np[x] = (navy)
            np.show()

        elif mapped >= 280 and mapped < 320:
            np[x] = (violet)
            np.show()

        elif mapped >= 320 and mapped < 360:
            np[x] = (white)
            np.show()

        elif mapped >= 360 and mapped < 400:

            np[x] = (black)
            np.show()

    sleep(100)
