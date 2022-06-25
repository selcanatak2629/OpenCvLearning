# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:15:50 2022

@author: selca
"""

import cv2

import cv2

kemal_sunal_image = cv2.imread("kemal_sunal.jpg")

aynalama_resim = cv2.copyMakeBorder(
            kemal_sunal_image,100,100,325,325,
            cv2.BORDER_REFLECT) # üst,alt,sol,sağ

uzatilan_resim = cv2.copyMakeBorder(
            kemal_sunal_image,120,120,120,120,
            cv2.BORDER_REPLICATE)

tekrarlanan_resim = cv2.copyMakeBorder(
            kemal_sunal_image , 300, 300, 300, 300, 
            cv2.BORDER_WRAP)
sarilan_resim = cv2.copyMakeBorder(
            kemal_sunal_image , 50, 50, 50, 50, 
            cv2.BORDER_CONSTANT,
            value=(75,150,255))

cv2.imshow("aynalanan kemal sunal", aynalama_resim)
cv2.imshow("uzatilan kemal sunal", uzatilan_resim)
cv2.imshow("tekrarlanan kemal sunal", tekrarlanan_resim)
cv2.imshow("sarilan kemal sunal", sarilan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()