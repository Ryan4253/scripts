# Elden Ring Rune Farming Script. Equip sacred relic sword at palace approach ledge road
# Press f12 to pause / unpause the script 
# Scripts required: pydirectinput

import pydirectinput as pdi
from time import time, sleep
import keyboard

KEYBOARD_STATE = {}

def changedToPressed(key : str) -> bool:
    state = keyboard.is_pressed(key)
    prev = False if not key in KEYBOARD_STATE else KEYBOARD_STATE[key]
    KEYBOARD_STATE[key] = state

    if state is True and prev is False:
        return True
    return False

def pausableSleep(timeout : float, key : str):
    startTime = time()
    while time() - startTime < timeout:
        sleep(0.01)
        if not changedToPressed(key):
            continue

        print('Pause')
        while not changedToPressed(key):
            sleep(0.01)
        print('Resume')

while True:
    pdi.press('g')    
    pausableSleep(0.1, 'f12')

    pdi.press('f')  
    pausableSleep(0.1, 'f12')

    pdi.press('e')
    pausableSleep(0.1, 'f12')

    pdi.press('e')   
    pausableSleep(5.8, 'f12')

    pdi.keyDown('w')
    pausableSleep(3.9, 'f12')
    pdi.keyUp('w')    
    pausableSleep(0.1, 'f12')

    pdi.keyDown('a')
    pausableSleep(1, 'f12')
    pdi.keyUp('a')    
    pausableSleep(0.1, 'f12')

    pdi.keyDown('w')
    pausableSleep(1.4, 'f12')
    pdi.keyUp('w')    
    pausableSleep(0.1, 'f12')

    pdi.press('shift')    
    pausableSleep(6, 'f12')
