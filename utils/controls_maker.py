"""
This is that CLI that allows for the creation of a smash bros ultimate profile.
"""

from enums import *
from generators import generate_keyboard_path

if __name__ == "__main__":
    tag = input("Username ?\n> ")
    path = generate_keyboard_path(tag)
    print(path)