from wrappers.weather.weathergov.utils import QuantitativeValue, GridpointQuantitativeValueLayer
from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from typing import Optional, List, Dict


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GridpointForecastPeriod:
    """ Class representing detailed forecast data for a specific time period for a raw.
    Follows NWS GridpointForecastPeriod schema. """

    number: int  # sequential number ID of the forecasted period.
    name: str  # text description of the forecasted period. (e.g. Tuesday Night)

    start_time: str  # ISO8601 timestamp. start time of the forecasted period with offset from UTC (-5).
    # Example output (2022-06-11T01:00:00-05:00).

    end_time: str  # ISO8601 timestamp. end time of the forecasted period with offset from UTC (-5).
    # Example output (2022-06-11T01:00:00-05:00).

    is_daytime: bool  # boolean val on whether its daytime (True) or nighttime (False).

    # temperature: QuantitativeValue  # sort of deprecated. see raw.py (old) & docs.
    temperature: int
    #  only two possible values - "rising" [overnight] & "falling" [during daytime]. NULLABLE.

    # wind_speed: QuantitativeValue  # sort of deprecated. see raw.py (old) & docs.
    wind_speed: str
    wind_direction: str  # text description indicating wind direction (e.g. ESE for east-southeast)

    icon: str  # Technically deprecated, but still appears in response.
    # icon graphic representing the forecast (e.g. sun for clear skies/sunny weather).

    short_forecast: str  # short text summary of the forecast for the given forecast period.
    detailed_forecast: str  # long, detailed summary of the forecast for the given forecast period.

    wind_gust: Optional[str] = None  # sort of deprecated. see raw.py (old) & docs.
    temperature_trend: Optional[str] = None  # If not null, indicates a temperature trend that doesn't follow diurnal (day-night) cycles.


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GridpointForecast:
    """ Class representing detailed forecast data for a raw. Follows NWS GridpointForecast schema. """

    units: str  # Specifies the units that are used in the text parts of the forecast.
    # Only two possible values - "us" & "si"

    forecast_generator: str  # the generator used to create the text-based forecast. Only relevant for debugging.
    generated_at: str  # ISO8601 timestamp. The timestamp the forecast was generated.
    update_time: str  # ISO8601 timestamp. The timestamp the forecast was generated.
    valid_times: str  # ISO8601 timestamp.
    elevation: Dict  # QuantitativeValue. elevation of the forecast area.
    periods: List[GridpointForecastPeriod]  # array of (GridpointForecastPeriod's) forecast periods for the given area.

    # context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: Optional[str] = None  # GeometryString. NULLABLE.


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Gridpoint:
    """ Class representing raw forecast data for a raw. Follows NWS Gridpoint schema.
    Depending on the raw, not all fields will be available, and it is unknown at this time which fields those are,
    or the gridpoints where that might occur."""

    temperature: Optional[GridpointQuantitativeValueLayer] = None
    dewpoint: Optional[GridpointQuantitativeValueLayer] = None
    max_temperature: Optional[GridpointQuantitativeValueLayer] = None
    min_temperature: Optional[GridpointQuantitativeValueLayer] = None
    relative_humidity: Optional[GridpointQuantitativeValueLayer] = None
    apparent_temperature: Optional[GridpointQuantitativeValueLayer] = None

    heat_index: Optional[GridpointQuantitativeValueLayer] = None

    wind_chill: Optional[GridpointQuantitativeValueLayer] = None
    sky_cover: Optional[GridpointQuantitativeValueLayer] = None
    wind_direction: Optional[GridpointQuantitativeValueLayer] = None
    wind_speed: Optional[GridpointQuantitativeValueLayer] = None
    wind_gust: Optional[GridpointQuantitativeValueLayer] = None

    weather: Optional[GridpointQuantitativeValueLayer] = None
    hazards: Optional[GridpointQuantitativeValueLayer] = None

    probability_of_precipitation: Optional[GridpointQuantitativeValueLayer] = None
    quantitative_precipitation: Optional[GridpointQuantitativeValueLayer] = None
    ice_accumulation: Optional[GridpointQuantitativeValueLayer] = None
    snowfall_amount: Optional[GridpointQuantitativeValueLayer] = None
    snow_level: Optional[GridpointQuantitativeValueLayer] = None
    ceiling_height: Optional[GridpointQuantitativeValueLayer] = None
    visibility: Optional[GridpointQuantitativeValueLayer] = None
    transport_wind_speed: Optional[GridpointQuantitativeValueLayer] = None
    transport_wind_direction: Optional[GridpointQuantitativeValueLayer] = None

    mixing_height: Optional[GridpointQuantitativeValueLayer] = None
    haines_index: Optional[GridpointQuantitativeValueLayer] = None
    lightning_activity_level: Optional[GridpointQuantitativeValueLayer] = None

    twenty_foot_wind_speed: Optional[GridpointQuantitativeValueLayer] = None
    twenty_foot_wind_direction: Optional[GridpointQuantitativeValueLayer] = None

    primary_swell_height: Optional[GridpointQuantitativeValueLayer] = None
    primary_swell_direction: Optional[GridpointQuantitativeValueLayer] = None
    secondary_swell_height: Optional[GridpointQuantitativeValueLayer] = None
    secondary_swell_direction: Optional[GridpointQuantitativeValueLayer] = None
    wave_period_2: Optional[GridpointQuantitativeValueLayer] = None
    wind_wave_height: Optional[GridpointQuantitativeValueLayer] = None

    dispersion_index: Optional[GridpointQuantitativeValueLayer] = None
    pressure: Optional[GridpointQuantitativeValueLayer] = None

    probability_of_tropical_storm_winds: Optional[GridpointQuantitativeValueLayer] = None
    probability_of_hurricane_winds: Optional[GridpointQuantitativeValueLayer] = None

    potential_of_15mph_winds: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_25mph_winds: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_35mph_winds: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_45mph_winds: Optional[GridpointQuantitativeValueLayer] = None

    potential_of_20mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_30mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_40mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_50mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None
    potential_of_60mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None

    grassland_fire_danger_index: Optional[GridpointQuantitativeValueLayer] = None
    davis_stability_index: Optional[GridpointQuantitativeValueLayer] = None
    atmospheric_dispersion_index: Optional[GridpointQuantitativeValueLayer] = None
    low_visibility_occurrence_risk_index: Optional[GridpointQuantitativeValueLayer] = None
    stability: Optional[GridpointQuantitativeValueLayer] = None
    red_flag_threat_index: Optional[GridpointQuantitativeValueLayer] = None

