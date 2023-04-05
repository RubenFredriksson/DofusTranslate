import tkinter as tk
import controller as c
import chatbox
import time

def main():

    def onTranslateClick():
        # Clear the output text box
        outputText.delete("1.0", tk.END)

        # Get the coordinates of the Dofus Chatbox
        startXPos, startYPos, endXPos, endYPos = chatbox.getChatboxPositions()

        if startXPos == 0 and startYPos == 0 and endXPos == 0 and endYPos == 0:
            outputText.insert("1.0", "Could not find the chatbox.")
            return
        
        # Take a screenshot of the chatbox
        image = c.imageCapture(startXPos, startYPos, endXPos, endYPos)

        # Using OCR, extract the text from the image
        dofusChat = c.imageToString(image)

        # Translate the text from Spanish to English
        englishDofusChat = chatbox.translate(dofusChat, "es", "en")
        
        # Push the text to the output text box
        for i, line in enumerate(englishDofusChat):
            if line != "" and line != None:
                lineNumber = str(i) + ".0"
                outputText.insert(lineNumber, line + "\n")

    # Instantiate the GUI
    root = tk.Tk()
    root.title("Dofus Chatbox Translate")

    # Create a Font object which will be used on the Translate button
    verdanaFont = ('Verdana', 16)

    # Create the Translate button
    translateButton = tk.Button(root, text="Translate", height=2, width=20, font=verdanaFont, command=onTranslateClick)
    translateButton.pack()

    # Create the output text box
    outputText = tk.Text(root, height=40, width=100)
    outputText.pack()

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
