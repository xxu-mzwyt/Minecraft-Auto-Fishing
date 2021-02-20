# screenshot.py
#########################################
# Author: mzWyt
# Date: 19 Feb 2021
#########################################

import pyautogui

def take_screen_shot(x, y, w, h):
    img = pyautogui.screenshot(region=[x, y, w, h])
    img.save(".\img.png")