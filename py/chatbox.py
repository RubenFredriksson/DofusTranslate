import controller as c
import pyautogui
import re

from deep_translator import GoogleTranslator

def getChatboxPositions():

    try:
        plusLocation = list(pyautogui.locateOnScreen("plus.png", confidence=0.85))
        emoteLocation = list(pyautogui.locateOnScreen("emote.png", confidence=0.85))
    except:
        return 0, 0, 0, 0

    startXPos = plusLocation[0]
    startYPos = plusLocation[1] + plusLocation[3]

    endXPos = emoteLocation[0] - startXPos
    endYPos = emoteLocation[1] - startYPos

    return startXPos, startYPos, endXPos, endYPos


def translate(text, fromLanguage, toLanguage):
    # Strip the timestamps from the text
    if ']' in text:
        text = text.split(']', 1)[1]

    pattern = r'\[\d{2}:\d{2}\]'
    text = [re.sub(pattern, "", str) for str in text]

    # Translate the text
    text = [GoogleTranslator(source=fromLanguage, target=toLanguage).translate(str) for str in text]

    return text