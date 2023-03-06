import json
import re
import tkinter as tk
import config
# from tkinter import ttk
# from tkinter
# import filedialog
# from backend.user.user import User
# from backend.user.locations import Location
# from backend.user.services import Service


class Main:  # Main class that will handle the GUI interface and serve as the root.

    def __init__(self, root):

        root.title("Earth v0.0.3")  # set Title

        # Calculate the resolution of the GUI by the screen resolution.
        window_width = int(root.winfo_screenwidth() * .60)
        window_height = int(root.winfo_screenheight() * .50)

        root.geometry(f'{window_width}x{window_height}')  # set GUI resolution.

        if config.is_initial_run():  # check if its the first run, if so go to Setup process.
            Setup(root)
        else:
            Home(root)


class Setup:

    def __init__(self, root):

        # create variables that will be set in the setup process
        self.display_name = None
        self.locations = None
        self.services = None
        self.connection = None
        self.current_step = 0

        # GUI
        self.setup_frame = tk.Frame(root)  # create frame that will hold all the widgets.
        title = tk.Label(self.setup_frame, text="Earth")  # create Label to represent as the title.

        title.grid(column=0, row=0, columnspan=2)  # position title

        message = tk.Label(self.setup_frame, text="Insert welcome message")  # create Label w/ welcome msg and explanation.
        message.grid(column=0, row=1, columnspan=2)  # position welcome message

        next_step = tk.Button(self.setup_frame, text="Continue", command=self.show_step_one)  # remove later for .bind()
        next_step.grid(column=0, row=2, columnspan=2)  # position next step button
        # self.setup_frame.bind('<ENTER>')

        # make sure the widgets resize as the frame resizes. Effective as this happens at the root.
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.setup_frame.grid()

    def show_step_one(self):
        self.current_step = 1
        for widget in self.setup_frame.winfo_children():
            widget.destroy()

        title = tk.Label(self.setup_frame, text="Earth")
        title.grid(column=0, row=0, columnspan=2)

        message = tk.Label(self.setup_frame, text="Are you a new or existing user?")
        message.grid(column=0, row=1, columnspan=2)

        new_user = tk.Button(self.setup_frame, text="New User", command=self.show_step_two)
        new_user.grid(column=0, row=2)

        existing_user = tk.Button(self.setup_frame, text="Existing User")
        existing_user.grid(column=1, row=2)

    def new_step_one_b(self):  # for existing users
        for widget in self.setup_frame.winfo_children():
            widget.destroy()

        title = tk.Label(self.setup_frame, text="Earth")
        pass

    def show_step_two(self):
        self.current_step = 2

        # create buttons for selecting standalone/local use or for connecting to another server.
        for widget in self.setup_frame.winfo_children():
            widget.destroy()

        username_label = tk.Label(self.setup_frame, text="Enter a Username: ")
        username_label.grid(column=0, row=2)

        username = tk.StringVar()
        username_field = tk.Entry(self.setup_frame, textvariable=username)
        username_field.grid(column=1, row=2)

        def submit():

            if re.match("^[a-zA-Z]+$", username.get()):
                self.display_name = username
                print(type(username_field.grid_info()['row']))
                self.show_step_three()
            else:
                Error("Error", "Invalid username. It cannot contain any spaces and must only be alphabetic letters.")

            pass

        continue_button = tk.Button(self.setup_frame, text='Continue', command=submit)
        continue_button.grid(column=0, row=3, columnspan=2)
        self.setup_frame.grid()

    def show_step_three(self):
        for widget in self.setup_frame.winfo_children():
            widget.destroy()

        title = tk.Label(self.setup_frame, text="Earth")
        title.grid(column=0, row=0, columnspan=2)

        message = tk.Label(self.setup_frame, text="Will you be using this locally or connecting to a server?")
        message.grid(column=0, row=1, columnspan=2)

        def local_():
            self.connection = "LOCAL"
            self.show_step_four()

        standalone = tk.Button(self.setup_frame, text="Local", command=local_)
        standalone.grid(column=0, row=2)

        server = tk.Button(self.setup_frame, text="Server")
        server.grid(column=1, row=2)

        self.setup_frame.grid()

    def show_step_four(self):
        pass

        # Ask user what services they'd like to register

    def show_step_five(self):
        # Ask user what locations they'd like to register.
        pass

    def next_step(self, var):
        def destroy_widgets():
            for widget in self.setup_frame.winfo_children():
                if widget.grid_info()['row'] == 0:
                    continue
                widget.destroy()
                
        if self.current_step == 1:
            if self.connection == "NEW":
                destroy_widgets()
            elif self.connection == "EXISTING":
                pass
        elif self.connection == 2:  # Local or Remote
            if re.match("^[a-zA-Z]+$", var.get()):
                self.display_name = var.get()
                destroy_widgets()
                self.show_step_three()
            else:
                Error("Error", "Invalid username. It cannot contain any spaces and must only be alphabetic letters.")

            pass
        elif self.connection == 3:  # Local or Remote


class Home:

    def __init__(self, root):
        pass


class Error:

    def __init__(self, title, message):
        foo = tk.Tk()
        foo.title(title)

        error_frame = tk.Frame(foo)

        error_msg = tk.Label(error_frame, text=message)
        error_msg.grid(column=0, row=0)
        error_frame.grid()

        foo.mainloop()

# Start the basics of initializing the GUI frame.


config.create_config_files()  # create any missing config files
root = tk.Tk()
m = Main(root)

with open(config.get_config_files()['settings.json'], 'r') as start_up:
    config_data = json.load(start_up)  # open settings.json and load JSON data into python dict
start_up.close()

root.update()
root.mainloop()





