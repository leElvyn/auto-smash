"""
This file contains consts like the layout of the switch keyboard, or the stage list.
"""
from enums import Controls

KEYBOARD_LOWERCASE_0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ''] #first row is the digits row
KEYBOARD_LOWERCASE_1 = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '']
KEYBOARD_LOWERCASE_2 = ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', '']
KEYBOARD_LOWERCASE_3 = ['w', 'x', 'c', 'v', 'b', 'n', '', '', '', '', '']

# This is the order in which controls are displayed when selecting a button

CONTROLS_ORDER_BUTTONS = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB
]
CONTROLS_ORDER_STICK = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB,
    Controls.SMASH_ATTACKS
]
CONTROLS_ORDER_DPAD = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB,
    Controls.TAUNT
]
