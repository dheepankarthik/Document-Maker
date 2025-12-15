import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from tkinterdnd2 import TkinterDnD # Drag and drop

root = tk.Tk()
root.geometry("1600x900")

#Frames & Title

titleLabel = tk.Label(root, text="Welcome to the Document Maker", font=("Times New Roman", 30), anchor="center", bd=3, relief="solid")
titleLabel.grid(row=0, column=0, sticky="nsew", ipady=20, ipadx=15)

buttonsFrame = tk.Frame(root, width=750)
buttonsFrame.grid(row=1, column=0)

## Output Frame 

outputFrame = tk.Frame(root)
outputFrame.grid(row=2, column=0, sticky="nsew")

canvas = tk.Canvas(outputFrame, width=900, height=500)
scrollbar = tk.Scrollbar(outputFrame, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

outputFrame = tk.Frame(canvas)
canvas.create_window((0, 0), window=outputFrame, anchor="nw")

outputFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

## End of Output Frame


# Functions

outputComponents = 0

def insertTextBox():
    global outputFrame, outputComponents
    textBoxToAppend = tk.Text(outputFrame, width=30)
    textBoxToAppend.grid(row=outputComponents, column=0)
    outputComponents = outputComponents + 1



# Buttons Frame

textBoxButton = tk.Button(buttonsFrame, text="Insert a text box", command=insertTextBox)
textBoxButton.grid(row=0, column=0)


#Running the app
root.mainloop()