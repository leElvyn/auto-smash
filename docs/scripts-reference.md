# Did you said "scripts" ?

Scripts are a list of inputs stored on the board (usually on the EEPROM) that should be replayed when the board is plugged in.

Currently, scripts are stored in a binary format, representing the raw eeprom of the board.

## Format : 

The eeprom of an ATMEGA32U4 is 1024 byetes in size. 

### Special bytes :

The first 8 bytes of the EEPROM are reserved for the script's settings.

There are 8 bytes, so 8x8 = 64 bits. 

Currently, there are only one of these settings, others are reserved for further use.

- 1st bit (bit 0) : replay. If this bit is set, the script will play indefinitly. if it isn't, the board will stop whenever the script is finished.

### Script bytes :

Every other bytes are used to store the script. every input is a combinaison of 2 bytes (limiting the length of a maximum of 512 inputs), the first one being the length, in frames, of the input, and the second one being the button. Buttons values can be found [here](docs/buttons.md).