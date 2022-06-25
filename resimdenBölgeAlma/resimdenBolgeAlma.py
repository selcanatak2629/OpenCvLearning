# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:32:38 2022

@author: selca
"""

import cv2

image = cv2.imread("baris.jpg")

kesit = image[50:150,300:400]
image[0:100,0:100] = kesit

image[:,:,0] = 255
image[400:450,300:350] = (0,150,255)

cv2.imshow("kesit alanı",kesit)
cv2.imshow("dunya barısı",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
