"""
This file will generate sequences for complex bits of the script. 
This includes the path to enter a tag on the keyboard, or the stages to enable/disable.
"""

from numpy.core.numeric import full
from enums import *
import consts
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Keyboard:
    def __init__(self) -> None:
        self.keyboard = [consts.KEYBOARD_LOWERCASE_0, consts.KEYBOARD_LOWERCASE_1, consts.KEYBOARD_LOWERCASE_2, consts.KEYBOARD_LOWERCASE_3]
        
    def get_empty_keyboard(self)->list:
        """Returns an array of 1's representing the keyboard."""
        print([[1]*len(self.keyboard[0])]*len(self.keyboard))
        return [[1]*len(self.keyboard[0])]*len(self.keyboard)

    def get_key_location(self, key)->list:
        """Returns the location of the key on the keyboard."""
        for row in self.keyboard:
            if key in row:
                return (self.keyboard.index(row), row.index(key))
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
        print(grid.grid_str(path=path, start=start, end=end))
        return path, key_position
        
def generate_keyboard_path(tag: str) -> list:
    """Generates a list of keyboard paths to enter a tag."""
    keyboard = Keyboard()
    full_path = [] # the full path is a list of lists of coordinates to press the keys
    path = [] # the path is the temporary list of coordinates to go from one key to another
    location = [0, 0] #This is the initial location of the cursor on the beyboard.
    for char in tag:
        path, location = keyboard.pathfind_key(char, location) # the position of the current key is the new starting point for the next key
        full_path.append(path)
    return full_path