import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.interpolate import interp1d as spline
# import sys
# from groupMap import mapCluster as mapGroup
from groupMap import coorGet, checkContinual, mapBlank, getLine, getBatchDistance, centralDots

# read the image from arguments
image = cv2.imread("curve.png")
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
z3=[mapBlank(z2)]
# print(z3)
# get these dots.
# print(type(grayscale))
# print(grayscale)
z4 = {tuple(x): [a for b in [coorGet(np.where(grayscale == y)) for y in x] for a in b] for x in z3}
# print(z4)
z5 = z4[list(z4.keys())[0]]
z6 = checkContinual(z5)
# z7 = getLine(z6)
z9 = list(sorted(centralDots(z6),key=lambda x:x[0]))
# # print(z7)
# print(z9,len(z9))
cf = lambda c0: np.array(c0).transpose(1, 0)
cs = cf(z9)
X, Y = cs[0], cs[1]
xnew = np.linspace(X.min(), X.max(), 200)  #300 represents number of points to make between T.min and T.max
func = spline(X,Y,kind='cubic')

#利用xnew和func函数生成ynew,xnew数量等于ynew数量
ynew = func(xnew)
plt.plot(xnew, ynew)
plt.plot(X, Y, "b.")
plt.show()


# plt.show()
# z8 = getBatchDistance(z9, z7)
# print(z8)
# generate a function?
# are they close enough?
# detect surrounding.
# print(z6, len(z6))
# thirty five dots in total.
# what a wonderful world.
# now we have three dots.
# randomly pick up things?
# z5 = list(z4.keys())[0]
# z6 = z4[z5]
# print([type(x) for x in z6])
# print(grayscale == 168 or grayscale == 0)
# # get coordinate?