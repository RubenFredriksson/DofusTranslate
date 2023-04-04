import controller as c
import pyautogui
import re

from deep_translator import GoogleTranslator

def getChatboxPositions():

    try:
        plusLocation = list(pyautogui.locateOnScreen("plus.png", confidence=0.9))
        emoteLocation = list(pyautogui.locateOnScreen("emote.png", confidence=0.9))
    except:
        return 0, 0, 0, 0

    startXPos = plusLocation[0]
    startYPos = plusLocation[1] + plusLocation[3]

    endXPos = emoteLocation[0] - startXPos
    endYPos = emoteLocation[1] - startYPos

    return startXPos, startYPos, endXPos, endYPos


def translate(text, fromLanguage, toLanguage):
    if text[1] == "]":
        text = text[3:]

    pattern = r'\[[^]]*\]'
    text = [re.sub(pattern, "", str) for str in text]
    text = [GoogleTranslator(source=fromLanguage, target=toLanguage).translate(str) for str in text]

    return text