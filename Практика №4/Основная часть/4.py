import tkinter as tk

root = tk.Tk()
root.title('List box')
root.geometry('210x200')

list_box = tk.Listbox(root, selectmode=tk.MULTIPLE)
endings = ['st', 'nd', 'rd'] + ['th'] * 2
items = [f'{i + 1}{endings[i]} item' for i in range(5)]
list_box.insert(tk.END, *items)
list_box.pack()

root.mainloop()
