from utils.req import req, RequestMethod
from user.locations import Location

class PositionStack:

    def __init__(self):
        self.base_url = "http://api.positionstack.com/v1/"
        self.key = ""  # fetch key. Hard-coded ATM. DO NOT COMMIT.
        pass

    def get_coordinates(self, address):
        url = "http://api.positionstack.com/v1/forward?access_key={0}&query={1}&&timezone_module=1"
        url.format(self.key, address)
        geocode = req(url, RequestMethod.GET)  # send request to forward geocode.
        response = geocode['data'][0]  # trim down the scope
        latitude = response['latitude']  # returns latitude of address
        longitude = response['longitude']  # returns longitude of address
        time_zone = response['timezone_module']['name']  # America/Detroit returned for parents?? # gives time zone for location.
        name = response['neighbourhood']  # get formatted name of the locale.

        return Location(latitude, longitude, time_zone, name)
        # return Location object.


class Geoapify:
    pass