from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from config import config
import json
from typing import List


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Service:
    name: str  # name of the service (i.e. weather.gov)
    endpoint: str  # endpoint for the services' API.
    enabled: bool  # method for enabling/disabling a servce
    api_key: str = None  # api key for the service. None if no API key required.


def load_services() -> List[Service]:  # function that gets all enabled services and loads them
    config_files = config.get_config_files()  # get config files
    if 'settings.json' not in config_files:  # check if settings.json exists and create if necessary.
        config.create_config_files()  # create config files. it will only create what's missing (i.e. settings.json)
        raise Exception("settings.json not in {0}. Creating file(s).".format(config.get_earth_directory()))  # TODO: error seems to be somewhat handled well, but update output & logging.

    enabled_subservices = []  # create empty list to store enabled services
    with open(config_files['settings.json'], mode='r') as config_file:  # open settings.json
        service_data = json.load(config_file)['services']  # load json data into dict and select services
        for service, subservices in service_data.items(): # loop over each service and a list of their subservices
            enabled_subservices.extend([subservice for subservice in subservices if subservice["enabled"]])  # add subservices that are enabled
    config_file.close()  # close settings.json

    services = [Service.from_dict(subservice) for subservice in enabled_subservices]  # returns list of Service objects from the list of enabled ones in enabled_subservices
    return services


def register_key(service: Service):
    services = load_services()  # find all services that are enabled - # TODO: we should avoid calling this each time a key needs to be registered, this should be cached.
    service_names = [s.name for s in services]  # find all the names of all the services that are enabled.
    if service.name not in service_names:
        # TODO: raise Error indicating that this service does not exist and thus cannot be registered
        pass
    else:
        config_files = config.get_config_files()  # fetches dict of config files in file_name-file_path (k-v) format.
        with open(config_files['settings.json'], mode='r') as config_file:  # open settings.json
            service_data = json.load(config_file)['services']  # load json data into dict and select services
           # service_data.extend(service.to_json())  # TODO: this LoC might be incorrect. One, we don't write this data to disk etc,. Two, extend() *ADDS* to the end of the list, but we are registering already EXISTING services.
        config_file.close()