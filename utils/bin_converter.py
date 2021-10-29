"""
Will convert arrays of actions to a bytearray.
"""

def prepare_for_flashing(actions: list)-> bytearray:
    """
    Will convert an array of actions to a bytearray, as well as adding the first 8 empty bytes for settings
    """
    bytes_array = bytearray()
    settings_empty = [0, 0, 0, 0, 0, 0, 0, 0]
    bytes_array.extend(settings_empty)
    for action in actions:
        bytes_array.append(action.duration)
        bytes_array.append(action.button.value)
    return bytes_array