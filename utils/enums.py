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
    LCLICK = 19
    RCLICK = 20

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
    # taunt only appears on the corresponding DPAD, so no need to put the 3 directions
    TAUNT = 5

    # Stick controls
    SMASH_ATTACKS = 6
    TILT_ATTACKS = 7

class StageSelectionType(Enum):
    anyone = 0
    take_turns = 1
    loser_pick = 2
    in_order = 3
    random = 4
    bf_o = 5
    bf_only = 6
    o_only = 7

class TimeValues(Enum):
    inf = 0
    t1_00 = 1
    t1_30 = 1.5
    t2_00 = 2
    t2_30 = 2.5
    t3_00 = 3
    t4_00 = 4
    t5_00 = 5
    t6_00 = 6
    t7_00 = 7
    t8_00 = 8
    t9_00 = 9
    t10_00 = 10
    t11_00 = 11
    t12_00 = 12
    t13_00 = 13
    t14_00 = 14
    t15_00 = 15
    t16_00 = 16
    t17_00 = 17
    t18_00 = 18
    t19_00 = 19
    t20_00 = 20