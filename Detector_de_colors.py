#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:48:36 2021

@author: swaglot
"""
'''
S'ha d'instal·lar la llibreria opencv
conda install opencv
Vaig tenir problemes amb la comanda anterior, vaig provar diverses coses i al final alguna em va funcionar (no sé quina)
'''
import cv2;
import numpy as np;
'''
Definim els rangs inferiors i superiors dels colors en format HSV 
Hue 0-179
Saturation 0-255
Value 0-255
Important: aquests rangs són vàlids només per la llibreria de phyton de opencv.
Altres plataformes usen intervals diferents i si vols saber-ne els valors equivalents has de fer la conversió pertinent.
'''

negreBaix=np.array([0, 0, 0], np.uint8)
negreAlt=np.array([27, 5, 51], np.uint8)

negreBaix2=np.array([0, 250, 0], np.uint8)
negreAlt2=np.array([27, 255, 51], np.uint8)

marroBaix=np.array([0, 200, 0], np.uint8)
marroAlt=np.array([9, 255, 102], np.uint8)

roigBaix=np.array([0, 250, 51], np.uint8)
roigAlt=np.array([1, 255, 165], np.uint8)

roigBaix2=np.array([176, 254, 51], np.uint8)
roigAlt2=np.array([179, 255, 165], np.uint8)

taronjaBaix=np.array([2, 250, 76], np.uint8)
taronjaAlt=np.array([8, 255, 204], np.uint8)

grocBaix=np.array([14, 250, 64], np.uint8)
grocAlt=np.array([22, 255, 196], np.uint8)

verdBaix=np.array([53, 250, 0], np.uint8)
verdAlt=np.array([72, 255, 102], np.uint8)

blauBaix=np.array([98, 250,0], np.uint8)
blauAlt=np.array([119, 255, 127], np.uint8)

lilaBaix=np.array([157, 100, 0], np.uint8)
lilaAlt=np.array([179, 255, 140], np.uint8)

grisBaix=np.array([0, 0, 0], np.uint8)
grisAlt=np.array([36, 153, 102], np.uint8)

blancBaix=np.array([9, 18, 64], np.uint8)
blancAlt=np.array([32, 102, 204], np.uint8)
'''
Obrim la imatge
'''
imatge=cv2.imread('Imatges_retallades/330k-0-H-G.png');
'''
Transformem la imatge de la variable imatge de RGB a HSV
'''
imatgeHSV=cv2.cvtColor(imatge, cv2.COLOR_BGR2HSV)
'''
La funció cv2.inRange(imatge, llindar_superior, llindar_inferior) retorna una imatge binaritzada (només blanc i negre).
Les seccions dins del rang apareixereran en blanc mentre les altres en negre
'''
areaNegre_blancbin=cv2.inRange(imatgeHSV, negreBaix, negreAlt);
areaNegre_blancbin2=cv2.inRange(imatgeHSV, negreBaix2, negreAlt2);

areaMarro_blancbin=cv2.inRange(imatgeHSV, marroBaix, marroAlt);
#areaMarro=cv2.bitwise_and(imatge, imatge, mask=areaMarro_blancbin)

areaRoig_blancbin=cv2.inRange(imatgeHSV, roigBaix, roigAlt);
areaRoig_blancbin2=cv2.inRange(imatgeHSV, roigBaix, roigAlt);

areaTaronja_blancbin=cv2.inRange(imatgeHSV, taronjaBaix, taronjaAlt);

areaGroc_blancbin=cv2.inRange(imatgeHSV, grocBaix, grocAlt);

areaVerd_blancbin=cv2.inRange(imatgeHSV, verdBaix, verdAlt);

areaBlau_blancbin=cv2.inRange(imatgeHSV, blauBaix, blauAlt);

areaLila_blancbin=cv2.inRange(imatgeHSV, lilaBaix, lilaAlt);

areaGris_blancbin=cv2.inRange(imatgeHSV, grisBaix, grisAlt);

areaBlanc_blancbin=cv2.inRange(imatgeHSV, blancBaix, blancAlt);

'''
La funció cv2.erode(imatge, filtre, #iteracions) retorna la imatge després d'aplicar-li el filtre d'erosió n vegades
La funció cv2.dilate(imatge, filtre, #iteracions) retorna la imatge després d'aplicar-li el filtre de dilatació n vegades      

Aplicar una erosió i despreś una dilatacioó serveix perquè aquells pixels blancs que no estiguin en conjunts numbrosos desapareguin.
Les dimensions del filtre especifiquen com de gran ha de ser aquesta agrupació de píxels blancs.
'''
kernel = np.ones((5,5), np.uint8)

areaNegre_blancbin = cv2.erode(areaNegre_blancbin, kernel, iterations=1)
areaNegre_blancbin = cv2.dilate(areaNegre_blancbin, kernel, iterations=1)

areaNegre_blancbin2 = cv2.erode(areaNegre_blancbin2, kernel, iterations=1)
areaNegre_blancbin2 = cv2.dilate(areaNegre_blancbin2, kernel, iterations=1)

areaMarro_blancbin = cv2.erode(areaMarro_blancbin, kernel, iterations=1)
areaMarro_blancbin = cv2.dilate(areaMarro_blancbin, kernel, iterations=1)

areaRoig_blancbin = cv2.erode(areaRoig_blancbin, kernel, iterations=1)
areaRoig_blancbin = cv2.dilate(areaRoig_blancbin, kernel, iterations=1)

areaRoig_blancbin2 = cv2.erode(areaRoig_blancbin2, kernel, iterations=1)
areaRoig_blancbin2 = cv2.dilate(areaRoig_blancbin2, kernel, iterations=1)

areaTaronja_blancbin = cv2.erode(areaTaronja_blancbin, kernel, iterations=1)
areaTaronja_blancbin = cv2.dilate(areaTaronja_blancbin, kernel, iterations=1)

areaGroc_blancbin = cv2.erode(areaGroc_blancbin, kernel, iterations=1)
areaGroc_blancbin = cv2.dilate(areaGroc_blancbin, kernel, iterations=1)

areaVerd_blancbin = cv2.erode(areaVerd_blancbin, kernel, iterations=1)
areaVerd_blancbin = cv2.dilate(areaVerd_blancbin, kernel, iterations=1)

areaBlau_blancbin = cv2.erode(areaBlau_blancbin, kernel, iterations=1)
areaBlau_blancbin = cv2.dilate(areaBlau_blancbin, kernel, iterations=1)

areaLila_blancbin = cv2.erode(areaLila_blancbin, kernel, iterations=1)
areaLila_blancbin = cv2.dilate(areaLila_blancbin, kernel, iterations=1)

areaGris_blancbin = cv2.erode(areaGris_blancbin, kernel, iterations=1)
areaGris_blancbin = cv2.dilate(areaGris_blancbin, kernel, iterations=1)

areaBlanc_blancbin = cv2.erode(areaBlanc_blancbin, kernel, iterations=1)
areaBlanc_blancbin = cv2.dilate(areaBlanc_blancbin, kernel, iterations=1)
#contorns,_=cv2.findContours(areaMarro_blancbin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#for c in contorns:
#    area=cv2.contourArea(c)
#    if area > 1:
#        cv2.drawContours(areaMarro_blancbin, [c], 0, [255, 0, 0], 1)
'''
Mostrem totes les imatges
'''      
cv2.imshow('Detecio_Negre', areaNegre_blancbin)
cv2.imshow('Detecio_Negre2', areaNegre_blancbin2)
cv2.imshow('Detecio_Marro', areaMarro_blancbin)
cv2.imshow('Detecio_Roig', areaRoig_blancbin)
cv2.imshow('Detecio_Roig2', areaRoig_blancbin2)
cv2.imshow('Detecio_Taronja', areaTaronja_blancbin)
cv2.imshow('Detecio_Groc', areaGroc_blancbin)
cv2.imshow('Detecio_Verd', areaVerd_blancbin)
cv2.imshow('Detecio_Blau', areaBlau_blancbin)
cv2.imshow('Detecio_Lila', areaLila_blancbin)
cv2.imshow('Detecio_Gris', areaGris_blancbin)
cv2.imshow('Detecio_Blanc', areaBlanc_blancbin)
'''
Les dues darreres comandes serveixen perquè es tanqui les finestres el pitjar qualsevol tecla (temps d'espera 0s)
''' 
cv2.waitKey(0)
cv2.destroyAllWindows()