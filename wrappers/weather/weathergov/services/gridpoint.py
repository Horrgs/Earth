from utils import req
from wrappers.weather.weathergov.utils import QuantitativeValue
from dataclasses import dataclass
import json
from typing import Optional, List, Dict


@dataclass
class GridpointForecastPeriod:
    """ Class representing detailed forecast data for a specific time period for a gridpoint.
    Follows NWS GridpointForecastPeriod schema. """

    number: int  # sequential number ID of the forecasted period.
    name: str  # text description of the forecasted period. (e.g. Tuesday Night)

    start_time: str  # ISO8601 timestamp. start time of the forecasted period with offset from UTC (-5).
    # Example output (2022-06-11T01:00:00-05:00).

    end_time: str  # ISO8601 timestamp. end time of the forecasted period with offset from UTC (-5).
    # Example output (2022-06-11T01:00:00-05:00).

    is_daytime: bool  # boolean val on whether its daytime (True) or nighttime (False).

    temperature: Dict[QuantitativeValue]  # sort of deprecated. see gridpoint.py (old) & docs.
    temperature_trend: str  # If not null, indicates a temperature trend that doesn't follow diurnal (day-night) cycles.
    #  only two possible values - "rising" [overnight] & "falling" [during daytime]. NULLABLE.

    wind_speed: Dict[QuantitativeValue]  # sort of deprecated. see gridpoint.py (old) & docs.
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
    elevation: Dict[QuantitativeValue]  # QuantitativeValue. elevation of the forecast area.
    periods: List[GridpointForecastPeriod]  # array of (GridpointForecastPeriod's) forecast periods for the given area.


@dataclass
class GridpointForecastGeoJson:
    """ Class representing detailed forecast data for a gridpoint using advanced geolocation tools.
    Follows NWS GridpointForecastGeoJson schema. """

    context: None  # JsonLdContext. ['@context']
    id: None  # unknown meaning.
    type: str  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry. Need to implement GeoJson library.
    properties: Dict[GridpointForecast]  # returns GridpointForecast object.


@dataclass
class Gridpoint:
    """ Class representing raw forecast data for a gridpoint. Follows NWS Gridpoint schema.
    Depending on the gridpoint, not all fields will be available, and it is unknown at this time which fields those are,
    or the gridpoints where that might occur."""

    temperature: None
    dewpoint: None
    max_temperature: None
    min_temperature: None
    relative_humidity: None
    apparent_temperature: None

    heat_index: None

    wind_chill: None
    sky_cover: None
    wind_direction: None
    wind_speed: None
    wind_gust: None

    weather: None
    hazards: None

    probability_of_precipitation: None
    quantitative_precipitation: None
    ice_accumulation: None
    snowfall_amount: None
    snow_level: None
    ceiling_height: None
    visibility: None
    transport_wind_speed: None
    transport_wind_direction: None

    mixing_height: None
    haines_index: None
    lightning_activity_level: None

    twenty_foot_wind_speed: None
    twenty_foot_wind_direction: None

    primary_swell_height: None
    primary_swell_direction: None
    secondary_swell_height: None
    secondary_swell_direction: None
    wave_period_2: None
    wind_wave_height: None

    dispersion_index: None
    pressure: None

    probability_of_tropical_storm_winds: None
    probability_of_hurricane_winds: None

    potential_of_15mph_winds: None
    potential_of_25mph_winds: None
    potential_of_35mph_winds: None
    potential_of_45mph_winds: None

    potential_of_20mph_wind_gusts: None
    potential_of_30mph_wind_gusts: None
    potential_of_40mph_wind_gusts: None
    potential_of_50mph_wind_gusts: None
    potential_of_60mph_wind_gusts: None

    grassland_fire_danger_index: None
    davis_stability_index: None
    atmospheric_dispersion_index: None
    low_visibility_occurrence_risk_index: None
    stability: None
    red_flag_threat_index: None

