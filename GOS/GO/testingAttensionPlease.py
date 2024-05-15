#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#testingAttensionPlease.py

from keyboard import add_hotkey, wait
SENSOR, MAINLOOP = add_hotkey, wait

def LET_SGOi(func):
    #HAHA GAZA--!
    SENSOR('space', func); #space -> func
    SENSOR('enter', quit); #enter -> quit
    MAINLOOP()

@LET_SGOi
def BroNeedOscarHA_HA_HA():
    print("\t YO BRUH NEED 『OSCAR』")
