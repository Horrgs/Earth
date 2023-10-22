import tkinter as tk
from tkinter import ttk
from enum import Enum
import prompt


class Setup(tk.Tk):  # highest class in the heirarchy of the GUI of the Setup process.

    def __init__(self):
        super().__init__()

        # initiate default variables and settings
        self.current_step = 1  # set the current step of the setup process to 1.
        self.new_user = False  # set new user to False by default.
        self.client_state = ClientState.FELSIC  # set installed client type as Felsic (light) by default. 
        self.username = "Terra"  # set default username as Terra by default.
        
        # initiate the different frames (steps) of the setup orcess
        self.step_one_frame = ttk.Frame(self)
        self.step_two_frame = ttk.Frame(self)
        self.step_three_frame = ttk.Frame(self)
        self.step_four_frame = ttk.Frame(self)
        self.step_five_frame = ttk.Frame(self)

        self.title("Earth v0.0.3")  # set Title

        # Calculate the resolution of the GUI by the screen resolution.
        window_width = int(self.winfo_screenwidth() * .60)
        window_height = int(self.winfo_screenheight() * .50)

        self.geometry(f'{window_width}x{window_height}')  # set GUI resolution.
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.draw_step_one()  # draw the frame of step one of the Setup process.
        self.mainloop()

    def draw_step_one(self):  # method to represent step one - new user or existing user (import files)
        title = ttk.Label(self.step_one_frame, text="Earth")  # draw title

        prompt = ttk.Label(self.step_one_frame, text="Are you importing an existing profile?")  # write prompt - new or existing user.
        new_user = ttk.Button(self.step_one_frame, text="Starting Fresh", command=lambda: self.submit(True))  # create Button for new users.
        existing_user = ttk.Button(self.step_one_frame, text="Importing", command=lambda: self.submit(False))  # create Button for existing users.

        # grid & arrange widgets in step_one frame
        title.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        prompt.grid(row=1, column=0, columnspan=2)
        new_user.grid(row=2, column=0, sticky='NESW', pady=(10, 0))
        existing_user.grid(row=2, column=1, sticky='NESW', pady=(10, 0))

        # grid the step_one frame
        self.step_one_frame.grid()

    def draw_step_two(self):  # method to represent step two of the setup process for new users - light install or heavy
        title = ttk.Label(self.step_two_frame, text="Earth")

        prompt = ttk.Label(self.step_two_frame, text="Felsic or Mafic?")  # write prompt - felsic (light) or mafic (heavy)

        # write Buttons meant to represent options of install - felsic (light) or mafic (heavy)
        felsic = ttk.Button(self.step_two_frame, text="Felsic", command=lambda: self.submit(ClientState.FELSIC))
        mafic = ttk.Button(self.step_two_frame, text="Mafic", command=lambda: self.submit(ClientState.MAFIC))

        # grid & arrange widgets
        title.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        prompt.grid(row=1, column=0, columnspan=2)
        felsic.grid(row=2, column=0)
        mafic.grid(row=2, column=1)

        # grid the frame to display.
        self.step_two_frame.grid()

    def draw_step_three(self):  # draw step three - username setup step
        title = ttk.Label(self.step_three_frame, text="Earth")  # draw title

        prompt = ttk.Label(self.step_three_frame, text="Username: ")  # draw prompt requsting username

        username = ttk.Entry(self.step_three_frame)  # create Entry for user to input username
        submit = ttk.Button(self.step_three_frame, text="Enter", command=lambda: self.submit(username.get()))  # create Button to submit username (see command: )

        username.bind('<Return>', lambda x: self.submit(username.get()))  # bind Enter to username field so when User presses Enter key, it'll attempt to submit username.

        # grid & arrange data in frame
        title.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        prompt.grid(row=1, column=0)
        username.grid(row=1, column=1)
        submit.grid(row=2, column=0, columnspan=2, sticky='NESW', pady=(10, 0))

        # grid and display frame.
        self.step_three_frame.grid()

    def draw_step_four(self):  # draw step four to represent services selection (e.g. weather services, geolocation)
        title = ttk.Label(self.step_four_frame, text="Earth")  # set Title

        prompt = ttk.Label(self.step_four_frame, text="Please select the services to register")  # prompt to select services.

        variable = tk.StringVar(self.step_four_frame)  # create default variable for dropdown menu of services.
        variable.set("NWS")  # set default variable value.
        weather_options = tk.OptionMenu(self.step_four_frame, variable, "NWS", "GreatEpicWeatherXW", "SuperCoolWeather")  # create dropdown menu (optionmenu) to select services to register.

        submit = tk.Button(self.step_four_frame, text="Submit", command=lambda: self.submit('foo'))  # create Button to submit selected services registered.

        # grid & arrange widgets.
        title.grid(row=0, column=0, columnspan=2)
        prompt.grid(row=1, column=0, columnspan=2)
        weather_options.grid(row=2, column=0)
        submit.grid(row=3, column=0)

        self.step_four_frame.grid_rowconfigure(index=0, weight=1)
        self.step_four_frame.grid_columnconfigure(index=0, weight=1)

        # grid and display frame.
        self.step_four_frame.grid()

    def submit(self, variable):

        if self.current_step == 1:  # current step is: select if new user or existing user
            # if current_step = 1, then variable = new_user (bool) - state of whether person is new user or not.

            if isinstance(variable, bool):  # verify that variable is of right type
                self.new_user = variable  # set new user state equal to variable input

                if self.new_user:  # new user is True
                    self.current_step += 1  # increase stepcount by one
                    self.step_one_frame.destroy()  # destroy frame of current step
                    self.draw_step_two()  # draw frame of next step.
                else:
                    print()
            else:
                print("Raise error.")

        elif self.current_step == 2:  # current step is: select felsic (light) or mafic (heavy)
            print()
            # if current_step = 2, then variable = felsic_state (bool) - state of whether user selected felsic or mafic.

            if isinstance(variable, ClientState):  # verify that variable is of right type
                self.client_state = variable  # set felsic state equal to variable input
                if self.client_state == ClientState.FELSIC:  # felsic (light) was selected.
                    pass
                elif self.client_state == ClientState.MAFIC:  # mafic (heavy) was selected.
                    pass
                self.current_step += 1  # increase stepcount by one
                self.step_two_frame.destroy()  # destroy frame of current step
                self.draw_step_three()  # draw frame of next step
            else:
                print("Raise error.")

        elif self.current_step == 3:
            # if current_step = 3, then variable = username (str). Need to sanitize username and make sure it's valid.

            if isinstance(variable, str):
                if variable.isalnum():
                    self.current_step += 1
                    self.step_three_frame.destroy()
                    self.draw_step_four()
                    # proceed to next step
                else:
                    prompt.PromptWindow(status_level=prompt.StatusLevel.INFO, message='Incorrect username input.')


class ClientState(Enum):
    FELSIC = 1
    MAFIC = 2