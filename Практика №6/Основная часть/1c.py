import tkinter as tk

root = tk.Tk()
root.title('Listbox')


def button_click():
    listbox.insert('end', entry.get())
    entry.delete(0, 'end')


listbox = tk.Listbox(root, width=50, selectmode=tk.MULTIPLE)
listbox.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

button = tk.Button(root, text='Add item', command=button_click)
button.pack(padx=10, pady=5)

root.mainloop()
