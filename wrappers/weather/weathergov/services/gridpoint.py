from needaname import req
from wrappers.weather.weathergov.utils import QuantitativeValue
import dataclasses
import json
import typing


class Gridpoint:
    # fetch raw forecast data for a specific gridpoint of a given NWS office.
    pass


class GridpointForecastPeriod:  # GridpointForecastPeriod schema, look at GridpointForecastGeoJson.
    #  period = None

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
        # self.temperature = QuantitativeValue(period['temperature'])

        self.temperature_unit = period['temperatureUnit']  # unit of the temperature value.
        """TODO: This property is deprecated. Future versions will indicate the unit within the quantitative value
         object for the temperature property. To make use of the future standard format now, set the
         forecast_temperature_qv feature flag on the request."""

        self.temperature_trend = period['temperatureTrend']  # if not null, indicates temperature trend that doesn't
        # follow day-night cycle for forecasted period

        self.wind_speed = period['windSpeed']  # wind speed for the period.
        """TODO: This property as an string value is deprecated. Future versions will express this value as a 
        quantitative value object. To make use of the future standard format now, set the forecast_wind_speed_qv" 
        feature flag on the request."""

        # self.wind_speed = QuantitativeValue(period['windSpeed'])

        self.wind_gust = period['windGust']  # peak wind gust for the period.
        """TODO: Per NWS docs, This property as an string value is deprecated. Future versions will express this value 
        as a quantitative value object. To make use of the future standard format now, set the "forecast_wind_speed_qv" 
        feature flag on the request."""
        # self.wind_gust = QuantitativeValue(period['windGust'])

        self.wind_direction = period['windDirection']
        # text description (e.g. SSE) of the prevailing wind direction.

        self.icon = period['icon']  # deprecated per NWS docs, no indication of replacement.

        self.short_forecast = period['shortForecast']  # short text summary of the forecast for the period.
        self.detailed_forecast = period['detailedForecast']  # detailed text description of the forecast for the period.


class GridpointForecast:
    # fetch detailed & textual forecast for a specific gridpoint of a given NWS office.

    def __init__(self, foo):
        # self.context = foo['@context']  # JsonLdContext
        # self.geometry = foo['geometry']  # GeometryString.
        # self.units = foo['units']  # Specifies the units that are used in the text parts of the forecast.
        self.forecast_generator = foo['forecastGenerator']  # Generator that was used to create the textual forecast (per NWS, only relevant for debugging.)
        self.generated_at = foo['generatedAt']  # time the forecast data was generated.
        self.update_time = foo['updateTime']  # last time the data for this forecast was updated.
        # self.valid_times = foo['validTimes'] # ISO8601Interval
        self.elevation = QuantitativeValue(foo['elevation'])  # elevation of the forecast area.
        self.periods = [GridpointForecastPeriod(i) for i in foo['periods']]  # an array of forecast periods.


class GridpointForecastGeoJson:
    # fetch forecast for a specific gridpoint of a given NWS office, using GeoJSON.
    # 14 12-hour periods, giving 7-day forecast. Endpoint: https://api.weather.gov/gridpoints/TOP/31,80/forecast
    # 156 -1hour periods, giving 7-day forecast. Endpoint: https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly.

    def __init__(self, foo):
        self.context = foo['@context']  # JsonLdContext
        self.id = foo['id']  # ?
        self.type = foo['type']  # ?
        self.geometry = foo['geometry']  # GeoJsonGeometry.
        self.properties = GridpointForecast(foo['properties'])