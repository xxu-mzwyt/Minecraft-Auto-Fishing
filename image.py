# image.py

#########################################
# Author: mzWyt
# Date: 19 Feb 2021
# Modified: 28 Feb 2021
#########################################

import pyautogui
from PIL import Image
import cv2
import numpy as np


target, hTarget, wTarget = 0, 0, 0

def take_screenshot(x, y, w, h):  # 截图
    img = pyautogui.screenshot(region=[x, y, w, h]) 
    img.save(".\\img.png")

def image_convert():
    img = cv2.imread('.\\target_oth.png', 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('.\\target_oth.png', dst)

def image_process(mode):
    img = cv2.imread('.\\img.png', 1)  # 读入截图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度

    langs = ['.\\target_en.png', '.\\target_zh.png', '.\\target_oth.png']
    template = cv2.imread(langs[mode], 1)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    loc = np.where(result >= 0.5)

    cnt = 0
    for i in zip(*loc[::-1]):
        cnt += 1
    print(cnt)
    if cnt > 0 and cnt <= 8:
        return True
    return False
