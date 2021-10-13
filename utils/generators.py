"""
This file will generate sequences for complex bits of the script. 
This includes the path to enter a tag on the keyboard, or the stages to enable/disable.
"""

from numpy.core.numeric import full
from enums import *
import consts
from buttons import *

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def flatten_list(list_of_lists):
    """Flattens a list of lists into a single list."""
    flattened_list = []
    for item in list_of_lists:
        if isinstance(item, list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    return flattened_list


def generate_sequence_from_list(list_of_positions):
    sequence = []
    # reset the location to the initial position
    location = [0, 0] 
    # This is because at every iteration of that nex loop, we compare the previous location with the current one to figure out what changed
    full_path = flatten_list(list_of_positions)
    for move in full_path:
        if isinstance(move, Action):
            sequence.append(move) # we just append the Action to the full sequence
            continue
        
        # here, we are comparing the previous location with the current one
        # if you can improve this, please do so
        if location[0] < move[0]:
            extend(sequence, Buttons.RIGHT)
        elif location[0] > move[0]:
            extend(sequence, Buttons.LEFT)
        elif location[1] < move[1]:
            extend(sequence, Buttons.DOWN)
        elif location[1] > move[1]:
            extend(sequence, Buttons.UP)
        location = move
    
    return sequence

    ### methods for generating keyboard paths ###

class Keyboard:
    def __init__(self) -> None:
        self.keyboard = [consts.KEYBOARD_LOWERCASE_0, consts.KEYBOARD_LOWERCASE_1, consts.KEYBOARD_LOWERCASE_2, consts.KEYBOARD_LOWERCASE_3]
        
    def get_empty_keyboard(self)->list:
        """Returns an array of 1's representing the keyboard."""
        return [[1]*len(self.keyboard[0])]*len(self.keyboard)

    def get_key_location(self, key)->list:
        """Returns the location of the key on the keyboard."""
        for row in self.keyboard:
            if key in row:
                return (row.index(key), self.keyboard.index(row))
        raise Exception("Key not found on keyboard.")

    def get_grid(self) -> Grid:
        """Returns a grid of the keyboard."""
        return Grid(matrix=self.get_empty_keyboard())


    def pathfind_key(self, key, location)->list:
        """
        Returns a list of coordinates to press the key.
        The location is the current location of the cursor on the keyboard.
        """
        key_position = self.get_key_location(key)
        grid = self.get_grid()
        start = grid.node(location[0], location[1])
        end = grid.node(key_position[0], key_position[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        print('operations:', runs, 'path length:', len(path))
        return path, key_position

        
def generate_keyboard_path(tag: str) -> list:
    """Generates a list of keyboard paths to enter a tag."""
    keyboard = Keyboard()
    full_path = [] # the full path is a list of lists of coordinates to press the keys
    path = [] # the path is the temporary list of coordinates to go from one key to another
    location = [0, 0] #This is the initial location of the cursor on the beyboard.
    for char in tag:
        if char == " ":
            extend(full_path, Buttons.Y)
            continue
        path, location = keyboard.pathfind_key(char, location) # the position of the current key is the new starting point for the next key
        full_path.append(path) # add the path from the previous key to the current key to the full path
        extend(full_path, Buttons.A) # press A after each key
    
    full_sequence = generate_sequence_from_list(full_path)
    extend(full_sequence, Buttons.PLUS)
    extend(full_sequence, Buttons.PLUS, delay=3)
    return full_sequence

    ### methods for generating controls paths ###


class Controls:
    """
    an instance of this object represent a control scheme. The default values are for the default control scheme.
    """
    A = Controls.NORMAL_ATTACK
    B = Controls.SPECIAL_ATTACK
    X = Controls.JUMP
    Y = Controls.JUMP

    L = Controls.GRAB
    R = Controls.GRAB
    ZL = Controls.SHIELD
    ZR = Controls.SHIELD

    R_STICK = Controls.SMASH_ATTACKS

    D_UP = Controls.UP_TAUNT
    D_DOWN = Controls.DOWN_TAUNT
    D_LEFT = Controls.SIDE_TAUNT
    D_RIGHT = Controls.SIDE_TAUNT