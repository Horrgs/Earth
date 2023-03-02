from backend.wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from backend.wrappers.weather.weathergov.services.point import PointGeoJson
from utils.req import req, RequestMethod
from utils.geoservices import PositionStack


def get_grid_info(point):  # retrieve the grid info of a given location (i.e. a latitude longitude)
    # Preparing 'payload'
    url = "https://api.weather.gov/points/{0},{1}" # base format of the URL
    point = list(map(float, point.split(","))) # split lat-lng point mapped as floats in a list.
    url = url.format(*point)  # fill in lat-lng point into url.

    push_req = req(url, RequestMethod.GET) # send GET request to weather.gov with lat-lng data.

    push_req = push_req['properties']  # retrieve NWS forecast grid info for the given lat-lng
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
    location = input("Enter location: ")  # Input formatted address (e.g. Main St, Albany)
    geocode = PositionStack().get_location(location)  # make classless?? Gets the Location (user.locations) of input.

    # get NWS locale from inputted Location by forward geocoding the address to latitude & longitude.
    nws_point = req("https://api.weather.gov/points/{0},{1}".format(geocode.latitude, geocode.longitude), RequestMethod.GET)

    point = PointGeoJson.from_json(nws_point.content) # load NWS locale data
    forecast_data = req(point.properties.forecast, RequestMethod.GET)  # get forecast of inputted locale
    forecast = GridpointForecastGeoJson.from_json(forecast_data.content) # load NWS forecast locale data
    return forecast

# x = get_weather('42.8864,-78.8784')
# print(x)