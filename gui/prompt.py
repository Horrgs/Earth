from enum import Enum
import tkinter as tk


class StatusLevel(Enum):  # Enum to represent the Status Level of the prompt.
    INFO = 1  # e.g. a tip hint.
    WARNING = 2  # e.g. an anticipated invalid input, like a bad username.
    ERROR = 3  # e.g. a non-critical crash, potentially unanticipated
    CRITICAL = 4  # e.g. a critical crash, likely unanticipated


class PromptWindow(tk.Tk):  # Main instance that represents the GUI for a prompt

    def __init__(self, status_level: StatusLevel, message):  # require Status Level & message purpose of the prompt
        super().__init__()
        self.title("Earth v0.0.3 - {0}".format(status_level.name))  # set Title

        self.geometry('500x200')  # set GUI resolution.
        self.grid_columnconfigure(index=0, weight=1)

        message_label = tk.Label(self, text=message)  # add in the message that serves the prompt.
        message_label.grid(column=0, row=0)

        acknowledge = tk.Button(self, text='OK', command=self.destroy)  # button to acknowledge prompt
        acknowledge.grid(column=0, row=1)

        self.mainloop()