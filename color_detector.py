#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:48:36 2021

@author: swaglot
@coauthor: Albert
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

class _Image():
    def __init__(self, path=''):
        self.path = path
        if self.path != '' and self.path != None:
            img = cv2.imread(self.path)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        else:
            img = None
            imgHSV = None
        self.img = img
        self.imgHSV = imgHSV
        self.areas = dict()

    def set_img(self, path):
        self.path = path
        self.img = cv2.imread(self.path)
        self.imgHSV = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def set_areas(self, areas_lower, areas_upper, names, kernel=np.ones((5,5), np.uint8), iterations=1):
        if self.imgHSV.all() == None: raise Exception('No image was declared. HSV is NONE and probably img is also')
        if len(areas_lower) is len(names) and len(areas_upper) is len(areas_lower):
            for i in range(len(names)):
                area = cv2.inRange(self.imgHSV, areas_lower[i], areas_upper[i])
                self.areas[names[i]] = cv2.dilate(cv2.erode(area, kernel, iterations), kernel, iterations)
        else:
            raise Exception("Lists do not have same length. Expect an N length lists containing the differents areas.")

class _Thresholds():
    thresh = dict()
    thresh["NEGRE_LOWER"]=np.array([0, 0, 0], np.uint8)
    thresh["NEGRE_UPPER"]=np.array([179, 85, 84], np.uint8)
    thresh["MARRO_LOWER"]=np.array([0,127,127], np.uint8)
    thresh["MARRO_UPPER"]=np.array([36,170,170], np.uint8)
    thresh["ROIG_LOWER"]=np.array([0, 127, 170], np.uint8)
    thresh["ROIG_UPPER"]=np.array([1, 255, 255], np.uint8)
    thresh["TARONJA_LOWER"]=np.array([2, 127,170], np.uint8)
    thresh["TARONJA_UPPER"]=np.array([10, 255, 255], np.uint8)
    thresh["GROC_LOWER"]=np.array([11, 127, 170], np.uint8)
    thresh["GROC_UPPER"]=np.array([36, 255, 255], np.uint8)
    thresh["VERD_LOWER"]=np.array([37, 127, 170], np.uint8)
    thresh["VERD_UPPER"]=np.array([84, 255, 255], np.uint8)
    thresh["BLAU_LOWER"]=np.array([85, 127, 170], np.uint8)
    thresh["BLAU_UPPER"]=np.array([138, 255, 255], np.uint8)
    thresh["LILA_LOWER"]=np.array([139, 127, 170], np.uint8)
    thresh["LILA_UPPER"]=np.array([179, 255, 255], np.uint8)
    thresh["GRIS_LOWER"]=np.array([0, 0, 85], np.uint8)
    thresh["GRIS_UPPER"]=np.array([179, 85, 169], np.uint8)
    thresh["BLANC_LOWER"]=np.array([0, 0, 170], np.uint8)
    thresh["BLANC_UPPER"]=np.array([179, 85, 255], np.uint8)

img = _Image()
img.set_img('./Imatges_retallades/680k-0-D-G.png')
thresh_lower = []
thresh_upper = []
for thresh in _Thresholds.thresh:
    if 'LOWER' in thresh:
        thresh_lower.append(_Thresholds.thresh[thresh])
    else:
        thresh_upper.append(_Thresholds.thresh[thresh])

names = ['negre', 'marro', 'roig', 'taronja', 'groc', 'verd', 'blau', 'lila', 'gris', 'blanc']
img.set_areas(thresh_lower, thresh_upper, names)

FIG = plt.figure(figsize=(10, 10))

i=1
for area in img.areas:
    FIG.add_subplot(int(len(img.areas)/3+1), 3, i)
    plt.imshow(img.areas[area], interpolation='none', cmap='gray',aspect='equal')
    plt.axis('off')
    plt.title(area)
    i+=1

plt.show()
