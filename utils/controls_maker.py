"""
This is that CLI that allows for the creation of a smash bros ultimate profile.
A "sequence" is a pre-defined set of moves that can be used, if combined to create a profile.

A sequence can be, for instance, what buttons need to be pressed to enter the controls menu.
"""

from enums import *
from generators import generate_keyboard_path

if __name__ == "__main__":
    tag = input("Username ?\n> ")
    path = generate_keyboard_path(tag)
    print(path)