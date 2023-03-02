from utils.req import req, RequestMethod
from backend.user.locations import Location


class PositionStack:  # Wrapper for PositionStack

    def __init__(self):
        self.base_url = "http://api.positionstack.com/v1/" # base URL to PositionStack
        self.key = ""  # fetch key. Hard-coded ATM. DO NOT COMMIT.
        pass

    def get_location(self, address):  # Get the Location (user.locations) of a given address
        url = "http://api.positionstack.com/v1/forward?access_key={0}&query={1}&&timezone_module=1"  # base URL for search
        url.format(self.key, address)  # format URL with the API key and inputted address
        geocode = req(url, RequestMethod.GET)  # send request for forward geocoding of the address.

        response = geocode['data'][0]  # trim down the scope

        latitude = response['latitude']  # returns latitude of address
        longitude = response['longitude']  # returns longitude of address
        time_zone = response['timezone_module']['name']  # America/Detroit returned for WNY?? gives time zone for location.
        name = response['neighbourhood']  # get formatted name of the locale.

        return Location(latitude, longitude, time_zone, name)  # return Location object.


class Geoapify:
    pass