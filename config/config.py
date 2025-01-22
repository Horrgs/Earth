# import std libs.
import os
import platform
import json


def is_initial_run():
    """
    Checks if this is the initial run of the program.

    Returns:
        bool: True if initial run, False otherwise.
    """
    # Get the file path of the parent directory of config files
    parent_dir = get_earth_directory()

    # Open the settings.json file in read mode
    with open(os.path.join(parent_dir, 'settings.json'), 'r') as config_file:
        # Load the JSON data into a Python object
        data = json.load(config_file)

        # Close the file & return the value of the 'initial' key
        config_file.close()
        return data.get('initial', True)  # TODO: I'm unsure on the datatype of data, where the .get() method is being called from, and why there's a bool value.

def get_earth_directory():  # finds the path to the Earth program based on OS.
    if platform.system() == 'Windows':  # check if system is Windows
        parent_dir = os.path.expanduser(r'~/Documents/')  # r' handles the backslash (/) Windows incompatibly issue.
    elif platform.system() == 'Linux':
        parent_dir = os.path.expanduser('~/Documents/')
    else:
        raise Exception('Unsupported operating system.')  # TODO: better error handling.

    earth_dir = os.path.join(parent_dir, 'Earth')  # create path to the folder Earth/ in Documents/
    if not os.path.isdir(earth_dir):  # check if Earth/ program folder DOES NOT exist.
        create_config_files()  # since the program folder does not exist, we create the files.
    return earth_dir  # return path to Earth program.


def get_template_files():
    """Get the list of template files in the config folder of the project directory."""
    # Use os.path.abspath() to get the absolute path of the current script and its directory.
    # os.path.dirname() then gets the directory of the script, and os.path.join() appends the 'config' directory
    # to create a path relative to the script file.
    template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

    template_files = []  # create empty list of template files
    for filename in os.listdir(template_folder):  # loop over files in template_folder (config/)
        if filename.endswith('.json'):  # find files that end in .json
            template_files.append(os.path.join(template_folder, filename))  # append json file to template files
    return template_files  # return the template files from config/


def create_config_files():  # creates config files, including any that are missing from an existing installation.
    """Create the configuration files based on the config."""
    template_files = get_template_files()  # get a list of the template files
    if not template_files:
        raise Exception('No template files found in the config folder.')  # template files are missing # TODO: better error handling.

    # set the parent directory to the users' local Documents folder
    if platform.system() == 'Windows':  # check if system is Windows
        parent_dir = os.path.expanduser(r'~/Documents/')  # r' handles the backslash (/) / Windows incompatibly issue.
    elif platform.system() == 'Linux':
        parent_dir = os.path.expanduser('~/Documents/')
    else:
        raise Exception('Unsupported operating system.')  # TODO: better error handling.

    earth_dir = os.path.join(parent_dir, 'Earth')  # create path to the project folder Earth/ in Documents/
    if not os.path.isdir(earth_dir):  # check if project folder Earth/ exists
        os.mkdir(earth_dir)  # create project folder Earth directory.

    for template_file in template_files:  # loop over template files
        with open(template_file, 'r') as f:  # open template file in read-only
            config = json.load(f)  # load json data into python directory

        config_file = os.path.join(earth_dir, os.path.basename(template_file)) # create path for the configuration file(s) being made
        if os.path.isfile(config_file): # check if the configuration file already exists
            print(f"Configuration file '{config_file}' already exists. Skipping.")
            continue

        with open(config_file, 'w') as f: # open the file path for the config file in write mode
            json.dump(config, f)  # write in the template data to the config file.
            print(f"Created configuration file '{config_file}'.")
            f.close()  # Close file once done writing.

def get_config_files():  # get dict of config files in k-v form. key is file name, value is absolute file path.
    if platform.system() == 'Windows':  # check if system is Windows
        parent_dir = os.path.expanduser(r'~/Documents/')  # r' handles the backslash (/) / Windows incompatibly issue.
    elif platform.system() == 'Linux':  # check if system is Linux
        parent_dir = os.path.expanduser('~/Documents/')  # set parent directory
    else:
        raise Exception('Unsupported operating system.')  # TODO: better error handling.

    earth_dir = os.path.join(parent_dir, 'Earth')  # create path to the program folder Earth/ in Documents/  # TODO: should we be using get_earth_directory() ?

    config_files = {}  # create dict to store config file paths
    if os.path.isdir(earth_dir):  # check if program folder Earth/ folder exists
        for f in os.listdir(earth_dir):  # loop files in program folder Earth/
            config_files[f] = os.path.join(earth_dir, f)  # store config file paths in config_files dict by file name.
    return config_files  # return dict of config files in filename-filepath (k-v) form.

if __name__ == '__main__':
    # create_config_files()
    print(get_config_files())

