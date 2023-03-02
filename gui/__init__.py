import json
from tkinter import *
from tkinter import ttk
# from tkinter
# import filedialog
import config


# Start the basics of initializing the GUI frame.

root = Tk()
root.title("Earth v.0.0.3")
root.geometry("1200x600")
start_up = ttk.Frame(root)
start_up.grid()

config.create_config_files()  # create any missing config files

with open(config.get_config_files()['config.json'], 'r') as start_up:
    config_data = json.load(start_up)  # open config.json and load JSON data into python dict
    if config_data['initial']:
        # Ask user if this will be standalone/local or connect to server.
        # If standalone/local, ask user if it will be multi-user. If server, server will handle users.
        # Ask user what services they'd like to register
        # Ask user what locations they'd like to register.

        pass
    else:
        if config_data['standalone']:  # GUI is standalone, not communicating with server
            pass
        else:
            pass





root.update()
root.mainloop()


