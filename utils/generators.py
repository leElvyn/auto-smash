"""
This file will generate sequences for complex bits of the script. 
This includes the path to enter a tag on the keyboard, or the stages to enable/disable.
"""

from numpy.core.numeric import full
from enums import *
from consts import *
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
        self.keyboard = [KEYBOARD_LOWERCASE_0, KEYBOARD_LOWERCASE_1, KEYBOARD_LOWERCASE_2, KEYBOARD_LOWERCASE_3]
        
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


class ControlScheme:
    """
    an instance of this object represent a control scheme. The default values are for the default control scheme.
    """
    A = Controls.NORMAL_ATTACK
    B = Controls.SPECIAL_ATTACK
    X = Controls.JUMP
    Y = Controls.JUMP

    L = Controls.GRAB
    R = Controls.GRAB
    Z = Controls.SHIELD

    R_STICK = Controls.SMASH_ATTACKS

    D_UP = Controls.UP_TAUNT
    D_MIDDLE = Controls.DOWN_TAUNT
    D_RIGHT = Controls.SIDE_TAUNT

    extra_rumbles = 1 # 0 for left, 1 for right
    extra_quick_smash = 1 # same
    extra_tap_jump = 1 #same 
    extra_sensibility = 1 # 0-2 for sensibility, left to right


    def get_changed_controls(self) -> list:
        """
        Returns a list of controls that are different from the default controls.
        """
        list_of_attributes = [a for a in dir(self) if not a.startswith('__')]
        changed_controls = []
        for control in list_of_attributes:
            if callable(getattr(self, control)):
                continue
            if getattr(self, control) != getattr(self.__class__, control):
                changed_controls.append(control)
        return changed_controls

    def select_control(self, default: Controls, new_control: Controls, is_stick = False) -> list:
        """
        Returns a sequence to go from the default control to the new control (for instance, i want Y mapped to grab, so go from JUMP, the third item in the list, to GRAB, the fifth item in the sequence).
        """
        sequence = []
        if not is_stick:
            default_position = CONTROLS_ORDER_BUTTONS.index(default) + 1
            new_position = CONTROLS_ORDER_BUTTONS.index(new_control) + 1
        else:
            default_position = CONTROLS_ORDER_STICK.index(default) + 1
            new_position = CONTROLS_ORDER_STICK.index(new_control) + 1
        difference = new_position - default_position
        if difference == 0:
            raise Exception("The new control is the same as the default control.")
        if difference < 0:
            for i in range(abs(difference)):
                extend(sequence, Buttons.UP)
        else:
            for i in range(difference):
                extend(sequence, Buttons.DOWN)
            
        extend(sequence, Buttons.A)
        delay(sequence, 10)
        return sequence

    def crawl_row(self, sequence, changes, ROW, cursor_location, reverse = False) -> int:
        for control in changes:
            new_cursor_location = ROW.index(control)
            for i in range(new_cursor_location - cursor_location):
                extend(sequence, Buttons.UP if reverse else Buttons.DOWN)
                cursor_location += 1
            extend(sequence, Buttons.A)
            delay(sequence, 10)
            extend(sequence, self.select_control(getattr(self.__class__, control), getattr(self, control)))
        return cursor_location

    def crawl_right_row(self, sequence, right_row_changes, RIGHT_ROW, is_reverse = False):
        cursor_location = 0 # location of the cursor on the right row only.
        for control in right_row_changes:
            new_cursor_location = RIGHT_ROW.index(control)
            for i in range(new_cursor_location - cursor_location):
                extend(sequence, Buttons.DOWN)
            extend(sequence, Buttons.A)
            delay(sequence, 10)
            extend(sequence, self.select_control(getattr(self.__class__, control), getattr(self, control)))
        return cursor_location

    def crawl_extras(self, sequence, extra_controls_changes, EXTRA_CONTROLS):
        cursor_location = 0
        for control in extra_controls_changes:
            new_cursor_location = EXTRA_CONTROLS.index(control)
            for i in range(new_cursor_location - cursor_location):
                extend(sequence, Buttons.DOWN)

            if control != "extra_sensibility": #sensibility doesn't work the same way
                # we always need to press left to change the control
                extend(sequence, Buttons.LEFT)
            
            else:
                if getattr(self, control) == 0:
                    extend(sequence, Buttons.LEFT)

                elif getattr(self, control) == 2:
                    extend(sequence, Buttons.LEFT, Buttons.RIGHT)
        extend(sequence, Buttons.PLUS)

    def generate_controls_sequence_gc(self):
        """
        Returns a list of inputs to change the control scheme.
        This will probably be ugly. 
        Here, we need to generate a sequence that goes to the right controls to change.
        Currently, for gamecube controller, there are basically two rows : 
        - one with L, DPAD, and extra options.
        - one with Z, R, A, B, X, Y
        There is also the C stick between the 2 rows. 
        
        This section is pretty hard to understand, due to attributes of objects. 
        Sometimes, an attribute is known with 
        """
        changed_controls = self.get_changed_controls()
        sequence = []

        LEFT_ROW = ["L", "D_UP", "D_MIDDLE", "D_RIGHT"]
        RIGHT_ROW = ["R", "Z", "X", "Y", "A", "B"]
        EXTRA_CONTROLS = ["extra_rumbles", "extra_quick_smash", "extra_tap_jump", "extra_sensibility"]
        MIDDLE_ROW = "R_STICK"

        left_row_changes = [control for control in changed_controls if control in LEFT_ROW] # control is the name of the attributes
        right_row_changes = [control for control in changed_controls if control in RIGHT_ROW]
        extra_controls_changes = [control for control in changed_controls if control in EXTRA_CONTROLS]

        go_to_left_row = len(left_row_changes) > 0
        go_to_right_row = len(right_row_changes) > 0
        go_to_extras = len(extra_controls_changes) > 0
        go_to_c_stick = MIDDLE_ROW in changed_controls
        cursor_location = 0

        if go_to_left_row:
            cursor_location = self.crawl_row(sequence, left_row_changes, LEFT_ROW, cursor_location)
            if go_to_extras:
                if cursor_location != 4: #if we aren't already on the other settings menu 
                    for i in range(4 - cursor_location):
                        extend(sequence, Buttons.DOWN)
                extend(sequence, Buttons.A)
                delay(sequence, 20)
                self.crawl_extras(sequence, extra_controls_changes, EXTRA_CONTROLS)
            if go_to_c_stick or go_to_right_row:

                if cursor_location < 3: #if we aren't already on the the down taunt button, or the other settings, both lead to the c stick
                    for i in range(3 - cursor_location):
                        extend(sequence, Buttons.DOWN)
                extend(sequence, Buttons.RIGHT)
                if go_to_c_stick:
                    extend(sequence, Buttons.A)
                    delay(sequence, 10)
                    self.select_control(self.__class__.R_STICK, self.R_STICK, True)
                extend(sequence, Buttons.RIGHT)
                if go_to_right_row:
                    self.crawl_row(sequence, right_row_changes, RIGHT_ROW, cursor_location, True)
        extend(sequence, Buttons.PLUS)
        return sequence

def generate_controls_sequence_gc():
    """
    Returns a list of inputs to change the control scheme.
    This will probably be ugly.
    """
    controller = ControlScheme()
    controller.L = Controls.SPECIAL_ATTACK
    controller.D_UP = Controls.SHIELD
    controller.extra_tap_jump = 0
    controller.R_STICK = Controls.NORMAL_ATTACK
    return controller.generate_controls_sequence_gc()
