from utils.req import req, RequestMethod
from backend.wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson
from backend.wrappers.weather.weathergov.services.point import PointGeoJson
from backend.user.user import User


def get_weather(user: User):

    for service in user.services:
        if service.name == "NWS":
            pass
        elif service.name == "tomorrow.io":
            pass
        else:
            pass
    pass


def get_location_metadata(location):  # pass (+/-lat,lng) in +/- and comma, string format and retireve NWS sector.
    # Preparing 'payload'

    location = list(map(float, location.split(",")))  # split lat-lng point mapped as floats in a list.

    base_url = "https://api.weather.gov/"  # base format of the URL
    meta_url = base_url + "points/{0},{1}".format(*location)  # fill in lat-lng point into url.
    metadata = req(meta_url, RequestMethod.GET)  # cache metadata for ~X hours.
    # this metadata should be loaded into a Point  dataclass.
    return PointGeoJson.from_json(metadata.content)  # return Point data for location


def get_weather_summary(point: PointGeoJson):  # get GridpointForecastGeoJson obj for given PointGeoJson obj.
    point = point.properties  # access the properties field (class type Point)
    forecast_data = req(point.forecast, RequestMethod.GET)  # access Points' forecast URL and send GET req for forecast
    return GridpointForecastGeoJson.from_json(forecast_data.content)  # return Foreceast as GridpointForecstGeoJson


def get_hourly_weather(point: PointGeoJson):  #
    point = point.properties
    forecast_hourly = req(point.forecast_hourly, RequestMethod.GET)
    return GridpointForecastGeoJson.from_json(forecast_hourly.content)


nws_point = get_location_metadata('42.8864,-78.8784')
weather = get_weather_summary(nws_point)

"""
for period in weather.properties.periods:
    print("{0}: {1}".format(period.name, period.detailed_forecast))
"""

hourly = get_hourly_weather(point=nws_point)
print(hourly)
"""for period in hourly.properties.periods:
    print(period)"""
