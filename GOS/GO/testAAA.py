import keyboard

keyboard.add_hotkey('space', lambda: print("YO!"))

keyboard.add_hotkey('ctrl+enter', lambda: quit())

keyboard.wait('ctrl+space')