"""
utils for generating sequences of buttons
"""
from enums import Buttons

def add_button(sequence: list, button: Buttons, duration: int):
    """
    add a button to a sequence
    """
    sequence.append(Action(button, duration))

def extend(sequence, button: Buttons, duration = 1, delay = 1):
    """
    extend the sequence with a delay of 1 (default) frame followed by the button for 1 frame (default)
    """
    add_button(sequence, Buttons.NOTHING, delay)
    add_button(sequence, button, duration)

class Action:
    """
    An action is a press of a button. It contains a button and a duration.
    """
    def __init__(self, button: Buttons, duration: int = 1):
        self.button = button
        self.duration = duration

    def __repr__(self):
        return str(f"({self.duration}, {self.button})")