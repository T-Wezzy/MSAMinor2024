import pyautogui
import math
import time



screenX, screenY = pyautogui.size()

mouseX, mouseY = pyautogui.position()


def drawCircle(radius):
    pyautogui.mouseUp()
    pyautogui.moveTo(screenX / 2 + radius, (screenY / 2))
    pyautogui.mouseDown()
    for i in range(31):
        radians = i * 12 * (math.pi / 180)
        pyautogui.moveTo((screenX / 2) + radius * math.cos(radians), (screenY / 2) + radius * math.sin(radians))
    pyautogui.mouseUp()

time.sleep(5)
drawCircle(500)