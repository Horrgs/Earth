# import std libraries
from dataclasses import dataclass
from typing import Optional, List
import os, uuid, json

from dataclasses_json import dataclass_json  # import of 3rd party library

# import intra- package libraries.
from utils.req import req, RequestMethod
from backend.user.locations import Location
from config import config
from backend.wrappers import geoservices


@dataclass_json
@dataclass  # TODO: get registered services (e.g. weather.gov, usgs earthquakes, NASA fire) - # 1/19/25 - Not sure why this TODO is here. This is handled by load_servies in /user/services.py
class User:
    display_name: str  # display name of the User.
    account_id: int  # unique numerical identifier assigned to each User.
    locations: Optional[List[Location]] = None  # list of locations the User monitors.
    services: Optional[str] = None  # list of services the User has registered.

    def register_location_new(self, new_location: Location):
        for existing_location in self.locations:  # TODO: self.locations is None as no data is ever loaded into it.
            """
            if geoservices.calculate_distance(new_location, existing_location) < 1000 meters:
                # location too close
                
                The 'need' for a threshold should be scrutinized. Weather can change within just a short distance. Maybe 500m.
            """

            if new_location.title == existing_location.title:
                raise ValueError("Location with that name already exists!")  # TODO: improve error handling.

        self.locations.append(new_location)
        config.update()

    # this method - register_location() - should be moved to wrappers/weather/weathergov
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
        self.locations.append(response)

    def modify_location(self):
        pass

    def register_service(self, service):
        pass

    def get_weather_profile(self):
        return "f"





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
    