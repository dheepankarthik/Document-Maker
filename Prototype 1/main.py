import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("320x180")

counter = 0
maxCounter = 20

def addCounter():
    global counter, maxCounter
    global counterLabel
    counter = counter + 1
    counterLabel.config(text=str(counter))

    if counter == maxCounter:
        messagebox.showinfo("Counter limit", "You have reached the counter limit.")



counterLabel = tk.Label(root, text=str(counter), font=("Arial", 12))
counterLabel.pack()

counterButton = tk.Button(root, text="Add counter", command=addCounter)
counterButton.pack()

root.mainloop()
