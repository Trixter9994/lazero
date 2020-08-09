# import cv2
import pytesseract
import cv2 as cv
import cv2
# import numpy as np
from skimage.filters import threshold_niblack, threshold_sauvola
import numpy as np

# def calcMe(x):
#     print(x.min(), x.max())
# # no greater, no lower?


def toReal(data):
    data = np.where(data <= 1, data, 1)
    data = np.where(data >= 0, data, 0)
    return data


def clahe_demo(image):
    # gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    gray = image
    clahe = cv.createCLAHE(5, (8, 8))
    dst = clahe.apply(gray)
    return dst
    # cv.namedWindow("clahe_demo", cv.WINDOW_NORMAL)
    # cv.imshow("clahe_demo", dst)
# shot along the place?
# for text?
# nah. we will try manga.
# def rgb2gray(img):
#     h=img.shape[0]
#     w=img.shape[1]
#     grayimg = np.zeros((h, w), np.uint8)
#     # wow this is magical.
#     for i in range (h):
#         for j in range (w):
#             grayimg[i,j]=0.144*img[i,j,0]+0.587*img[i,j,1]+0.299*img[i,j,2]
#     return grayimg

# def bernsens(img):
#     h=img.shape[0]
#     w=img.shape[1]
#     img1=np.zeros((h,w),np.uint8)
#     for i in range (1,h-1):
#         for j in range (1,w-1):
#             matrix=np.zeros((3,3),np.uint8)
#             for k in range (-1,2):
#                 for l in range (-1,2):
#                     matrix[k+1,l+1]=img[i+k,j+l]
#             threshold=(np.max(matrix)+np.min(matrix))/2
#             if img[i,j]>=threshold:
#                 img1[i,j]=255
#             else:
#                 img1[i,j]=0
#     return img1


def cod16(image):
  # hint: increase contrast.
  window_size = 3
  # image = cv.imread("sample2.jpg")
#   image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
  # ix = lambda i: cv.cvtColor(i, cv.COLOR_RGB2GRAY)
  # print(type(image),image.shape)
  # print(image)
  image = clahe_demo(image)
  # must use gray.
  # print("spliter")
  # that is fucking insane.
  thresh_niblack = (toReal(threshold_niblack(
      image, window_size=window_size, k=3))*255.0).astype(np.uint8)
  thresh_sauvola0 = (toReal(threshold_sauvola(
      image, window_size=3, k=1.303))*255.0).astype(np.uint8)  # for full scan?
  # perfect inverse of the one above
  thresh_sauvola1 = (toReal(threshold_sauvola(
      image, window_size=3, k=0.999999999999999999))*255.0).astype(np.uint8)  # for button detection?
  # just filter those things out.
  # thresh_niblack = threshold_niblack(image, window_size=window_size, k=12).astype(np.uint8)
  # thresh_sauvola0 = threshold_sauvola(image, window_size=3, k=1.103).astype(np.uint8)  # for full scan?
  # # perfect inverse of the one above
  # thresh_sauvola1 = threshold_sauvola(image, window_size=3, k=1.523).astype(np.uint8)  # for button detection?
  # print(type(thresh_niblack), thresh_niblack.shape)
  # print(type(thresh_niblack[0][0]))
  # ndarray.
  # it just cannot be right. give it up?
  # the shape can differ.
  # calcMe(thresh_niblack)
  # calcMe(thresh_sauvola0)
  # calcMe(thresh_sauvola1)
  # cv.imshow("grayimage",thresh_niblack)
  # cv.waitKey(0)
  # cv.imshow("thresholdimage", thresh_sauvola0)
  # cv.waitKey(0)
  # cv.imshow("thresholdimage", thresh_sauvola1)
  # cv.waitKey(0)
  # cv.destroyAllWindows()
  # return
  # # use floor function?
  # # just what the fuck?
  return thresh_niblack, thresh_sauvola0, thresh_sauvola1

