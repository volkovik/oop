import tkinter as tk
from tkinter import messagebox


def change_label():
    if not value.get():
        messagebox.showerror('Error', 'Please enter a value')
        return

    label.config(text=value.get())


root = tk.Tk()
root.title('Label changer')
root.geometry('300x150')

label = tk.Label(root, text='_', font=('Arial Bold', 14))
label.pack(pady=10, padx=10, fill='x')

value = tk.StringVar()
entry = tk.Entry(root, textvariable=value)
entry.pack(pady=10, padx=10, fill='x')

button = tk.Button(root, text='Change label', command=change_label)
button.pack(pady=10, padx=10, fill='x')

root.mainloop()
