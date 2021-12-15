"""
This file will generate sequences for complex bits of the script. 
This includes the path to enter a tag on the keyboard, or the stages to enable/disable.
"""

import numpy

from enums import *
from consts import *
from buttons import *
import sequences

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
    delay(full_sequence, 15)
    extend(full_sequence, Buttons.PLUS)
    extend(full_sequence, Buttons.PLUS, delay=3)
    return full_sequence

    ### methods for generating controls paths ###


class ControlScheme:
    """
    an instance of this object represent a control scheme. The default values are for the default control scheme.
    
    TO BE FINISHED
    """
    A = Controls.NORMAL_ATTACK
    B = Controls.SPECIAL_ATTACK
    X = Controls.JUMP
    Y = Controls.JUMP

    L = Controls.GRAB
    R = Controls.GRAB
    Z = Controls.SHIELD

    R_STICK = Controls.SMASH_ATTACKS

    D_UP = Controls.TAUNT
    D_MIDDLE = Controls.TAUNT
    D_RIGHT = Controls.TAUNT

    extra_rumbles = 1 # 0 for left, 1 for right
    extra_quick_smash = 1 # same
    extra_tap_jump = 1 #same 
    extra_sensibility = 1 # 0-2 for sensibility, left to right

    cursor_location = 0
    tag = ""


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

    def select_control(self, default: Controls, new_control: Controls, is_stick = False, is_dpad = False) -> list:
        """
        Returns a sequence to go from the default control to the new control (for instance, i want Y mapped to grab, so go from JUMP, the third item in the list, to GRAB, the fifth item in the sequence).
        *sight* DPAD have different controls
        """
        sequence = []
        if is_stick:
            default_position = CONTROLS_ORDER_STICK.index(default) + 1
            new_position = CONTROLS_ORDER_STICK.index(new_control) + 1
        elif is_dpad:
            default_position = CONTROLS_ORDER_DPAD.index(default) + 1
            new_position = CONTROLS_ORDER_DPAD.index(new_control) + 1
        else:
            default_position = CONTROLS_ORDER_BUTTONS.index(default) + 1
            new_position = CONTROLS_ORDER_BUTTONS.index(new_control) + 1
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

    def crawl_row(self, changes, ROW, reverse = False, is_left_row = False) -> int:
        for control in changes:
            new_cursor_location = ROW.index(control)
            for i in range(new_cursor_location - self.cursor_location):
                extend(self.sequence, Buttons.UP if reverse else Buttons.DOWN)
                self.cursor_location += 1
            extend(self.sequence, Buttons.A)
            delay(self.sequence, 10)
            extend(self.sequence, self.select_control(getattr(self.__class__, control), getattr(self, control), is_dpad=True if self.cursor_location > 0 and self.cursor_location < 4 and is_left_row else False))

    def crawl_right_row(self, sequence, right_row_changes, RIGHT_ROW, is_reverse = False):
        for control in right_row_changes:
            new_cursor_location = RIGHT_ROW.index(control)
            for i in range(new_cursor_location - self.cursor_location):
                extend(sequence, Buttons.DOWN)
            extend(sequence, Buttons.A)
            delay(sequence, 10)
            extend(sequence, self.select_control(getattr(self.__class__, control), getattr(self, control)))

    def crawl_extras(self, extra_controls_changes, EXTRA_CONTROLS):
        
        extras_cursor_location = 0
        for control in extra_controls_changes:
            new_cursor_location = EXTRA_CONTROLS.index(control)
            for i in range(new_cursor_location - extras_cursor_location):
                extend(self.sequence, Buttons.DOWN)

            if control != "extra_sensibility": #sensibility doesn't work the same way
                # we always need to press left to change the control
                extend(self.sequence, Buttons.LEFT)
            
            else:
                if getattr(self, control) == 0:
                    extend(self.sequence, Buttons.LEFT)

                elif getattr(self, control) == 2:
                    extend(self.sequence, Buttons.LEFT, Buttons.RIGHT)
        extend(self.sequence, Buttons.PLUS)

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
        self.sequence = []
        
        delay(self.sequence, 250)

        extend(self.sequence, Buttons.DOWN)
        extend(self.sequence, Buttons.DOWN)
        extend(self.sequence, Buttons.RIGHT)
        extend(self.sequence, Buttons.A, delay=90)
        extend(self.sequence, Buttons.RIGHT)
        extend(self.sequence, Buttons.UP, delay=10)
        extend(self.sequence, Buttons.X, delay=16)
        extend(self.sequence, Buttons.RIGHT, delay=2)
        extend(self.sequence, Buttons.A, delay=20)
        extend(self.sequence, Buttons.DOWN, delay=15)
        extend(self.sequence, Buttons.A, delay=70)

        keyboard_sequence = generate_keyboard_path(self.tag)
        self.sequence.extend(keyboard_sequence)

        delay(self.sequence, 120)
        extend(self.sequence, Buttons.RIGHT, delay=2)
        extend(self.sequence, Buttons.RIGHT, delay=2)
        extend(self.sequence, Buttons.A, delay=30)

        self.sequence.extend(sequences.test_personal_sequence())
        return

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

        if go_to_left_row or go_to_extras:
            self.crawl_row(left_row_changes, LEFT_ROW, is_left_row=True)
            if go_to_extras:
                if self.cursor_location != 4: #if we aren't already on the other settings menu 
                    for i in range(4 - self.cursor_location):
                        extend(self.sequence, Buttons.DOWN)
                extend(self.sequence, Buttons.A)
                delay(self.sequence, 20)
                self.crawl_extras(extra_controls_changes, EXTRA_CONTROLS)
                self.cursor_location = 4
            if go_to_c_stick or go_to_right_row:

                if self.cursor_location < 3: #if we aren't already on the the down taunt button, or the other settings, both lead to the c stick
                    for i in range(3 - self.cursor_location):
                        extend(self.sequence, Buttons.DOWN)
                extend(self.sequence, Buttons.RIGHT)
                if go_to_c_stick:
                    extend(self.sequence, Buttons.A)
                    delay(self.sequence, 10)
                    self.select_control(self.__class__.R_STICK, self.R_STICK, True)
                extend(self.sequence, Buttons.RIGHT)
                if go_to_right_row:
                    self.crawl_row(right_row_changes, RIGHT_ROW, True)
        extend(self.sequence, Buttons.PLUS)
        self.sequence = flatten_list(self.sequence)

