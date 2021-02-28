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

def img_init(mode):
    global target
    langs = ['.\\target_en.png', '.\\target_zh.png', '.\\target_oth.png']
    target = cv2.imread(langs[mode])
    return target.shape[:2]

def img_process(hTarget, wTarget):
    global target
    # print(wTarget, hTarget)
    img = cv2.imread('.\\img.png', 1)  # 读入截图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度

    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 大津法二值化

    cv2.imwrite('.\\dst.png', dst)

    h, w = dst.shape[:2]
    
    hProj = [0] * h  # 水平投影数组
    for y in range(h):  # 统计白色像素个数
        for x in range(w):
            if dst[y, x] == 255:
                hProj[y] += 1

    hStart = []
    hEnd = []
    currLine = False
    
    for i in range(h):  # 统计所有行的边界
        if not currLine and hProj[i] > 0:
            hStart.append(i)
            currLine = True
        if currLine and hProj[i] == 0:
            hEnd.append(i)
            currLine = False

    if len(hStart) > len(hEnd):  # 若最后一行不完整，补全end数组
        hEnd.append(h)

    for i in range(len(hStart)):  # 遍历每一行
        dstCrop = dst[hStart[i]:hEnd[i], 0:w]

        hCrop = hEnd[i] - hStart[i]
        
        vProj = [0] * w  # 垂直投影数组
        for x in range(w):  # 统计白色像素个数
            for y in range(hCrop):
                if dstCrop[y, x] == 255:
                    vProj[x] += 1
        
        vStart = 0
        vEnd = 0
        currLine = False

        for j in range(w):  # 统计左右边界
            if not currLine and vProj[j] > 0:
                if vStart == 0:  # 只保留第一个start
                    vStart = j
                currLine = True
            if currLine and vProj[j] == 0:
                vEnd = j
                currLine = False
        try:
            dstCrop = dstCrop[0:hCrop-1, vStart:vEnd]  # 截取只含文字的部分
            dstResized = cv2.resize(dstCrop, (wTarget, hTarget))
            cv2.imwrite('.\\test.png', dstResized)
            diff = 0
            for x in range(wTarget):
                for y in range(hTarget):
                    if not (dstResized[y, x] == target[y, x]).any:
                        diff += 1
            print('diff', diff)
        except EOFError as err:
            # print(err)
            pass

    print('false')
    return False
    
