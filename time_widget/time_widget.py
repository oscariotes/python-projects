from tkinter import *
from tkinter.ttk import *
import pytz
from datetime import datetime

root = Tk()
root.title('Clock')

manila_timezone = pytz.timezone('Asia/Manila')
pacific_timezone = pytz.timezone('US/Pacific')

def get_formatted_time(timezone):
    return datetime.now(timezone).strftime('%I:%M:%S %p')

def update_time():
    manila_time_str = get_formatted_time(manila_timezone)
    pacific_time_str = get_formatted_time(pacific_timezone)
    formatted_string = f"Manila {manila_time_str}\nPacific {pacific_time_str}"
    lbl.config(text=formatted_string)
    lbl.after(1000, update_time)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='green',
            foreground='white')

lbl.pack(anchor='center')
update_time()

mainloop()