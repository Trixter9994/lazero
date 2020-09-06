import numpy as np
import matplotlib.pyplot as plt
import cv2
# import sys
from groupMap import mapCluster as mapGroup
from groupMap import coorGet, checkContinual

# read the image from arguments
image = cv2.imread("3dots.png")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(grayscale, 30, 100)
# print(grayscale.tolist())
x,y=len(grayscale),len(grayscale[0])
# print(x,y)
z = grayscale.flatten()
# print(z)
z0, z1 = set(z), np.bincount(z)
z2 = {x: z1[x] for x in z0}
# print(z2)
z3=mapGroup(z2)
print(z3)
# get these dots.
# print(type(grayscale))
# print(grayscale)
z4 = {tuple(x): [a for b in [coorGet(np.where(grayscale == y)) for y in x] for a in b] for x in z3}
# print(z4)
z5 = z4[list(z4.keys())[0]]
z6 = checkContinual(z5)
print(z6,len(z6))
# now we have three dots.
# randomly pick up things?
# z5 = list(z4.keys())[0]
# z6 = z4[z5]
# print([type(x) for x in z6])
# print(grayscale == 168 or grayscale == 0)
# # get coordinate?