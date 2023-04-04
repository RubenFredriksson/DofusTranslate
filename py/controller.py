import numpy
import cv2
import pyautogui
import pytesseract

def debug(value):

    debugLog = "\n\n"

    if type(value) != list:
        value = [value]

    for strings in value:
        debugLog += (str(strings) + "\n")

    debugFile = open("debug.txt", "w")
    debugFile.write(debugLog)
    debugFile.close()

    return "Success"


def imageDebug(image):

    cv2.imshow('FRAME',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return "Success"


def imageCapture(xPos, yPos, width, height):

    image = pyautogui.screenshot(region=(xPos, yPos, width, height))

    image = cv2.cvtColor(numpy.array(image),cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image


def imageToString(image):
    
    text = pytesseract.image_to_string(image).split("\n")
    
    clean = []

    for str in text:
        if (str != ""):
            clean.append(str)
    
    del clean[-1]

    return clean
