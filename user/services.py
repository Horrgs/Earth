from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
import config
import json


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Service:
    name: str  # name of the service (i.e. weather.gov)
    endpoint: str # endpoint for the services' API.
    enabled: bool  # method for enabling/disabling a servce
    api_key: str = None # api key for the service. None if no API key required.


def load_services():  # function that gets all enabled services and loads them
    config_files = config.get_config_files()  # get config files
    if 'config.json' not in config_files:  # check if config.json exists and create if necessary.
        config.create_config_files()  # create config files. it will only create what's missing (i.e. config.json)
        raise Exception("config.json not in {0}. Creating file(s).".format(config.get_earth_directory()))

    enabled_subservices = []  # create empty list to store enabled services
    with open(config_files['config.json'], mode='r') as config_file:  # open config.json
        service_data = json.load(config_file)['services']  # load json data into dict and select services
        for service, subservices in service_data.items(): # loop over each service and a list of their subservices
            enabled_subservices.extend([subservice for subservice in subservices if subservice["enabled"]])  # add subservices that are enabled
    config_file.close()  # close config.json

    for subservice in enabled_subservices:
        print(Service.from_dict(subservice))


def register_key(service_name):
    pass