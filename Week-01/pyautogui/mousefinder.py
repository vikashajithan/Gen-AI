import pyautogui
import time

time.sleep(2)

x,y = pyautogui.position()

time.sleep(2)
print(f"x : {x}, y : {y}")