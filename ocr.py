# ocr.py
#########################################
# Author: mzWyt
# Date: 19 Feb 2021
#########################################

import pytesseract
from PIL import Image
import cv2

def img_to_text():
    img = cv2.imread('.\img.png', 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = 255 - gray
    # cv2.imshow('dst', dst)
    # cv2.waitKey(0)
    cv2.imwrite('.\img_dst.png', dst)

    image = Image.open('.\img_dst.png')
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)