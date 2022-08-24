"""
This file will write the data to the board.
"""
import os
import time

def write_data(data):
    """
    This function will write the data to the board.
    """
    print(type(data))
    print("Waiting for board to be plugged in ...")
    timeout = 0
    while True:
        if os.path.exists("/Users/red/dev") or True:
            with open("/Users/red/dev/EEPROM.BIN", 'wb') as f:
                print("Writing data to board ...")
                f.write(data)
                f.close()
                print("Data written to board !")
                break
        timeout += 1
        if timeout > 100:
            print("ERROR: Could not write data to the board.")
            break
        time.sleep(0.3)
