import controller as c
import screenResolution as sr
import pyautogui
import re

from deep_translator import GoogleTranslator

def getChatboxPositions():

    try:
        plusLocation = list(pyautogui.locateOnScreen(sr.getPlusImage(), confidence=0.85))
        emoteLocation = list(pyautogui.locateOnScreen(sr.getEmoteImage(), confidence=0.85))
    except:
        return 0, 0, 0, 0

    startXPos = plusLocation[0]
    startYPos = plusLocation[1] + plusLocation[3]

    endXPos = emoteLocation[0] - startXPos
    endYPos = emoteLocation[1] - startYPos

    return startXPos, startYPos, endXPos, endYPos


def getPlusPosition():
    try:
        plusLocation = list(pyautogui.locateOnScreen(sr.getPlusImage(), confidence=0.85))
    except:
        return 0
    
    return plusLocation[0], plusLocation[1]


def getEmotePosition():
    try:
        emoteLocation = list(pyautogui.locateOnScreen(sr.getEmoteImage(), confidence=0.85))
    except:
        return 0
    
    return emoteLocation[0], emoteLocation[1]


def translate(text, fromLanguage, toLanguage, mode):
    
    if mode == "Read":
        # Strip the timestamps from the text
        if ']' in text:
            text = text.split(']', 1)[1]

        pattern = r'\[\d{2}:\d{2}\]'
        text = [re.sub(pattern, "", str) for str in text]
        
        abbreviationMap = {
            "es": {
                "csm": "concha su madre",
                "ctm": "concha tu madre",
                " mp ": " mensaje privado ",
                "xq": "por qué",
                "pq": "por qué"
            },
            "fr": {
                "fdp": "fils de pute",
                "mdr": "mort de rire",
                "ptdr": "pété de rire",
                " mp ": " message privé "
            },
            "en": {
                "lmao": "laughing my ass off",
                "lmfao": "laughing my fucking ass off",
                "smh": "shaking my head",
                "brb": "be right back",
                "afk": "away from keyboard",
                " pm ": " private message ",
                "fml": "fuck my life",
                "wtf": "what the fuck"
            }
        }

        if fromLanguage in abbreviationMap:
            for abbr, replacement in abbreviationMap[fromLanguage].items():
                text = [str.replace(abbr, replacement) for str in text]

        # Translate the text
        text = [GoogleTranslator(source=fromLanguage, target=toLanguage).translate(str) for str in text]

    elif mode == "Write":
        text = GoogleTranslator(source=fromLanguage, target=toLanguage).translate(text)

    return text