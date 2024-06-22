import pyautogui as auto
import time


screenX, screenY = auto.size()

auto.moveTo(screenX / 2, 300)
while True:
    r, g, b = auto.pixel(425, 300)
    print(f"R: {r} G: {g} B: {b}")
    if r == 75 and g == 219 and b == 106:
        auto.click(screenX / 2, 300)



# time.sleep(5)
# mouseX, mouseY = pyautogui.position()
# print(f"{mouseX}, {mouseY}")