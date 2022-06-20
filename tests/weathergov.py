from wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from wrappers.weather.weathergov.services.point import get_grid_info
from utils.req import get, RequestMethod
import json


def get_gridpoint_weather(code, grid, hourly=False):
    """Get the weather forecast for a NWS gridpoint.
    param: code - NWS issued code, designated per jursidcition (i.e. BUF for Buffalo)
    param: grid - NWS issued gridpoint, a subset of each code (i.e. [41, 30] of BUF)
    param: hourly - Fetch 1 hour period forecasts. If false (by default), periods are 12 hours

    return: GridpointForecastGeoJson object, see NWS schema details for more."""

    url = "https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast".format(code, grid[0], grid[1])  # format request url
    if hourly:  # check if hourly data is being requested
        url = "{0}/hourly".format(url)  # hourly data is requested, format url.
    response = get(url, RequestMethod.GET)  # issue GET request for the formatted url.

    return GridpointForecastGeoJson.from_json(json.dumps(response))
    # convert response to json & convert to GridpointForecastGeoJson object, then return it.


gg = get_grid_info([42.3601, -71.0589])
f = get_gridpoint_weather(gg['gridId'], list(gg.values())[1:], False)
for p in f.properties.periods:
    print(p)
