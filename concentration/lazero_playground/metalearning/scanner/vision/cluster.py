import cv2
# import numpy as np
import csv
# use k-means twice?
def writer(a, b):
  with open(a+".csv", "a+",newline="") as f:
    c = csv.writer(f)
    for d in b:
      c.writerow(d)
    # f.write("\b")
img = cv2.imread('book.bmp')
# print(img)
x, y = len(img), len(img[0])
for x0 in range(x):
  writer("stream", [["object" + "-".join(list(map(str, [x0, y0])))] + img[x0][y0].tolist() for y0 in range(y)])
    # they are different. but we can mix them up somehow.