# import the necessary packages
from skimage.measure import compare_ssim
# import argparse
import imutils
import cv2
import classic
import defRandom
import numpy as np
# import cv2


def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image
# fuck these people. I just want to backup my fucking behavior, making it indexable.
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
# 	help="first input image")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
# args = vars(ap.parse_args())
# randomly select the interval.
# load the two input images
# crop them.
def getEnhanced(image):
  return cv2.equalizeHist(image)
def cropDifference(first,second):
  imageA = pil2cv(first)
  imageB = pil2cv(second)
  # convert the images to grayscale
  grayA = getEnhanced(cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY))
  grayB = getEnhanced(cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY))

  # compute the Structural Similarity Index (SSIM) between the two
  # images, ensuring that the difference image is returned
  (score, diff) = compare_ssim(grayA, grayB, full=True)
  diff = (diff * 255).astype("uint8")
  # print("SSIM: {}".format(score))

  # threshold the difference image, followed by finding contours to
  # obtain the regions of the two input images that differ
  thresh = cv2.threshold(diff, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
  cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
  cnts = imutils.grab_contours(cnts)

  # loop over the contours
  cnt=[]
  for c in cnts:
    # only recongnize selected few?
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    x, y, w, h = cv2.boundingRect(c)
    area=cv2.contourArea(c)
    cnt.append([imageB[y: y + h, x: x + w], [x, y, w, h], area])
  cnt0, cnt1 = list(reversed(sorted(cnt,key=(lambda x: x[2]))))[:5], []
  # no children allowed.
  for axr, amr in enumerate(classic.parallel(3,classic.getText,list(map((lambda x: x[0]), cnt0)))):
    text = amr
    cnt1.append([text, cnt0[axr][1]])
  return cnt1
    # f0=classic(f)
    # only get one single image. the latter one.
    # cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # get the text.
    # process -> wait -> process
    # cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
  # show the output images
  # cv2.imshow("Original", imageA)
  # cv2.imshow("Modified", imageB)
  # cv2.imshow("Diff", diff)
  # cv2.imshow("Thresh", thresh)
  # cv2.waitKey(0)
