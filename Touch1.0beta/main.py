"""
ElectrOS, 2016

Raspbian Desktop Overlay

Program meant on use of Raspberry Pi Computer, specifically touchscreens.

Open-Source

v. 1.0 beta
"""

import time
import sys
import thread

import sudo #ElectrOS mudule to make sure 3rd party applications are not messing with system files
import systemScreens

version = 1.0
state = "beta"

security = sudo.Master()
thread.start_new_thread( security.security, () )

        

defScreens = systemScreens.DefScreens()
firstTime = systemScreens.FirstTime()

defScreens.boot_animation()

firstTime.screen1(version)

defScreens.loop()


