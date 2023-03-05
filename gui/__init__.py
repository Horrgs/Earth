import json
import tkinter as tk
# from tkinter import ttk
# from tkinter
# import filedialog
import config


class Main:

    def __init__(self, root):

        root.title("Main v0.0.3")

        # Calculate the resolution of the GUI by the screen resolution.
        window_width = root.winfo_screenwidth() * .60
        window_height = root.winfo_screenheight() * .50

        #root.geometry(f'{window_width}x{window_height}')  # set GUI resolution.

        if config.is_initial_run():
            Setup(root)
        else:
            if config_data['standalone']:  # GUI is standalone, not communicating with server
                pass
            else:
                pass


class Setup:

    def __init__(self, root):
        self.setup_frame = tk.Frame(root)
        title = tk.Label(self.setup_frame, text="Earth")  # create Label to represent as the title.

        title.grid(column=0, row=0, columnspan=2, sticky='WE')

        message = tk.Label(self.setup_frame, text="Insert welcome message")  # create Label w/ welcome msg and explanation.
        message.grid(column=0, row=1, columnspan=2)

        # self.setup_frame.bind('<ENTER>')

    def show_step_one(self):
        # create buttons for selecting standalone/local use or for connecting to another server.

        username_label = tk.Label(self.setup_frame, text="Enter a Username: ")
        username_label.grid(column=0, row=2)

        username = tk.StringVar()
        username_field = tk.Entry(self.setup_frame, textvariable=username)
        username_field.grid(column=1, row=2)

        def submit():
            # check if username entry is valid
            pass

        continue_button = tk.Button(self.setup_frame, text='Continue', command=submit)
        continue_button.grid(column=0, row=3, columnspan=2)
        self.setup_frame.grid()

    def show_step_two(self):
        self.setup_frame.destroy()

        title = tk.Label(self.setup_frame, text="Earth")
        title.grid(column=0, row=0, columnspan=2)

        message = tk.Label(self.setup_frame, text="Will you be using this locally or connecting to a server?")
        message.grid(column=0, row=1, columnspan=2)

        standalone = tk.Button(self.setup_frame, text="Local")
        standalone.grid(column=0, row=2)

        server = tk.Button(self.setup_frame, text="Server")
        server.grid(column=1, row=2)

        self.setup_frame.grid()

    def show_step_four(self):
        pass

        # If standalone/local, ask user if it will be multi-user. If server, server will handle users.
        # Ask user what services they'd like to register
        # Ask user what locations they'd like to register.

    def setup_locations(self):
        pass

# Start the basics of initializing the GUI frame.


config.create_config_files()  # create any missing config files
root = tk.Tk()
m = Main(root)

with open(config.get_config_files()['settings.json'], 'r') as start_up:
    config_data = json.load(start_up)  # open settings.json and load JSON data into python dict
start_up.close()

root.update()
root.mainloop()


