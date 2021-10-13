"""
Will convert arrays of actions to a bytearray.
"""

def convert_to_bytearray(actions: list)-> bytearray:
    """
    Will convert an array of actions to a bytearray.
    """
    bytes_array = bytearray()
    for action in actions:
        bytes_array.append(action.duration)
        bytes_array.append(action.button.value)
    return bytes_array