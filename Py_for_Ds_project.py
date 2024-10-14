import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
import requests

# Main window

root = tk.Tk()
root.title("Calculator Application")
root.geometry("400x600")

# Define color scheme
btn_bg = "#4CAF50"  # Button background
btn_fg = "#ffffff"  # Button text color
entry_bg = "#ffffff"  # Entry background
entry_fg = "#000000"  # Entry text color

# ========== Basic Calculator Functionality ==========
def clear_display():
    display.set("")

def evaluate_expression():
    try:
        expression = display.get()
        result = eval(expression)
        display.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input!")

def append_to_expression(value):
    # Get current expression
    current_expr = display.get()
    # Prevent adding multiple consecutive operators
    if current_expr and current_expr[-1] in '+-*/' and value in '+-*/':
        return
    # Prevent starting with an operator
    if not current_expr and value in '+-*/':
        return
    display.set(current_expr + value)

# Display setup
display = tk.StringVar()
calc_entry = tk.Entry(root, textvariable=display, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4, bg=entry_bg, fg=entry_fg)
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ========== Calculator Buttons ==========
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row_val, col_val = 1, 0
for button in buttons:
    if button == '=':
        action = evaluate_expression
    else:
        action = lambda x=button: append_to_expression(x)
    
    ttk.Button(root, text=button, command=action, width=10).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear (AC) button
ttk.Button(root, text='AC', command=clear_display, width=10, style='W.TButton').grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# ========== Additional Styling ==========
style = ttk.Style()
style.configure('W.TButton', font=('Arial', 18), background=btn_bg, foreground=btn_fg)

# Launch the app
root.mainloop()
