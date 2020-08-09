import cv2
import matplotlib.pyplot as plt
# just what the fuck is this?
# read the image
image = cv2.imread("7_fs_40_bc_255.A.png")
# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# create a binary thresholded image
# what is the way of decomposing?
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
plt.imshow(binary, cmap="gray")
plt.show()
# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
print(contours,hierarchy)
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)
# show the image with the drawn contours
# what the fuck is this?
# it does has the contour somehow. but what is the semantic meaning? what does this fucking shape mean?
# shall we use that thing? No please no.
plt.imshow(image)
plt.show()