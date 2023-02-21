import config
import json
from user.services import Service


def get_users():
    pass


def setup():
    config.create_config_files()  # Will create any config files that are missing.
    # configure services & settings
    # optionally create an account. If not, skip X step(s).
    # if created a profile, select locations to monitor and modify their settings.
    # if no profile created, use default settings and look up a location.


if __name__ == '__main__':
    setup()
