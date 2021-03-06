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

def image_process(mode):
    img = cv2.imread('.\\img.png', 1)  # 读入截图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度

    langs = ['.\\target_en.png', '.\\target_zh.png', '.\\target_oth.png']
    template = cv2.imread(langs[mode], 1)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)  # 模板匹配
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    # 以下为统计匹配个数：
    # 由于阈值问题，模板匹配基本不会输出false
    # 因此，统计大于0.5的匹配个数，如果匹配成功，个数应较少（少于等于8）

    loc = np.where(result >= 0.3)

    cnt = 0
    for i in zip(*loc[::-1]):
        cnt += 1
    # print(cnt)

    thresholds = [100, 30, 50]
    if cnt > 0 and cnt <= thresholds[mode]:
        return True

    return False
