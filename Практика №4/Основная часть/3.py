import tkinter as tk


def change_label():
    label.config(text=radio_var.get())


root = tk.Tk()
root.title('Radio buttons')
root.geometry('300x100')

radio_var = tk.StringVar()
radio_var.set('First')

label = tk.Label(root, text=radio_var.get(), font=('Arial Bold', 14))
label.pack()

first_radio_button = tk.Radiobutton(
    root,
    text='First',
    variable=radio_var,
    value='First',
    command=change_label
)
first_radio_button.pack()

second_radio_button = tk.Radiobutton(
    root,
    text='Second',
    variable=radio_var,
    value='Second',
    command=change_label
)
second_radio_button.pack()

root.mainloop()
