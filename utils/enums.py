from enum import Enum

class Buttons(Enum):
    """
    Enum for the buttons in the game.
    """
    NOTHING = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    A = 5
    B = 6
    X = 7
    Y = 8
    D_UP = 9
    D_DOWN = 10
    D_LEFT = 11
    D_RIGHT = 12
    L = 13
    R = 14
    ZL = 15
    ZR = 16
    PLUS = 17
    MINUS = 18

    # currently, axes are just for enums   
    L_STICK = None
    R_STICK = None
    # NEXT TO BE IMPLEMENTED


class Controls(Enum):
    """
    list of controls a button can be assigned to
    """ 
    NORMAL_ATTACK = 0
    SPECIAL_ATTACK = 1
    JUMP = 2
    SHIELD = 3
    GRAB = 4
    UP_TAUNT = 5
    SIDE_TAUNT = 6
    DOWN_TAUNT = 7
    # Stick controls
    SMASH_ATTACKS = 8
    TILT_ATTACKS = 9
