from wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from utils.req import req, RequestMethod
from wrappers.weather.weathergov.services.point import PointGeoJson


def get_location_metadata(location):  # retrieve the grid info of a location in lat-lng, comma separated str format. ('39,-40')
    # Preparing 'payload'

    location = list(map(float, location.split(","))) # split lat-lng point mapped as floats in a list.

    base_url = "https://api.weather.gov/" # base format of the URL
    meta_url = base_url + "points/{0},{1}".format(*location) # fill in lat-lng point into url.
    metadata = req(meta_url, RequestMethod.GET)  # cache metadata for ~X hours.
    # this metadata should be loaded into a Point  dataclass.
    return PointGeoJson.from_json(metadata.content)  # return Point data for location


def get_weather(point: PointGeoJson):  # get GridpointForecastGeoJson obj for given PointGeoJson obj.
    point = point.properties  # access the properties field (class type Point)
    forecast_data = req(point.forecast, RequestMethod.GET)  # access Points' forecast URL and send GET req for forecast
    return GridpointForecastGeoJson.from_json(forecast_data.content)  # return Foreceast as GridpointForecstGeoJson


weather = get_weather(get_location_metadata('42.8864,-78.8784'))

for period in weather.properties.periods:
    print("{0}: {1}".format(period.name, period.detailed_forecast))