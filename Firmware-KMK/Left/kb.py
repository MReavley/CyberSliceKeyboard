import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP19, board.GP20, board.GP21, board.GP22, board.GP23, board.GP24, board.GP25)
    row_pins = (board.GP16, board.GP17, board.GP18)
    diode_orientation = DiodeOrientation.COL2ROW
    #columns_to_anodes=True,
    #pull=True


    coord_mapping = [
     6,  5,  4,  3,  2,  1,    36, 37, 38, 39, 40, 41, 
    13, 12, 11, 10,  9,  8,    29, 30, 31, 32, 33, 34,
    20, 19, 18, 17, 16, 15,    22, 23, 24, 25, 26, 27,
                14,  7,  0,    21, 28, 35    ]
                
