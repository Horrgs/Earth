# import std libraries
from dataclasses import dataclass
from typing import Optional, List
import os, uuid, json, logging

from dataclasses_json import dataclass_json  # import of 3rd party library

# import intra- package libraries.
from utils.req import req, RequestMethod
from backend.user.locations import Location
from backend.user.services import Service
from config import config
from backend.wrappers import geoservices


@dataclass_json
@dataclass  # TODO: get registered services (e.g. weather.gov, usgs earthquakes, NASA fire) - # 1/19/25 - Not sure why this TODO is here. This is handled by load_servies in /user/services.py
class User:
    display_name: str  # display name of the User.
    account_id: int  # unique numerical identifier assigned to each User.
    locations: Optional[List[Location]] = None  # list of locations the User monitors.
    services: Optional[str] = None  # list of services the User has registered.

    def __post_init__(self):
        pass


    def register_location(self, new_location: Location): # allows a User to register a location.
        for existing_location in self.locations:  # TODO: if no locations have been registered (e.g. new users), self.locations is likely None. Could cause error.
            """
            if geoservices.calculate_distance(new_location, existing_location) < 1000 meters:
                # location too close
                
                The 'need' for a threshold should be scrutinized. Weather can change within just a short distance. Maybe 500m.
            """

            if new_location.title == existing_location.title:
                raise ValueError("Location with that name already exists!")  # TODO: improve error handling. Should handle the error and keep trying again until its a valid name.
        self.locations.append(new_location)
        config.update()


    def modify_location(self):  # function for modifying the data for an existing Location
        pass

    def register_service(self, service):  # function for registering a new Service.
        pass

    def load_services(self) -> List[Service]:  # function that returns a list of Service objects of enabled Services.
        config_files = config.get_config_files()  # get config files
        if 'settings.json' not in config_files:  # check if settings.json exists and create if necessary.
            config.create_config_files()  # create config files. it will only create what's missing (i.e. settings.json)
            logging.info('settings.json not in {0}. Creating file(s).'.format(config.get_earth_directory()))

        enabled_subservices = []  # create empty list to store enabled services
        with open(config_files['settings.json'], mode='r') as config_file:  # open settings.json
            service_data = json.load(config_file)['services']  # load json data into dict and select services
            for service, subservices in service_data.items():  # loop over each service and a list of their subservices
                enabled_subservices.extend([subservice for subservice in subservices if
                                            subservice["enabled"]])  # add subservices that are enabled
        config_file.close()  # close settings.json

        services = [Service.from_dict(subservice) for subservice in
                    enabled_subservices]  # returns list of Service objects from the list of enabled ones in enabled_subservices
        return services

    def modify_service(self):  # method for modifying the data of a Service registered to the User.
        pass


    def get_weather_profile(self):
        return "f"

"""    
    method deprecated in favor of modify_service(). Commented out as not in use.
    def register_key(self, service: Service):
        services = self.load_services()  # find all services that are enabled - # TODO: we should avoid calling this each time a key needs to be registered, this should be cached.
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

    # this method - register_location() - should be moved to wrappers/weather/weathergov. commented out as not in use.
    def register_location(self, latitude, longitude, flags=None):
        # for each registered service, fetch relevant metadata.

        # for NWS service
        url = "https://api.weather.gov/points/{0},{1}".format(latitude, longitude)
        weathergov_req = req(url, RequestMethod.GET)
        response = {
            'gridId': weathergov_req['properties']['gridId'],
            'gridX': weathergov_req['properties']['gridX'],
            'gridY': weathergov_req['properties']['gridY']
        }
        self.locations.append(Location(
            longitude=weathergov_req['geometry']['corrdinate'][0],
            latitude=weathergov_req['geometry']['corrdinate'][1],
            time_zone=weathergov_req['properties']['']
        ))
        self.locations.append(response)"""

def create_user(user: User) -> User:
    active_users = get_active_users()
    used_ids = [u.account_id for u in active_users]
    account_id_temp = uuid.uuid4().int & (1 << 32) - 1  # generate random 32-bit unsigned integer
    attempt = 1
    while account_id_temp in used_ids:
        account_id_temp = uuid.uuid4().int & (1 << 32) - 1  # generate random 32-bit unsigned integer
        attempt += 1
        if attempt > 10:
            break
    earth_dir = config.get_earth_directory()
    user_file_path = os.path.join(earth_dir, 'users.json')
    with open(user_file_path, 'a') as user_file:
        user_json = user.to_json()
        user_file.write(user_json)
        user_file.write('\n')
    return user


def get_active_users() -> List[User]:  # Returns list of User objects of created Users.
    earth_dir = config.get_earth_directory()  # gets path to the program files.
    user_file_path = os.path.join(earth_dir, 'users.json')  # creates path to the users.json file.

    if not os.path.exists(user_file_path):  # checks if the users.json file exists.
        return []  # TODO: ???

    with open(user_file_path) as user_file:  # opening users.json file to load data.
        try:
            user_data = json.load(user_file)  # load data.
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in {user_file_path}: {e}")  # TODO: better error handling.
        user_file.close()

    return [User.from_dict(user) for user in user_data]  # return list of User objects of created objects.


def load_users() -> List[User]:
    # get path to program files & then specifically users.json
    earth_dir = config.get_earth_directory()
    user_file_path = os.path.join(earth_dir, 'users.json')

    if not os.path.exists(user_file_path):  # check if users.json DOES NOT exist.
        raise FileNotFoundError("[Earth] users.json missing!")  # TODO: better error handling.
    else:
        with open(user_file_path) as user_file:  # open users.json file.
            try:
                users_data = json.load(user_file)  # load users.json data.
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON in {user_file_path}: {e}")  # TODO: better error handling.
            user_file.close()

        users = []
        for user_dict in users_data:
            users.append(User(**user_dict))  # load list of users json data into User objects in a list.
        return users  # return list of created User objects.
    