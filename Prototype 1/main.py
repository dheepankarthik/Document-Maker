import tkinter as tk
from tkinter import messagebox

# Defining the window

root = tk.Tk()
root.geometry("320x180")

# Required functionalities for overall program
counter = 0
maxCounter = 20

def addCounter():
    global counter, maxCounter
    counter = counter + 1
    if counter == maxCounter:
        messagebox.showinfo("Counter Status", "Counter limit reached")

textInputs = []

textInputsNumber = 0

def textBoxPopup():
    global textInputsNumber
    popup = tk.Toplevel(root)
    popup.geometry("800x450")
    popup.title("Text input box")

    frame = tk.Frame(popup)
    frame.pack(padx=50, pady=50)

    text = tk.Text(frame, width=50, height=5, wrap="word")
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    popupScrollBar = tk.Scrollbar(frame, command=text.yview)
    popupScrollBar.pack(side=tk.RIGHT, fill=tk.Y)

    text.config(yscrollcommand=popupScrollBar.set)

    def auto_resize(event=None):
        txt = text.get("1.0", "end-1c")
        lines = txt.count("\n") + 1
        text.config(height=lines)

    text.bind("<KeyRelease>", auto_resize)

    # Submit button
    def submit():
        global textInputsNumber
        textInputs.append(text.get("1.0", "end-1c"))
        textInputsNumber += 1      # ← moved here
        addCounter()
        popup.destroy()

    tk.Button(popup, text="Submit", command=submit).pack(pady=10)

    textInputsNumber += 1

def textInputPrint():
    global textInputs, textInputsNumber
    for i in range(len(textInputs)):
        print(f'Text number {i} - {textInputs[i]}')


def outputToFrame():
    global textInputs

    for widget in outputFrameContents.winfo_children():
            widget.destroy()


    for i in range(len(textInputs)):
        if textInputs[i] == "":
            tk.Label(outputFrameContents, text="No input").pack()
        else:
            tk.Label(outputFrameContents, text=textInputs[i]).pack()
        
        

# Elements present in window

tk.Label(root, text="Hello").pack()




textBoxInsert = tk.Button(root, text="Enter text box", command=textBoxPopup)
textBoxInsert.pack()

textPrint = tk.Button(root, text="Print text", command=textInputPrint)
textPrint.pack()

outputButton = tk.Button(root, text="Output", command=outputToFrame)
outputButton.pack()


# Output frame

outputFrame = tk.Frame(root)
outputFrame.pack(pady=50)

outputFrameTitleFrame = tk.Frame(outputFrame)

outputFrameTitle = tk.Label(outputFrameTitleFrame, text="Output:")
outputFrameTitle.pack()

outputFrameContents = tk.Frame(outputFrame)
outputFrameContents.pack()

#Running the program

root.mainloop()
