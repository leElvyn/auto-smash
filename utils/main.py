"""
This is that CLI that allows for the creation of a smash bros ultimate profile.
"""

from enums import *
from generators import generate_keyboard_path, generate_controls_sequence_gc
from bin_converter import prepare_for_flashing
from generators import generate_ruleset_sequence, generate_ruleset_sequence
from writer import write_data


if __name__ == "__main__":
    """tag = input("Username ?\n> ")
    path = generate_keyboard_path(tag)
    byte_path = prepare_for_flashing(path)
    print(path)
    print(byte_path)"""
    #print(generate_controls_sequence_gc())
    sequence = generate_ruleset_sequence()
    
    byte_path = prepare_for_flashing(sequence)
    write_data(byte_path)