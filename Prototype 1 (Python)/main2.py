import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from tkinterdnd2 import TkinterDnD # Drag and drop

root = tk.Tk()
root.geometry("1600x900")

#Frames & Title

titleLabel = tk.Label(root, text="Welcome to the Document Maker", font=("Times New Roman", 30), anchor="center", bd=3, relief="solid")
titleLabel.grid(row=0, column=0, sticky="nsew", ipady=20, ipadx=15)

buttonsFrame = tk.Frame(root, width=750)
buttonsFrame.grid(row=1, column=0, pady=50)

outputFrame = tk.Frame(root, width=900)
outputFrame.grid(row=1, column=0)

# Functions

def inputDialog():
    popup = tk.Toplevel(buttonsFrame)
    popup.geometry("800x450")
    popup.title("Input")

# Buttons Frame

inputDialogButton = tk.Button(buttonsFrame, text="Input", command=inputDialog, font=("Arial", 16))
inputDialogButton.grid(row=0, column=0)


#Running the app
root.mainloop()