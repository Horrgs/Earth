import tkinter as tk
from enum import Enum
import backend.user.user as user


# Enum to represent the state of the client installed on the computer.
class ClientState(Enum):
    FELSIC = 1  # light install (client only)
    MAFIC = 2  # heavy install


class EarthApp(tk.Tk):  # This class represents the highest instance of the Earth application after Setup has been done.

    def __init__(self):
        super().__init__()
        self.title("Earth v0.0.3")  # set Title
        self.home_frame = tk.Frame(self)  # create home frame.

        # Calculate the resolution of the GUI by the screen resolution.
        window_width = int(self.winfo_screenwidth() * .60)
        window_height = int(self.winfo_screenheight() * .50)

        self.geometry(f'{window_width}x{window_height}')  # set GUI resolution.
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.active_users = user.get_active_users()  # get list of active users.
        for active_user in self.active_users:
            pass



    def draw_home(self):

        welcome_msg = tk.Label(self.home_frame, text="Welcome, {0}")