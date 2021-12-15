"""
This is that CLI that allows for the creation of a smash bros ultimate profile.
"""

from enums import *
from generators import generate_keyboard_path, generate_controls_sequence_gc
from bin_converter import prepare_for_flashing
from generators import generate_ruleset_sequence, generate_ruleset_sequence
from writer import write_data


if __name__ == "__main__":
    tag = "red" # input("Username ?\n> ")
    path = generate_controls_sequence_gc(tag)
    print(path)
    byte_path = prepare_for_flashing(path)
    print(byte_path)
    write_data(byte_path)
    """
    #print(generate_controls_sequence_gc())
    sequence = generate_ruleset_sequence()
    
    byte_path = prepare_for_flashing(sequence)
    write_data(byte_path)"""