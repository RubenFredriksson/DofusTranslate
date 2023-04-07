import tkinter as tk
from tkinter import messagebox

import controller as c
import chatbox
import time

def main():

    def onTranslateClick(fromLanguage, toLanguage):

        # Change the language to ISO 2 Letter Code
        fromLanguage = c.languageToISO(fromLanguage)
        toLanguage = c.languageToISO(toLanguage)

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

        # Translate the text
        outputChat = chatbox.translate(dofusChat, fromLanguage, toLanguage)
        
        # Push the text to the output text box
        for i, line in enumerate(outputChat):
            if line != "" and line != None:
                lineNumber = str(i + 1) + ".0"
                outputText.insert(lineNumber, line + "\n")

    def onExportClick():
        # Get confirmation that user wishes to export the chatbox
        response = messagebox.askyesno("Warning", "Are you sure you want to export the chatbox?")
        if response != 1:
            return

        # Export the chatbox
        text = outputText.get("1.0", tk.END)

        with open("output.txt", "w") as f:
            f.write(text)

    # Instantiate the GUI
    root = tk.Tk()
    root.title("Dofus Chatbox Translate")

    # Create a Font object which will be used on the Translate button
    verdanaFont = ('Verdana', 16)

    # Create the Translate button
    translateButton = tk.Button(root, text="Translate", height=2, width=20, font=verdanaFont, command=lambda: onTranslateClick(fromLanguage.get(), toLanguage.get()))
    translateButton.pack()

    # Create the output text box
    outputText = tk.Text(root, height=30, width=100)
    outputText.pack()

    # Create a label for the language dropdown menu
    label = tk.Label(root, text="Translate From:")
    label.pack(padx=10, side=tk.LEFT)

    # Establish Language Options
    languageOptions = ["Spanish", "French", "English"]

    # Create the language dropdown menu
    fromLanguage = tk.StringVar(root)
    fromLanguage.set(languageOptions[0]) # Default = Spanish
    fromLanguageOptionMenu = tk.OptionMenu(root, fromLanguage, *languageOptions)
    fromLanguageOptionMenu.pack(padx=10, side=tk.LEFT)

    label = tk.Label(root, text="To:")
    label.pack(padx=10, side=tk.LEFT)

    # Create the language dropdown menu
    toLanguage = tk.StringVar(root)
    toLanguage.set(languageOptions[2]) # Default = English
    toLanguageOptionMenu = tk.OptionMenu(root, toLanguage, *languageOptions)
    toLanguageOptionMenu.pack(padx=10, side=tk.LEFT)

    # Create the Export button
    exportButton = tk.Button(root, text="Export", height=2, width=20, command=onExportClick, padx=-100, pady=-100)
    exportButton.pack(padx=20, pady=20, anchor=tk.N, side=tk.RIGHT)

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
