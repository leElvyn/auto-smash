#
#             LUFA Library
#     Copyright (C) Dean Camera, 2014.
#
#  dean [at] fourwalledcubicle [dot] com
#           www.lufa-lib.org
#
# --------------------------------------
#         LUFA Project Makefile.
# --------------------------------------

# Run "make help" for target help.

# Set the MCU accordingly to your device (e.g. at90usb1286 for a Teensy 2.0++, or atmega16u2 for an Arduino UNO R3)
MCU          = atmega32u4
ARCH         = AVR8
F_CPU        = 16000000
F_USB        = $(F_CPU)
OPTIMIZATION = s
TARGET       = src/Joystick
SRC          = $(TARGET).c Descriptors.c $(LUFA_SRC_USB)
LUFA_PATH    = ./lufa/LUFA
CC_FLAGS     = -DUSE_LUFA_CONFIG_HEADER -IConfig/
LD_FLAGS     = -lm

ARDUINO_PATH = /home/red/arduino-1.8.16/hardware/tools/avr/avr
INCLULDE_DIR += $(ARDUINO_PATH)/include/

CC_FLAGS += -I$(ARDUINO_PATH)/include/ -mmcu=$(MCU)
# Default target
all:

# Include LUFA build script makefiles
include $(LUFA_PATH)/Build/lufa_core.mk
include $(LUFA_PATH)/Build/lufa_sources.mk
include $(LUFA_PATH)/Build/lufa_build.mk
include $(LUFA_PATH)/Build/lufa_cppcheck.mk
include $(LUFA_PATH)/Build/lufa_doxygen.mk
include $(LUFA_PATH)/Build/lufa_dfu.mk
include $(LUFA_PATH)/Build/lufa_hid.mk
include $(LUFA_PATH)/Build/lufa_avrdude.mk
include $(LUFA_PATH)/Build/lufa_atprogram.mk

# Target for LED/buzzer to alert when print is done
with-alert: all
with-alert: CC_FLAGS += -DALERT_WHEN_DONE
