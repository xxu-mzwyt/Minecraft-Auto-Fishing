# image.py

#########################################
# Author: mzWyt
# Date: 19 Feb 2021
# Modified: 28 Feb 2021
#########################################
import time

import numpy
import pyautogui
import cv2

target, hTarget, wTarget = 0, 0, 0


def take_screenshot(x, y, w, h):  # 截图
    img = pyautogui.screenshot(region=[x, y, w, h])

    # img.save(".\\img.png")
    time.sleep(0.3)

    return img


def image_process(mode, img):
    # img = cv2.imread('.\\img.png', 1)  # 读入截图
    gray = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_BGR2GRAY)  # 灰度

    langs = ['.\\target_en.png', '.\\target_zh.png', '.\\target_oth.png']
    template = cv2.imread(langs[mode], 1)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)  # 模板匹配
    # cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 如果匹配度小于5%，就认为没有找到。
    print(max_val)

    if max_val > 0.98:
        return True
    else:
        return False

    # return False

    # if min_val > 0.05:
    #     return False
    # return True
    # strmin_val = str(min_val)

    # 以下为统计匹配个数：
    # 由于阈值问题，模板匹配基本不会输出false
    # 因此，统计大于0.5的匹配个数，如果匹配成功，个数应较少（少于等于8）

    # loc = np.where(result >= 0.95)
    #
    # cnt = 0
    # for i in zip(*loc[::-1]):
    #     cnt += 1
    # print(cnt)
    #
    # thresholds = [100, 30, 50]
    # if 0 < cnt <= thresholds[mode]:
    #     return True
    #
    # return False
