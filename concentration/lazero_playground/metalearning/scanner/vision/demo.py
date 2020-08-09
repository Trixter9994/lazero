import pyautogui
import time
time.sleep(1)
pyautogui.screenshot("buf0.png")
time.sleep(1)
pyautogui.click(button="right")
pyautogui.screenshot("buf1.png")
# with timestamp.