from wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from utils.req import req, RequestMethod
from wrappers.weather.weathergov.services.point import Point
from dataclasses import dataclass
import json
from utils.geoservices import PositionStack


def get_gridpoint_weather(code, grid, hourly=False):
    """Get the weather forecast for a NWS gridpoint.
    param: code - NWS issued code, designated per jursidcition (i.e. BUF for Buffalo)
    param: grid - NWS issued raw, a subset of each code (i.e. [41, 30] of BUF)
    param: hourly - Fetch 1 hour period forecasts. If false (by default), periods are 12 hours

    return: GridpointForecastGeoJson object, see NWS schema details for more."""

    url = "https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast".format(code, grid[0], grid[1])  # format request url
    if hourly:  # check if hourly data is being requested
        url = "{0}/hourly".format(url)  # hourly data is requested, format url.
    response = req(url, RequestMethod.GET)  # issue GET request for the formatted url.

    return GridpointForecastGeoJson.from_json(json.dumps(response))
    # convert response to json & convert to GridpointForecastGeoJson object, then return it.

"""
gg = get_grid_info([42.3601, -71.0589])
f = get_gridpoint_weather(gg['gridId'], list(gg.values())[1:], False)
for p in f.properties.periods:
    print(p) """


def __init__():
    location = "42.8864,-78.8784"
    location = list(map(float, location.split(",")))

    base_url = "https://api.weather.gov/"
    meta_url = base_url + "points/{0},{1}".format(*location)
    metadata = req(meta_url, RequestMethod.GET)  # cache metadata for ~X hours.

    # this metadata should be loaded into a Point  dataclass.

    forecast_url = metadata['properties']['forecast']
    forecast_hourly_url = metadata['properties']['forecastHourly']
    raw_forecast_url = metadata['properties']['forecastGridData']

    forecast_data = req(forecast_url, RequestMethod.GET)
    forecast_data = GridpointForecastGeoJson.from_json(json.dumps(forecast_data))
    print(forecast_data)


def get_grid_info(point):
    url = "https://api.weather.gov/points/{0},{1}"
    point = [str(p).strip() for p in point]
    url = url.format(*point)
    print(url)
    push_req = req(url, RequestMethod.GET)
    push_req = push_req['properties']
    response = {
        'gridId': push_req['gridId'],
        'gridX': push_req['gridX'],
        'gridY': push_req['gridY']
    }
    return response


def get_weather(point):
    url = "https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast"
    grid_info = get_grid_info(point)
    url = url.format(grid_info['gridId'], grid_info['gridX'], grid_info['gridY'])
    push_req = req(url, RequestMethod.GET)
    print(push_req)


f = get_grid_info([42.9, -78.5])
print(list(f.values()))

def bob():
    location = input("Enter location: ")
    geocode = PositionStack().get_coordinates(location)  # not ideal, don't want class. make classless.
    nws_point = req("https://api.weather.gov/points/{0},{1}".format(geocode.latitude, geocode.longitude), RequestMethod.GET)
    p = Point(nws_point)
    forecast_data = req("https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast", RequestMethod.GET)
    forecast = GridpointForecastGeoJson(forecast_data)

__init__()