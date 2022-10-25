print('code.py running...')
import board

# from kmk.hid import HIDModes

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.modules import Module
from kmk.scanners import DiodeOrientation

from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers

class DebugKeys(Module):
    def __init__(self):
        super().__init__()
    def process_key(self, keyboard, key, is_pressed, int_coord):
        # return super().process_key(keyboard, key, is_pressed, int_coord)
        print(int_coord)
        return key

keyboard = KMKKeyboard()
#        GND                BATTERY+
#          .----------------. 
# D1 P0.06 |                | BATTERY+
# DO P0.08 |                | GND
#      GND |                | RESET
#      GND |                | 3.3V
# D2 PO.17 |                | P0.37 D21
# D3 P0.20 |                | P0.29 D20
# D4 P0.22 |                | P0.02 D19
# D5 P0.24 |                | P1.15 D18
# D6 P1.00 |                | P1.13 D15
# D7 P0.11 |                | P1.11 D14
# D8 P1.04 |                | P0.10 D16
# D9 P1.06 |________________| P0.09 D10

keyboard.col_pins = [
    board.P1_11, # D14
    board.P1_13, # D15
    board.P1_15, # D18
    board.P0_02, # D19
    board.P0_29, # D20
    board.P0_20, # D3
    board.P0_22, # D4
    board.P0_24, # D5
    board.P1_00, # D6
    board.P0_11, # D7
]
# keyboard.col_pins = [   # ORIGINAL
#     board.P0_11,        # board.P1_11, # D14
#     board.P1_00,        # board.P1_13, # D15
#     board.P0_24,        # board.P1_15, # D18
#     board.P0_22,        # board.P0_02, # D19
#     board.P0_20,        # board.P0_29, # D20
#     board.P0_29,        # board.P0_20, # D3
#     board.P0_02,        # board.P0_22, # D4
#     board.P1_15,        # board.P0_24, # D5
#     board.P1_13,        # board.P1_00, # D6
#     board.P1_11,        # board.P0_11, # D7
# ]

keyboard.row_pins = [
    board.P0_10, # D16
    board.P0_09, # D10
    board.P1_04, # D8
    board.P1_06, # D9
]
# keyboard.row_pins = [   # ORIGINAL
#     board.P1_04,        # board.P0_10, # D16
#     board.P1_06,        # board.P0_09, # D10
#     board.P0_10,        # board.P1_04, # D8
#     board.P0_09,        # board.P1_06, # D9
# ]

keyboard.diode_orientation = DiodeOrientation.ROW2COL

# keyboard.modules.append(DebugKeys())

modtap = ModTap()
modtap.tap_time = 200
keyboard.modules.append(modtap)

layers = Layers()
keyboard.modules.append(layers)

keyboard.coord_mapping = [
             1,  2,  3,  4,         5,  6,  7,  8,
    0,   10, 11, 12, 13, 14,       15, 16, 17, 18, 19, 9,
         20, 21, 22, 23, 24,       25, 26, 27, 28, 29,
                     33, 34,       35, 36
]

ALPHA = 0
SYM = 1
NUM = 2
NAV = 3
RFN = 4
LFN = 5

