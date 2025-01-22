from config import config
from gui.setup import Setup


def get_users():
    pass


def startup():
    config.create_config_files()  # Will create any config files that are missing.
    if config.is_initial_run(): # first time set up
        Setup() # initiate GUI for first time set up

        # configure services & settings
        # optionally create an account. If not, skip X step(s).
        # if created a profile, select locations to monitor and modify their settings.
        # if no profile created, use default settings and look up a location.
    else:
        pass

def login():
    pass

if __name__ == '__main__':
    startup()
