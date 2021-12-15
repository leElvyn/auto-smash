"""
This file contains sequences, that are static.
A "sequence" is a pre-defined set of moves that can be used, if combined to create a profile.

A sequence can be, for instance, what buttons need to be pressed to enter the controls menu.
For sequences that are dynamic, check the file: utils/generators.py
"""

from buttons import extend
from enums import Buttons


def test_personal_sequence():
    s = []
    extend(s, Buttons.DOWN)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.A, delay=16)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.LEFT, delay=5)
    extend(s, Buttons.PLUS, delay=7)
    extend(s, Buttons.RIGHT)
    extend(s, Buttons.RIGHT)
    extend(s, Buttons.UP)
    extend(s, Buttons.UP)
    extend(s, Buttons.UP)
    extend(s, Buttons.A, delay=14)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.DOWN)
    extend(s, Buttons.A, delay=15)
    extend(s, Buttons.PLUS, delay=30)
    extend(s, Buttons.B, delay=90)
    return s