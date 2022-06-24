# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 23:19:44 2022

@author: selca
"""

import cv2

butterfly_images = cv2.imread("butterfly.jpg")

cv2.imshow("kelebek resmi", butterfly_images)

#bgr değeri(renk degerleri)
print(butterfly_images[(230,80)]) # assagı-sağa

cv2.waitKey(0)
cv2.destroyAllWindows()

