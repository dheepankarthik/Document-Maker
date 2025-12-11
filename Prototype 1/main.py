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


# Elements present in window

tk.Label(root, text="Hello").pack()




textBoxInsert = tk.Button(root, text="Enter text box", command=textBoxPopup)
textBoxInsert.pack()

textPrint = tk.Button(root, text="Print text", command=textInputPrint)
textPrint.pack()

#Running the program

root.mainloop()
