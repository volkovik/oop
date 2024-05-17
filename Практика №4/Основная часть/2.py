import tkinter as tk


def change_label():
    label.config(text=str(is_checked.get()))


root = tk.Tk()
root.title('Checkbox')
root.geometry('300x70')

label = tk.Label(root, text='0', font=('Arial Bold', 14))
label.pack()

is_checked = tk.IntVar()
checkbox = tk.Checkbutton(
    root,
    text='Check me!',
    command=change_label,
    variable=is_checked
)
checkbox.pack()

root.mainloop()
