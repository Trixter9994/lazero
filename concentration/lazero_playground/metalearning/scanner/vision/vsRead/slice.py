import cv2
import pytesseract
# def saveMe(a,b):
#     cv2.imwrite("dreamer/"+str(a)+".png",b)
# this is a simple method. we can adjust the values with ease.
# we can have different values with filter.
# this cannot detect the line direction -> fourier transform -> linear analysis.
# will never fucking work.
image = cv2.imread('dreamer/9.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (11,11), 0)
(T, threshInv) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
# print(gray,type(gray))
cv2.waitKey()
# dimension is three.
# this shit is production ready.
# better use char segments.
# we do not have this shit so far. translate it into the thing.
"""
003D = EQUALS SIGN
• other related characters:  ≁ –  ≣
→  ≠ not equal to
→  ≡ identical to
→  ꞊ modifier letter short equals sign
→  𐆐 roman sextans sign
"""
# can we use this to crack unknown pdf codes? yes of course.