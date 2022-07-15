from dataclasses import dataclass
from typing import Optional, List, Dict
from utils.req import req, RequestMethod
from user.locations import Location


def create_user(name: str):
    # create UUID for user.
    pass


@dataclass  # TODO: get registered services (e.g. weather.gov, usgs earthquakes, NASA fire)
class User:
    account_id: int  # unique numerical identifier assigned to each User.
    display_name: str  # display name of the User.
    locations: Optional[List[Location]] = None  # list of locations the User monitors.
    services: Optional[str] = None  # list of services the User has registered.

    def register_location(self, latitude, longitude, flags=None):
        # for each registered service, fetch relevant metadata.

        # for NWS service
        url = "https://api.weather.gov/points/{0},{1}".format(latitude, longitude)
        weathergov_req = req(url, RequestMethod.GET)
        weathergov_req = weathergov_req['properties']
        response = {
            'gridId': weathergov_req['gridId'],
            'gridX': weathergov_req['gridX'],
            'gridY': weathergov_req['gridY']
        }
        self.locations.append(response)

    def modify_location(self):
        pass

    def register_service(self, service):
        pass
