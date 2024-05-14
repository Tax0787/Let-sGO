#!/bin/sh
sh getpkg.sh
pyinstaller -F --icon="icon.ico" GO.py
