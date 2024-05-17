import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Checkbox')
root.geometry('300x70')


def check():
    if is_checked.get():
        messagebox.showinfo('Info', 'Checkbox is checked!')
    else:
        messagebox.showinfo('Info', 'Checkbox is not checked!')


is_checked = tk.IntVar()

checkbox = tk.Checkbutton(
    root, width=10, height=20,
    font=('Arial', 18), text='Check me!',
    variable=is_checked, command=check
)
checkbox.pack()

root.mainloop()