def generate_controls_sequence_gc(tag):
    """
    Returns a list of inputs to change the control scheme.
    This will probably be ugly.
    """
    controller = ControlScheme()
    controller.tag = tag
    controller.L = Controls.SPECIAL_ATTACK
    controller.D_UP = Controls.SHIELD
    controller.extra_tap_jump = 0
    controller.R_STICK = Controls.NORMAL_ATTACK
    controller.generate_controls_sequence_gc()
    return controller.sequence

class Stages:
    """I don't want to do that ... please"""
    stage_list = STAGE_LIST
    empty_list = STAGE_LIST_EMPTY

    def __init__(self):
        self.finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

    def get_stage_location(self, key)->list:
        """Returns the location of the key on the keyboard."""
        for row in self.keyboard:
            if key in row:
                return (row.index(key), self.keyboard.index(row))
        raise Exception("Key not found on keyboard.")


    def pathfind_stage(self, stage_location, location)->list:
        """
        Returns a list of coordinates to press the key.
        The location is the current location of the cursor on the keyboard.
        """

        grid = Grid(matrix=self.empty_list)
        start = grid.node(location[0], location[1])
        end = grid.node(stage_location[0], stage_location[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        return path, stage_location

    def find_closest_stage(self, reaming_stages_coordonates, location):
        """
        Tests the distance between the location and the remaining stages.
        Returns the closest stage.
        """
        closest_stage = None
        closest_distance = None
        for stage in reaming_stages_coordonates:
            print(stage)
            path, _ = self.pathfind_stage(stage, location)
            distance = len(path)
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_stage = stage
        return closest_stage

    def find_str_in_2d_array(self, string):
        """
        Returns the location of the string in the 2d array.
        """
        for row in self.stage_list:
            if string in row:
                return (row.index(string), self.stage_list.index(row))

    def stage_names_to_coordinates(self, stages):
        stages_coordonates = []
        for stage in stages:
            stages_coordonates.append(self.find_str_in_2d_array(stage))
        return stages_coordonates        

class RuleSet:
    style = 0 # 0 : time, 1 : stock, 2 : stamina
    stock = 3
    time = 0 # 0 is inf. 1 is 1:00, 2 is 1:30 ... 7 min is 9 (TimeValues.inf)
    fs_meter = False
    spirits = False
    cpu_lvl = 3
    damage_handicap = False
    stage_selection = 0 # StageSelectionType.anyone
    items = None
    stages = Stages()
    
    # advanced
    first_to = 1
    stage_morph = False
    stage_hazards = True 
    friendly_fire = False
    launch_rate = 1.0
    underdog_boost = False
    pause = True
    score = False
    show_damage = True

    sequence = []

    stages = []

    ruleset_name = "competitif"

    def __init__(self):
        self.style = 1 # competitive is in stock.

    def get_changed_rules(self, attributes):
        """
        Takes a list of attribute names (str) and compares the default value with the self value
        """

        default = []
        modified = []
        for rule in attributes:
            if callable(getattr(self, rule)):
                continue
            default.append(getattr(self.__class__, rule))
            modified.append(getattr(self, rule))
        return default, modified

    def edit_boolean_field(self, new_option):
        if new_option == True:
            extend(self.sequence, Buttons.RIGHT, delay=4)
        else:
            extend(self.sequence, Buttons.LEFT, delay=4)
        
    def edit_int_field(self, old, new):
        movement = new - old

        for _ in range(abs(movement)):
            if movement > 0:
                extend(self.sequence, Buttons.RIGHT, delay=1)
            else:
                extend(self.sequence, Buttons.LEFT, delay=1)

    def crawl_row(self, default, modified):
        if len(default) != len(modified):
            raise Exception
        for i in range(len(default)):
            if default[i] != modified[i]:
                if type(modified[i]) == bool:
                    self.edit_boolean_field(modified)
                elif type(modified[i]) == int:
                    self.edit_int_field(default[i], modified[i])
            extend(self.sequence, Buttons.DOWN, delay=1)

    def generate_ruleset_sequence(self):
        """This method is a flow, from the normal rules, to the items, to the stages, to the advanced."""
        # main menu to rulesets
        extend(self.sequence, Buttons.A, delay=10)
        extend(self.sequence, Buttons.A, delay=5)
        extend(self.sequence, Buttons.A, delay=130)
        extend(self.sequence, Buttons.UP, delay=3)
        extend(self.sequence, Buttons.A, delay=20)

        # normal options are the easiest
        default, modified = self.get_changed_rules(RULESET_ORDERS[0])
        self.crawl_row(default, modified)

        # Next are items 
        # we just disable items.
        extend(self.sequence, Buttons.A, delay=15)
        extend(self.sequence, Buttons.LEFT, delay=3)
        extend(self.sequence, Buttons.A, delay=5)
        extend(self.sequence, Buttons.B, delay=13)
        extend(self.sequence, Buttons.DOWN, delay=4)

        # Stages
        # I don't wanna do that
        # stages
        if self.stages != []:
            extend(self.sequence, Buttons.A, delay=15)
            extend(self.sequence, Buttons.LEFT, delay = 4)
            extend(self.sequence, Buttons.A, delay = 6)
            self.generate_stages_path(self.stages)
            extend(self.sequence, Buttons.B, delay=13)
        extend(self.sequence, Buttons.DOWN, delay=4)
        
        extend(self.sequence, Buttons.A, delay = 7)
        extend(self.sequence, Buttons.DOWN, delay=4)
        default, modified = self.get_changed_rules(RULESET_ORDERS[3])
        self.crawl_row(default, modified)
        extend(self.sequence, Buttons.A, delay=50)
        self.sequence.extend(generate_keyboard_path(self.ruleset_name))
        add_button(self.sequence, Buttons.LEFT, 40)
        add_button(self.sequence, Buttons.UP, 10)
        add_button(self.sequence, Buttons.A, 1)


        return self.sequence
        

    def generate_stages_path(self, stage_names:list) -> list:
        """
        We take the list of the stages, and we generate a list of inputs to go to each stage.
        This is hard.
        - Why ?
        Because, unlike with the keyboard, where there is a clear order of the keys. Here, we are cursed with the ability to optimize the pathfinding.
        This is also known as the Traveling Salesman Problem.
        We are just implementing the greedy algorithm.
        """
        stages = Stages()
        full_path = [] # the full path is a list of lists of coordinates to press the keys
        path = [] # the path is the temporary list of coordinates to go from one key to another
        location = [0, 0] #This is the initial location of the cursor on the beyboard.
        reaming_stages = stages.stage_names_to_coordinates(stage_names)

        for _ in range(len(reaming_stages)):
            closest_stage = stages.find_closest_stage(reaming_stages, location)
            path, location = stages.pathfind_stage(closest_stage, location) # the position of the current key is the new starting point for the next key
            full_path.append(path) # add the path from the previous key to the current key to the full path
            print("############")
            extend(full_path, Buttons.A) # press A after each key
            reaming_stages.remove(closest_stage) # remove the stage from reaming list
        full_sequence = generate_sequence_from_list(full_path)
        self.sequence.extend(full_sequence)

def generate_ruleset_sequence():
    ruleset = RuleSet()
    ruleset.ruleset_name = "wanted x zevent"
    ruleset.time = 9
    ruleset.stages = ["battlefield", "small_battlefield", "yoshis_story", "pokémon_stadium_2", "lylat_cruise", "hollow_bastion" ,"final_destination", "smashville"]
    delay(ruleset.sequence, 100)
    ruleset.stage_hazards = False
    ruleset.generate_ruleset_sequence()
    print(ruleset.sequence)
    return ruleset.sequence