keyboard.keymap = [
    [ # ALPHA
                                     KC.W,                   KC.E,                  KC.R,                  KC.T,                               KC.Y,                     KC.U,                   KC.I,                     KC.O,
       KC.Q,  KC.A,                  KC.S,                   KC.D,                  KC.F,                  KC.G,                               KC.H,                     KC.J,                   KC.K,                     KC.L,                     KC.SCOLON,                 KC.P,
              KC.MT(KC.Z, KC.LCTRL), KC.MT(KC.X, KC.LSHIFT), KC.MT(KC.C, KC.LALT),  KC.MT(KC.V, KC.LCMD),  KC.B,                               KC.N,                     KC.MT(KC.M, KC.LCMD),   KC.MT(KC.COMMA, KC.LALT), KC.MT(KC.DOT, KC.LSHIFT), KC.MT(KC.SLASH, KC.LCTRL),
                                                                                    KC.LT(SYM, KC.SPACE),  KC.LT(NUM, KC.SPACE),               KC.LT(SYM, KC.SPACE),     KC.LT(NUM, KC.SPACE),
    ],

    [ # SYM
                          KC.AT,    KC.HASH,   KC.DOLLAR,            KC.PERC,                          KC.CIRCUMFLEX,        KC.AMPR,                KC.ASTR, KC.UNDS, 
        KC.ESC, KC.TAB,   KC.MINUS, KC.EQUAL,  KC.EXLM,              KC.COLON,                         KC.BSLASH,            KC.GRAVE,               KC.LPRN, KC.RPRN, KC.ENTER, KC.BSPC,
                KC.COMMA, KC.DOT,   KC.BSLASH, KC.QUOTE,             KC.GRAVE,                         KC.PIPE,              KC.LBRC,                KC.RBRC, KC.LCBR, KC.RCBR,
                                               KC.LT(NAV, KC.SPACE), KC.LT(NAV, KC.SPACE),             KC.LT(SYM, KC.SPACE), KC.LT(NAV, KC.SPACE),
   ],

    # NUM
    [
                          KC.LPRN,  KC.LCBR, KC.LBRC,              KC.NO,                            KC.EQL,               KC.N7,                KC.N8,       KC.N9,
        KC.ESC, KC.TAB,   KC.UNDS,  KC.PLUS, KC.RPRN,              KC.COLON,                         KC.MINUS,             KC.N4,                KC.N5,       KC.N6,    KC.ENT, KC.BSPC,
                KC.LABK,  KC.RABK,  KC.BSLS, KC.DQUO,              KC.TILDE,                         KC.N0,                KC.N1,                KC.N2,       KC.N3,    KC.QUES,
                                             KC.LT(NAV, KC.SPACE), KC.LT(NAV, KC.SPACE),             KC.LT(NAV, KC.SPACE), KC.LT(NAV, KC.SPACE),
    ],

    # NAV
    [
                                   KC.NO  ,  KC.NO  , KC.NO  ,    KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,    
        KC.ESC, KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  ,    KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER,   KC.BSPC,
                KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  ,    KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                                      KC.SPACE  , KC.SPACE,                   KC.SPACE,   KC.SPACE,
    ],

    # RFN
    [
                                   KC.NO  ,  KC.NO  , KC.NO  ,  KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,
        KC.ESC, KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  ,  KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER, KC.BSPC,
                KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  ,  KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                                      KC.SPACE, KC.SPACE,                   KC.SPACE,   KC.SPACE,
    ],
    # [
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.F11,   KC.F7, KC.F8, KC.F9, KC.NO,
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.F10,   KC.F4, KC.F5, KC.F6, KC.NO,
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.NO,    KC.F1, KC.F2, KC.F3, KC.NO,
    #                     KC.NO, KC.NO, KC.SPC,                            KC.BSPC,  KC.NO, KC.NO,
    # ],

    # LFN
    [
                                   KC.NO  ,  KC.NO  , KC.NO  ,  KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,
        KC.ESC, KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  ,  KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER,   KC.BSPC,
                KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  ,  KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                                      KC.SPACE, KC.SPACE,                   KC.SPACE,   KC.SPACE,
    ],
    # [
    #     KC.NO,  KC.F7,  KC.F8, KC.F9, KC.F11,                                      KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
    #     KC.NO,  KC.F4,  KC.F5, KC.F6, KC.F10,                                      KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
    #     KC.NO,  KC.F1,  KC.F2, KC.F3, KC.NO,                                       KC.NO,   KC.NO  , KC.NO  , KC.NO  , KC.NO,
    #                     KC.NO, KC.NO, KC.SPC,                                      KC.BSPC, KC.NO, KC.NO,
    # ],
]

# keyboard.debug_enabled = True

if __name__ == '__main__':
    print('keyboard.go()-ing')
    # keyboard.go(hid_type=HIDModes.BLE, secondary_hid_type=HIDModes.USB)
    keyboard.go()
