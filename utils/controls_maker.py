"""
This is that CLI that allows for the creation of a smash bros ultimate profile.
"""

from enums import *
from generators import generate_keyboard_path
from bin_converter import convert_to_bytearray

if __name__ == "__main__":
    tag = input("Username ?\n> ")
    path = generate_keyboard_path(tag)
    byte_path = convert_to_bytearray(path)
    print(path)
    print(byte_path)