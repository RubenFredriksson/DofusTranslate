import controller as c
import pyautogui


def getPlusImage():
    screenSize = pyautogui.size()

    if screenSize == (1920, 1080):
        return "img/plus-1920-1080.png"
    elif screenSize == (1366, 768):
        return "img/plus-1366-768.png"
    elif screenSize == (1440, 900):
        return "img/plus-1440-900.png"
    elif screenSize == (1280, 720):
        return "img/plus-1280-720.png"
    elif screenSize == (1600, 900):
        return "img/plus-1600-900.png"
    else:
        return "img/plus-1920-1080.png"
    
    
def getEmoteImage():
    screenSize = pyautogui.size()

    if screenSize == (1920, 1080):
        return "img/emote-1920-1080.png"
    elif screenSize == (1366, 768):
        return "img/emote-1366-768.png"
    elif screenSize == (1440, 900):
        return "img/emote-1440-900.png"
    elif screenSize == (1280, 720):
        return "img/emote-1280-720.png"
    elif screenSize == (1600, 900):
        return "img/emote-1600-900.png"
    else:
        return "img/emote-1920-1080.png"