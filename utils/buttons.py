"""
utils for generating sequences of buttons
"""
from enums import Buttons

def add_button(sequence, button: Buttons, duration):
    """
    add a button to a sequence
    """
    sequence.append((duration, button))

def extend(sequence, buttons: Buttons, duration = 1, delay = 1):
    """
    extend the sequence with a delay of 1 (default) frame followed by the button for 1 frame (default)
    """
    add_button(sequence, Buttons.NOTHING, delay)
    add_button(sequence, buttons, duration)