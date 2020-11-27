#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import pytz
from tzlocal import get_localzone
from datetime import datetime

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #--------------------------------------------
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.style = ttk.Style(self)

        self.init_UI()

    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.main_frame, text='Select Country')
        self.fieldset.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.local_timezone = tk.StringVar()
        countries = list(pytz.all_timezones)
        country_drop_down = ttk.OptionMenu(self.fieldset, self.local_timezone, *countries)
        self.local_timezone.set(get_localzone())
        country_drop_down.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        go_btn = ttk.Button(self.fieldset, text='Go', command=self.display_datetime)
        go_btn.grid(row=0, column=2, sticky=tk.W, padx=(0, 5), pady=5)

    def display_datetime(self):
        timezone = pytz.timezone(self.local_timezone.get())
        current_country_time = datetime.now(timezone)

        prompt = f'The date of {timezone} is {current_country_time.strftime(r"%d-%m-%y")}\n'
        prompt += f'The time of {timezone} is {current_country_time.strftime(r"%H:%M:%S")}'
        response = mb.showinfo('Info', prompt)

#===========================
# Start GUI
#===========================

def main():
    world_clock = App()
    world_clock.title('World Clock Version 1.0')
    world_clock.style.theme_use('clam')
    world_clock.mainloop()

if __name__ == '__main__':
    main()
