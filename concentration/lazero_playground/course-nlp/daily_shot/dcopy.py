import pyautogui
import time
from stackMe import queue
import multiprocessing
import fuckMe
def getDone(a,b):
  with open(b,"w+") as f:
    f.write(a)
def saveSession(a,b,c=2):
  a0 = int(time.time())
  for x, y in a:
    if len(x)>=c:
      getDone(x, b + "\\" + str(a0) + "-" + str(y)[1:-1].replace(" ", ""))
def default(x):
  time.sleep(x)
  return pyautogui.screenshot()
def getCore():
  # no just consider normal situation.
  return queue(2)
def checkState(a):
  return a.length() == 2
if __name__ == "__main__":
  multiprocessing.freeze_support()
  f=getCore()
  while True:
    d = default(5)
    # print(type(d))
    f.queue(d)
    if checkState(f):
      x,y=f.dump()
      c0 = fuckMe.cropDifference(x, y)
      saveSession(c0,"point_of_plot")
      # print("________________________________")
      # print(c0)
      # print("________________________________")
  # do the logging.
# time.sleep(1)
# pyautogui.click(button="right")
# s0=pyautogui.screenshot()
# just let my fucking life become easier.
# store the thing into a txt file.
# i would like to look through things.
# shots of my daliy fucking life.
# can make it into my fucking usb drive?
# select those with possible text.
# difference -> readable text