# just to render them all.
# if possible.
# import text_to_image as tti
import cv2
import numpy as np
import math
# tti.encode("it does not work", "t")
# it does not work.
from PIL import Image, ImageFont, ImageDraw
# import os
PRE_CAL = 0.07
PRE_CAL = (1 - PRE_CAL, PRE_CAL)
PRE_CAL1 = math.sqrt((*PRE_CAL,)[1])  # really strange.
PRE_CAL1 = (*PRE_CAL,)[1]**(0.78)  # really strange.
PRE_CAL1 = (1-PRE_CAL1, PRE_CAL1)
# not too black?
# ok, just about having it.


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
# from PIL import Image, ImageFont, ImageDraw

# will my code blow your shit?


def cropImage(a):
    x, y = a.shape
    w, h = x//2, y//2
    # return [a[]]
    return [a[0:h, 0:  w], a[0:  h, w: x], a[h:y, 0:  w], a[h:y, w:x]]
# check them out.


def getTop(a):
    x, y = a.shape
    return [a[0:y, x-2:x], a[y-2:y, 0:x]]


def getDown(a):
    x, y = a.shape
    return [a[0:y, 0:2], a[0:2, 0:x]]


def getScheme(a):
    b, c = a[0], a[3]
    d, e = getTop(b)
    f, g = getDown(c)
    h = {"T": d, "L": e, "D": f, "R": g}
    return h


def sumMatrix(a):
    return np.mean(a)


def blackish(a):
    x, y = a.shape
    z = x*y
    return np.sum(a == 0)/z


def getRender(a):
    # check all the corners.
    assert type(a) == str and len(a) == 1
    text = u"{}".format(a)
    # what about other characters?
    # get info about different chars. get it especially on UNICODE OFFICIAL REFERENCE. EXTRACT FONT DATA FROM THEIR FUCKING PDFS.
    # text = u"这是一段测试文本，test 123。"
    im = Image.new("RGB", (50, 50), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    x = "C:\\WINDOWS\\FONTS\\msyh.ttc"
    # print(x)
    # bullshit.
    # just how does it looks like?
    # make it gray? or colorful?
    font = ImageFont.truetype(x, 30)
    dr.text((10, 5), text, font=font, fill="#000000")
    # you even have fill. what about unicode?
    im = pil2cv(im)
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    return im
# percentage: below 90 percent white?
# fully connected?


# print(PRE_CAL)
# print(PRE_CAL1)
# black: 0 white:255
# outdated code checking tool.
# UNICODE IS NOT SUPPORTED IN GNU NANO.
# HOW DOES THIS COME OUT?
def getJson(code):
    try:
        a = getRender(code)
        b = cropImage(a)
        d = ["TL", "TR", "DL", "DR"]
        e = {}
        # i={}
        m = sumMatrix(a) < 255*PRE_CAL[0]
        # print(m)
        n = sumMatrix(a) < 254.9
        # print(n)
        c = blackish(a) > 0
        i = {"visible": m, "painted": n, "pureBlack": c}
        for x in range(4):
            # print(b[x])
            m = sumMatrix(b[x]) < 255*PRE_CAL[0]
            # print(m)
            n = sumMatrix(b[x]) < 254.9
            # print(n)
            c = blackish(b[x]) > 0
            # print(c)
            # do we need overall things?
            e.update({d[x]: {"visible": m, "painted": n, "pureBlack": c}})
        h = getScheme(b)
        h = {x: sumMatrix(h[x]) for x in h.keys()}
        # binarize it.
        for x in h.keys():
            h.update({x: h[x] < 255 * PRE_CAL[0]})
        return {code: {"main": i, "blocks": e, "boundaries": h}}
    except:
        return {code: None}
    # just to try.
# print(e)
# print(h)
#     cv2.imshow(str(x), b[x])
#     # 0 - 1
#     # 2 - 3
# identical?
#     cv2.waitKey(0)
# # cv2.destroy
# cv2.destroyAllWindows()
# a matrix?
# print(type(im))
# great. now calculate the spec.
# im.show()
# this requires something.
# to numpy.
# print(type(dr))
# great?
# im.save('output.png')
#