def getText(f):
    config = ("--oem 1 --psm 6")  # LSTM is awful.
    # get it a try.
    # must likely we shall use a language detector before use?
    return pytesseract.image_to_string(f, lang="chi_sim+eng", config=config, nice=0)
    # no other shits.
# is it really good?
# should we cut it?
# only four bounds.

# def getRead(sx):
#   image = cv2.imread(sx)
#   # what the hell?
#   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#   g = getText(gray)
#   return g



# # if __name__ == '__main__':
def getRead(sx):
    # image = cv2.imread(sx)
    ratio = 1
    image = cv2.imdecode(np.fromfile(sx, dtype=np.uint8), 0)
    # cv2.imshow("original",image)
    img = cv2.resize(image, (int(
        image.shape[1] / ratio), int(image.shape[0] / ratio)), cv2.INTER_NEAREST)
    # retval, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    # cv2.imshow("original",image)
    # cv2.imshow("original",image)
    # print(img.shape)

    # cv2.namedWindow('OTSU threshold',0)
    # cv2.imshow('OTSU threshold',otsu)
    # cv2.imwrite('otsu_results.jpg',otsu)
    # time_start = time.time()
    thresh = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    thresh = cv2.adaptiveThreshold(
        thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    a= cod16(thresh)
    for x in a:
        cv2.imshow("display",x)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#     ratio = 1
# this is indeed shit. give it up.
#     image = cv2.imdecode(np.fromfile(sx, dtype=np.uint8), 0)
#     # cv2.imshow("original",image)
#     img = cv2.resize(image, (int(
#         image.shape[1] / ratio), int(image.shape[0] / ratio)), cv2.INTER_NEAREST)
#     # retval, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
#     # cv2.imshow("original",image)
#     # cv2.imshow("original",image)
#     # print(img.shape)

#     # cv2.namedWindow('OTSU threshold',0)
#     # cv2.imshow('OTSU threshold',otsu)
#     # cv2.imwrite('otsu_results.jpg',otsu)
#     # time_start = time.time()
#     thresh = cv2.adaptiveThreshold(
#         img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
#     thresh = cv2.adaptiveThreshold(
#         thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
#     retval, thresh = cv2.threshold(thresh, 150, 255, cv2.THRESH_OTSU)
#     # retval, thresh = cv2.threshold(img, retval, 255, cv2.THRESH_OTSU)
#     # cv2.imshow("original", thresh)
#     # print(type(thresh))
#     return getText(thresh)
    # print(thresh.shape)

# it is shit.
print(getRead("the_trench.jpg"))

# cv2.namedWindow('OTSU threshold', 0)
# cv2.imshow('OTSU threshold', thresh) # use this one.
# print(thresh.shape)
# time_end = time.time()
# print('thresh cost', time_end - time_start)
# # this is rather quick.
# # cv2.imwrite('otsu_results.jpg',otsu)
# # # retval, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_OTSU)
# # # retval, thresh = cv2.threshold(img, retval, 255, cv2.THRESH_OTSU)
# # # what about this one?

# time_start = time.time()
# roii = cv2.integral(img)
# time_end = time.time()
# print('integral cost', time_end - time_start)

# time_start = time.time()
# # what is this integral anyway?
# for j in range(1):
#     thresh = thresholdIntegral1(img, roii)
# time_end = time.time()
# print('totally cost', time_end - time_start)
# cv2.namedWindow('fast inergral threshold', 0)
# cv2.imshow('fast inergral threshold', thresh)
# # not too goddamn bad.
# # # cv2.imwrite('results.jpg', np.uint8(thresh))
# # time_start = time.time()
# # roii = cv2.integral(img)
# # time_end = time.time()
# # print('integral cost', time_end - time_start)
# # # time_start = time.time()
# # for j in range(1):
# #     thresh = thresholdIntegral(img, roii)
# # time_end = time.time()
# # print('totally cost', time_end - time_start)
# # cv2.namedWindow('integral threshold',0)
# # cv2.imshow('integral threshold',thresh)
