import cv2
import pytesseract

def getText(f):
  config = ("--oem 1 --psm 6")  # LSTM is awful.
  # get it a try.
  # must likely we shall use a language detector before use?
  return pytesseract.image_to_string(f, lang="chi_sim+eng", config=config, nice=0)
  # no other shits.
# is it really good?
# should we cut it?
def getRead(sx):
  image = cv2.imread(sx)
  # what the hell?
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  print(type(gray))
  print(gray.shape)
#   g = getText(gray)
#   return g

print(getRead("the_trench.jpg"))
