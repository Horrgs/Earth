from needaname import req
from wrappers.weather.weathergov.utils import QuantitativeValue
from dataclasses import dataclass
import json
import typing


@dataclass
class GridpointForecastPeriod:
    """ Class representing detailed forecast data for a specific time period for a gridpoint.
    Follows NWS GridpointForecastPeriod schema. """

    number: int  # sequential number ID of the forecasted period.
    name: str  # text description of the forecasted period. (e.g. Tuesday Night)

    start_time: str  # ISO8601 timestamp. start time of the forecasted period.
    # Example output (2022-06-09T06:08:03+00:00). Unsure of timezone handling.

    end_time: str  # ISO8601 timestamp. end time of the forecasted period.
    # Example output (2022-06-09T06:08:03+00:00). Unsure of timezone handling.

    is_daytime: bool  # boolean val on whether its daytime (True) or nighttime (False).

    temperature: None  # sort of deprecated. see gridpoint.py (old) & docs.
    temperature_unit: None  # sort of deprecated. see gridpoint.py (old) & docs.

    temperature_trend: str  # If not null, indicates a temperature trend that doesn't follow diurnal (day-night) cycles.
    #  only two possible values - "rising" [overnight] & "falling" [during daytime]. NULLABLE.

    wind_speed: None  # sort of deprecated. see gridpoint.py (old) & docs.
    wind_gust: None  # sort of deprecated. see gridpoint.py (old) & docs.

    wind_direction: str  # text description indicating wind direction (e.g. ESE for east-southeast)

    icon: None  # Technically deprecated, but still appears in response.
    # icon graphic representing the forecast (e.g. sun for clear skies/sunny weather).

    short_forecast: str  # short text summary of the forecast for the given forecast period.
    detailed_forecast: str  # long, detailed summary of the forecast for the given forecast period.


@dataclass
class GridpointForecast:
    """ Class representing detailed forecast data for a gridpoint. Follows NWS GridpointForecast schema. """

    context: None  # JsonLdContext. ['@context']
    geometry: None  # GeometryString. NULLABLE.

    units: str  # Specifies the units that are used in the text parts of the forecast.
    # Only two possible values - "us" & "si"

    forecast_generator: str  # the generator used to create the text-based forecast. Only relevant for debugging.
    generated_at: str  # ISO8601 timestamp. The timestamp the forecast was generated.
    update_time: str  # ISO8601 timestamp. The timestamp the forecast was generated.
    valid_times: str  # ISO8601 timestamp.
    elevation: None  # QuantitativeValue. elevation of the forecast area.
    periods: [GridpointForecastPeriod]  # array of (GridpointForecastPeriod's) forecast periods for the given area.


@dataclass
class GridpointForecastGeoJson:
    """ Class representing detailed forecast data for a gridpoint using advanced geolocation tools.
    Follows NWS GridpointForecastGeoJson schema. """

    context: None  # JsonLdContext. ['@context']
    id: None  # unknown meaning.
    type: str  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry. Need to implement GeoJson library.
    properties: None  # returns GridpointForecast object.


class Gridpoint:
    """ Class representing raw forecast data for a gridpoint. Follows NWS Gridpoint schema."""
    pass


class GridpointForecastPeriodOld:  # GridpointForecastPeriod schema, look at GridpointForecastGeoJson.
    #  period = None

    def __init__(self, period):
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

