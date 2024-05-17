from itertools import cycle

import tkinter as tk
from typing import Literal

root = tk.Tk()
root.title('Contact Details')


frame_colors = cycle([
    'lightgrey', 'lightblue', 'lightgreen',
    'lightyellow', 'lightpink', 'lightcyan'
])


def create_label(
        text: str,
        master: tk.Misc = root,
        side: Literal['left', 'right', 'top', 'bottom'] = 'top'
):
    label = tk.Label(master, text=text)
    label.pack(side=side, anchor='w', padx=5, pady=5)
    return label


def create_entry(
        master: tk.Misc = root,
        side: Literal['left', 'right', 'top', 'bottom'] = 'top'
):
    entry = tk.Entry(master)
    entry.pack(side=side, fill='x', padx=5, pady=5)
    return entry


def create_frame(
        master: tk.Misc = root,
        side: Literal['left', 'right', 'top', 'bottom'] = 'top'
):
    frame = tk.Frame(master, bg=next(frame_colors))
    frame.pack(side=side, fill='x', expand=True)
    return frame


# Первая строка
name_frame = create_frame()
name_label = create_label('Name:', name_frame)
name_entry = create_entry(name_frame)

# Вторая строка
email_phone_frame = create_frame()

email_frame = create_frame(email_phone_frame, side='left')
email_label = create_label('Email:', email_frame)
email_entry = create_entry(email_frame)

phone_frame = create_frame(email_phone_frame, side='left')
phone_label = create_label('Phone:', phone_frame)
phone_entry = create_entry(phone_frame)

# Третья строка
address_frame = create_frame()
address_label = create_label('Address:', address_frame)
address_entry = create_entry(address_frame)

# Четвертая строка
city_state_zip_frame = create_frame()

city_frame = create_frame(city_state_zip_frame, side='left')
city_label = create_label('City:', city_frame)
city_entry = create_entry(city_frame)

state_frame = create_frame(city_state_zip_frame, side='left')
state_label = create_label('State:', state_frame)
state_entry = create_entry(state_frame)

zip_frame = create_frame(city_state_zip_frame, side='left')
zip_label = create_label('Zip:', zip_frame)
zip_entry = create_entry(zip_frame)

button_frame = create_frame()
button = tk.Button(button_frame, text='Submit')
button.pack(side='top', padx=5, pady=5)


root.mainloop()
