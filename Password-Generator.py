from tkinter import *
from tkinter import ttk, messagebox
import string
import random


def showValue(value):
    int_val = int(float(value))
    sliderValueLabel.config(text=str(int_val))  # Update the slider value label

def generatePassword():
    passLength = int(float(passLengthSlider.get())) # Use the value of the passLength slider

    allowedCharacters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+-;:>?/,.")
    
    password = ""
    
    while len(password) < passLength:
        password += random.choice(allowedCharacters)

    return password
 

def showPasswordOnClick():
    global password
    password = generatePassword()
    passwordText.configure(state="normal")
    passwordText.delete("1.0", END)
    passwordText.insert("1.0", password)
    passwordText.configure(state="disabled")
    copyPassBtn.config(state="normal")


def copyPass():
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied!", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Oops!", "No password to copy. Generate one first!")

# --- GUI SETUP ---
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

# Set window size, title
root.title("Password Generator")
root.geometry("450x200")
root.resizable(False, False)

# Label prompting the user to choose pass length
ttk.Label(frame, text="Choose Password Length").grid(column=0, row=0, sticky="W")
passLengthSlider = ttk.Scale(frame, from_=8, to=32, orient=HORIZONTAL, command=showValue)
passLengthSlider.grid(column=1, row=0, sticky="EW", padx=5)
passLengthSlider.set(12)

# Slider value label
sliderValueLabel = ttk.Label(frame, text="12")
sliderValueLabel.grid(column=2, row=0, sticky="W")

# Generate button
generatePasswordBtn = ttk.Button(frame, text="Generate Password", command=showPasswordOnClick)
generatePasswordBtn.grid(column=0, row=1, pady=(10, 0))

# Copy button
copyPassBtn = ttk.Button(frame, text="Copy Password", command=copyPass)
copyPassBtn.config(state="disabled")
copyPassBtn.grid(column=1, row=1, pady=(10, 0))

# Password display (Text widget)
passwordText = Text(frame, height=1, width=40, font=("Consolas", 12))
passwordText.grid(column=0, row=2, columnspan=3, pady=(15, 0))
passwordText.configure(state="disabled")  # Make it read-only

root.mainloop()

