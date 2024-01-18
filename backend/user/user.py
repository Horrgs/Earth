# import std libraries
from dataclasses import dataclass
from typing import Optional, List
import os, uuid, json

from dataclasses_json import dataclass_json # import of 3rd party library

# import intra- package libraries.
from utils.req import req, RequestMethod
from backend.user.locations import Location
from config import config
from backend.wrappers import geoservices

@dataclass_json
@dataclass  # TODO: get registered services (e.g. weather.gov, usgs earthquakes, NASA fire)
class User:
    display_name: str  # display name of the User.
    account_id: Optional[int] = None  # unique numerical identifier assigned to each User.
    locations: Optional[List[Location]] = None  # list of locations the User monitors.
    services: Optional[str] = None  # list of services the User has registered.

    def register_location_new(self, new_location: Location):
        for existing_location in self.locations:
            """
            if geoservices.calculate_distance(new_location, existing_location) < 1000 meters:
                # location too close
            """

            if new_location.title == existing_location.title:
                raise ValueError("Location with that name already exists!")

        self.locations.append(new_location)
        config.update()

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
    account_id_temp = uuid.uuid4().int & (1 << 32) - 1 # generate random 32-bit unsigned integer
    attempt = 1
    while account_id_temp in used_ids:
        account_id_temp = uuid.uuid4().int & (1 << 32) - 1 # generate random 32-bit unsigned integer
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


def get_active_users() -> List[User]:
    earth_dir = config.get_earth_directory()
    user_file_path = os.path.join(earth_dir, 'users.json')

    if not os.path.exists(user_file_path):
        return []

    with open(user_file_path) as user_file:
        try:
            user_data = json.load(user_file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in {user_file_path}: {e}")

    return (User.from_dict(user) for user in user_data)