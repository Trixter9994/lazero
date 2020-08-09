import random
import pyautogui
import time

# random shits. range: (0,1)
# better if I have a quantum computer.
buff=pyautogui.size()
def moveOn(a,b):
    pyautogui.moveTo(a,b,1)
    time.sleep(1)
def generator():
    return [int(random.random()*a) for a in buff]
def main(a):
    for x in range(a):
        moveOn(*generator())
