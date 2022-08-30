import board
import time
from digitalio import DigitalInOut, Direction, Pull

from kb import KMKKeyboard

import adafruit_pioasm
import neopixel

from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()
modtap = ModTap()
mousekeys=MouseKeys()

split_side = SplitSide.LEFT

split = Split(split_flip=False,split_type=SplitType.UART, split_side=split_side, use_pio=True,
split_target_left=False, target_left=False, data_pin= board.GP1,
data_pin2=board.GP2)

layers_ext = Layers()
locks = LockStatus()


keyboard.modules.append(split)
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.modules.append(mousekeys)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(locks)


#print("Hello World!")

red = DigitalInOut(board.GP0)
red.direction=Direction.OUTPUT
red.value=1


keyboard.keymap = [
    [  #QWERTY
        KC.N1, KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,               KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.Q,  \
        KC.N2, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,               KC.H,    KC.J,    KC.K,    KC.L, KC.QUOT, KC.A,  \
        KC.N3, KC.NO,  KC.NO ,   KC.C,    KC.V,    KC.B,               KC.N,    KC.M,    KC.N2,   KC.N2,  KC.N1, KC.Z,  \
                                KC.NO,   KC.NO,  KC.NO,                KC.N3,   KC.N4,   KC.N5,
    ]
]   




if __name__ == '__main__':
    keyboard.go()