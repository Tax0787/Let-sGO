#!/usr/bin/python
# -*- coding: utf-8 -*-

#GO.py

from random import randint as r
from os import system as s
from abc import ABCMeta, abstractmethod
from time import sleep as waiting

class DidntPipInstallKeyboardPkgErrBeforeExecOrBuildErr(Exception):pass
DPIKPEBEOBE = DidntPipInstallKeyboardPkgErrBeforeExecOrBuildErr

class DidntMakeOption(Exception): pass
DMO = DidntMakeOption

try:
    from option import clr as clrtxt, end_key
    STOP = end_key
except:
    raise DMO("Nah Didn't make option.py and string value of var 'clr' & 'end_key'.....")

try:
    from keyboard import add_hotkey, wait
    SENSER, MAINLOOP = add_hotkey, wait
except:
    raise DPIKPEBEOBE("Dev Fault ; didn't `pip install keyboard` before setting runtime")

clr = lambda : s(clrtxt)

BackColors = lambda : r(40, 47) if r(0, 1) else r(100, 107)
ChangeColor = lambda : print('\033[{}m'.format(BackColors()))

def event(self):
    print('\a')
    clr()
    ChangeColor()

def END():
    clr()
    waiting(1)
    clr()
    print('\033[0m')

class AppCore(metaclass = ABCMeta):
    def __init__(self):
        clr()
        SENSER('space', self.__EVENT);
        SENSER(STOP, END);
        MAINLOOP(STOP);
        END()
    
    @abstractmethod
    def __EVENT(self):
        pass

def AppGen(func):
    return type('App', (AppCore, ), {'_AppCore__EVENT' : func})

main = AppGen(event)

if __name__ == "__main__": main()
