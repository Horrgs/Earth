from wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from utils.req import req, RequestMethod
from wrappers.weather.weathergov.services.point import PointGeoJson
from utils.geoservices import PositionStack

def get_grid_info(point): # retrieve the grid info of a given location (i.e. a latitude longitude)
    # Preparing 'payload'
    url = "https://api.weather.gov/points/{0},{1}" # base format of the URL
    point = list(map(float, point.split(","))) # split lat-lng point mapped as floats in a list.
    url = url.format(*point)  # fill in lat-lng point into url.

    push_req = req(url, RequestMethod.GET) # send GET request to weather.gov with lat-lng data.

    push_req = push_req['properties'] # retrieve NWS forecast grid info for the given lat-lng
    response = {
        'gridId': push_req['gridId'],
        'gridX': push_req['gridX'],
        'gridY': push_req['gridY']
    }
    return response  # return response


def get_weather(location):
    location = list(map(float, location.split(",")))

    base_url = "https://api.weather.gov/"
    meta_url = base_url + "points/{0},{1}".format(*location)
    metadata = req(meta_url, RequestMethod.GET)  # cache metadata for ~X hours.
    # this metadata should be loaded into a Point  dataclass.
    p = PointGeoJson.from_json(metadata.content)
    point = p.properties

    forecast_data = req(point.forecast, RequestMethod.GET)
    return GridpointForecastGeoJson.from_json(forecast_data.content)

def bob():
    location = input("Enter location: ")
    geocode = PositionStack().get_coordinates(location)  # not ideal, don't want class. make classless.
    nws_point = req("https://api.weather.gov/points/{0},{1}".format(geocode.latitude, geocode.longitude), RequestMethod.GET)
    p = Point(nws_point)
    forecast_data = req("https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast", RequestMethod.GET)
    forecast = GridpointForecastGeoJson(forecast_data)

x = get_weather('42.8864,-78.8784')
print(x)