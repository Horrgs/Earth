from utils import req

"""
Get forecast for given NWS station (station ID, 0). Specify the 2.5km x 2.5km grid point for station.
additional args available.
"""
def get_forecast(location):
    url = "https://api.weather.gov/gridpoints/{0}/{1}/forecast{2}"  # station id, grid_loc, addtl. args.
    url = url.format(location['id'], location['grid_location'], '')
    req = utils.send(url, utils.RequestMethod.GET, None)

    for item in req['periods']:
        p = Period(item)

class Forecast:
    pass

class DailyForecast(Forecast):  #14 12-hour periods, giving 7 day forecast. Endpoint: https://api.weather.gov/gridpoints/TOP/31,80/forecast
    pass

class HourlyForecast(Forecast):  # 156 -1hour periods, giving 7 day forecast. Endpoint: https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly.
    pass


class Period:  # GridpointForecastPeriod schema, look at GridpointForecastGeoJson.
    #period = None

    def __init__(self, period):
        self.number = period['number']  # sequential number ID of the forecasted period.
        self.name = period['name']  # text description of the forecasted period. (e.g. Tuesday Night)

        self.start_time = period['startTime']  # start time of the forecasted period.
        self.end_time = period['endTime']  # end time of the forecasted period.
        self.is_daytime = period['isDaytime']  # boolean val on whether its daytime (True) or nighttime (False).

        self.temperature = period['temperature']
        """
            Sort of deprecated? There are two flags under temperature - description and "?? one of ??". Per NWS for
            description, "High/low temperature for the period, depending on whether the period is day or night. 
            This property as an integer value is deprecated. Future versions will express this value as a quantitative 
            value object. To make use of the future standard format now, set the "forecast_temperature_qv" feature 
            flag on the request.
        """

        self.temperature_unit = period['temperatureUnit']  # unit of the temperature value.
        """TODO: This property is deprecated. Future versions will indicate the unit within the quantitative value object 
        for the temperature property. To make use of the future standard format now, set the "forecast_temperature_qv" 
        feature flag on the request."""

        self.temperature_trend = period['temperatureTrend']  # if not null, indicates temperature trend that doesn't
        # follow day-night cycle for forecasted period

        self.wind_speed = period['windSpeed']  # wind speed for the period.
        """TODO: This property as an string value is deprecated. Future versions will express this value as a quantitative 
            value object. To make use of the future standard format now, set the forecast_wind_speed_qv" feature 
            flag on the request."""

        self.wind_gust = period['windGust']  # peak wind gust for the period.
        """TODO: Per NWS docs, This property as an string value is deprecated. Future versions will express this value as 
            a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" feature
             flag on the request."""


        self.wind_direction = period['windDirection']  # text description (e.g. SSE) of the prevailing wind direction.

        self.icon = period['icon']  # deprecated per NWS docs, no indication of replacement.

        self.short_forecast = period['shortForecast']  # short text summary of the forecast for the period.
        self.detailed_forecast = period['detailedForecast']  # detailed text description of the forecast for the period.
