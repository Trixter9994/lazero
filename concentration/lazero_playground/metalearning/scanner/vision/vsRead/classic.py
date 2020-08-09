import cv2
import pytesseract
from multiprocessing import Pool, freeze_support
# TimeoutError?
# use graph query to do this.
def parallel(x, v,z):
  with Pool(processes=x) as pool:
    return pool.map(v, z)
def getText(f):
  config = (" --oem 1 --psm 6") # LSTM is awful.
  return pytesseract.image_to_string(f, config=config,nice=0)
# def saveMe(a,b):
#     cv2.imwrite("dreamer/"+str(a)+".png",b)
# this is a simple method. we can adjust the values with ease.
# we can have different values with filter.
# x,y,w,h
# this cannot detect the line direction -> fourier transform -> linear analysis.
if __name__ == "__main__":
  freeze_support()
  # it has gaussian blur.
  image = cv2.imread('5.png')
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (9,3), 0)# odd different.
  thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,2))
  dilate = cv2.dilate(thresh, kernel, iterations=4)

  cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  ar=[]
  ROI_number = 0 # i must slice it around.
  
  # shall we use multithreading?
  # use multilanguage mode.
  # too fucking long.
  for c in cnts:
      # area=cv2.contourArea(c)
      x,y,w,h = cv2.boundingRect(c)
      f=image[y-4:y+8+h,x:x+w] # the way to crop the image.
      ar.append([f, [x,y,w,h]])  # we are gonna check this twice.
  for ra,rx in enumerate(parallel(12,getText,list(map((lambda x:x[0]),ar)))):
      text = rx
      x,y, w, h=ar[ra][1]
      cv2.rectangle(image, (x, y - 4), (x + w, 8 + y + h), (36, 255, 12), 3)
      cv2.putText(image,text,(int(x+w/2),int(y+h/2)),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
  af=0
  # for a0, b0 in ar:
  #     saveMe(af,a0)
  #     af+=1
  cv2.imshow('thresh', thresh)
  cv2.imshow('dilate', dilate)
  cv2.imshow('image', image)
  cv2.waitKey()
# this shit is production ready.
# better use char segments.