import pyautogui as pag
from pynput.mouse import Listener
from pynput import mouse
import time
import sys

sequenceList = []
global loops
loops = 1
screenX, screenY = pag.size()
box1ready = True
box2ready = True
box3ready = True
box4ready = True
box5ready = True
box6ready = True
box7ready = True
box8ready = True
box9ready = True


def printCoords():
    mouseX, mouseY = pag.position()
    print(f"{mouseX}, {mouseY}")

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.right:
        listener.stop()
        quit()
        
with Listener(on_click=on_click) as listener:
    listener.join()

time.sleep(5)
pag.click(1716, 539)
time.sleep(0.2)
while True:
    sequenceList = [0]
    pag.moveTo(screenX / 2, screenY / 2)

    while loops > len(sequenceList) - 1:
        time.sleep(0.1)



        # top left box
        r, g, b = pag.pixel(1580, 300)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 1:
            sequenceList.append(1)
            print(sequenceList)
            continue
        # top middle box
        r, g, b = pag.pixel(1710, 300)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 2:
            sequenceList.append(2)
            print(sequenceList)
            
            continue
        # top right box
        r, g, b = pag.pixel(1844, 300)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 3:
            sequenceList.append(3)
            print(sequenceList)
            
            continue
        # middle left box
        r, g, b = pag.pixel(1580, 440)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 4:
            sequenceList.append(4)
            print(sequenceList)
            
            continue
        # middle middle box
        r, g, b = pag.pixel(1710, 440)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 5:
            sequenceList.append(5)
            print(sequenceList)
            
            continue
        # middle right box
        r, g, b = pag.pixel(1844, 440)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 6:
            sequenceList.append(6)
            print(sequenceList)
            
            continue
        # bottom left box
        r, g, b = pag.pixel(1580, 570)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 7:
            sequenceList.append(7)
            print(sequenceList)
            
            continue
        # bottom middle box
        r, g, b = pag.pixel(1710, 570)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 8:
            sequenceList.append(8)
            print(sequenceList)
            
            continue
        # bottom right box
        r, g, b = pag.pixel(1844, 570)
        if r != 37 and g != 115 and b != 193 and sequenceList[-1] != 9:
            sequenceList.append(9)
            print(sequenceList)
            
            continue

    time.sleep(2)

    for i in sequenceList:
        time.sleep(0.02)
        if i == 1:
            pag.click(1580, 300)
            continue
        if i == 2:
            pag.click(1710, 300)
            continue
        if i == 3:
            pag.click(1844, 300)
            continue
        if i == 4:
            pag.click(1580, 440)
            continue
        if i == 5:
            pag.click(1710, 440)
            continue
        if i == 6:
            pag.click(1844, 440)
            continue
        if i == 7:
            pag.click(1580, 570)
            continue
        if i == 8:
            pag.click(1710, 570)
            continue
        if i == 9:
            pag.click(1844, 570)
            continue

    pag.moveTo(screenX / 2, screenY / 2)
    time.sleep(1)
    loops += 1