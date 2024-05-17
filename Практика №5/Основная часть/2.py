import tkinter as tk
from itertools import cycle

root = tk.Tk()
root.title("Calculator")

bg_colors = cycle([
    'lightgrey', 'lightblue', 'lightgreen',
    'lightyellow', 'lightpink', 'lightcyan'
])


def create_button(text: str, row: int, column: int):
    button = tk.Button(root, text=text, width=7, height=3, bg=next(bg_colors))
    button.grid(row=row, column=column)
    return button


entry = tk.Entry(root, font=('Arial', 14), bg=next(bg_colors))
entry.grid(row=0, column=0, columnspan=4, sticky='ew')

button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i, button_label in enumerate(button_labels):
    create_button(button_label, i // 4 + 1, i % 4)

root.mainloop()
