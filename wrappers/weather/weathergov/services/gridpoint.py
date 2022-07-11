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

    temperature: Optional[GridpointQuantitativeValueLayer] = None  # air temperature in preferred units (F/C)

    dewpoint: Optional[GridpointQuantitativeValueLayer] = None  # dewpoint temperature in preferred units (F/C).
    # the dewpoint is the temperature that air needs to be cooled to achieve a relative humidity of 100%.

    max_temperature: Optional[GridpointQuantitativeValueLayer] = None  # highest temperature
    min_temperature: Optional[GridpointQuantitativeValueLayer] = None  # lowest temperature
    relative_humidity: Optional[GridpointQuantitativeValueLayer] = None  #  The relative humidity is the amount of water vapor in the air relative to the amount needed to achieve saturation.
    apparent_temperature: Optional[GridpointQuantitativeValueLayer] = None  # apparent temperature is what is perceived by humans. Takes into account the air temperature, wind speed, and relative humidity.

    heat_index: Optional[GridpointQuantitativeValueLayer] = None  # related to apparent temperature, this is the air temperature combined with relative humidity. Informative for high-temperature scenarios.

    wind_chill: Optional[GridpointQuantitativeValueLayer] = None  # related to apparent temperature, this is the temperature perceived by humans on their exposed skin due to the combined air temperature & wind-speed.

    # when the apparent temperature is lower than the air temperature, wind chill is used. When apparent temperature is
    #  higher than the air temperature, the heat index is used.

    sky_cover: Optional[GridpointQuantitativeValueLayer] = None  # percent of the sky that is obscured, typically by clouds. A clear sunny day will have 0% sky cover.
    wind_direction: Optional[GridpointQuantitativeValueLayer] = None  # the prevalent (dominant) direction the wind is blowing.
    wind_speed: Optional[GridpointQuantitativeValueLayer] = None  # the sustained wind speeds, typically over an interval of time.
    wind_gust: Optional[GridpointQuantitativeValueLayer] = None  # a brief increase in the speed of the wind.

    weather: Optional[GridpointQuantitativeValueLayer] = None
    hazards: Optional[GridpointQuantitativeValueLayer] = None

    probability_of_precipitation: Optional[GridpointQuantitativeValueLayer] = None  # likelihood for any precipitation (snow, sleet, ice, hail, rain)
    quantitative_precipitation: Optional[GridpointQuantitativeValueLayer] = None  # total amount of precipitation expected to fall (precipitate)
    ice_accumulation: Optional[GridpointQuantitativeValueLayer] = None  # total amount of ice (that has accumulated) on the ground, i.e. 1" of freezing rain freezing into ice.
    snowfall_amount: Optional[GridpointQuantitativeValueLayer] = None  # total amount of snow that has fallen.
    snow_level: Optional[GridpointQuantitativeValueLayer] = None  # an elevation marker. Above this elevation, snow will precipitate, and below the elevation, other forms of precipitation will precipitate (freezing rain, rain)
    ceiling_height: Optional[GridpointQuantitativeValueLayer] = None  # the height of the base of the lowest clouds that cover more than half the sky, relative to the ground (not sea level.)
    visibility: Optional[GridpointQuantitativeValueLayer] = None  # farthest distance an object is still discernable. Or, the distance at which objects become no longer discernable.
    transport_wind_speed: Optional[GridpointQuantitativeValueLayer] = None  # the wind speed in the mixing layer of the atmosphere. Relevant for fire danger.
    transport_wind_direction: Optional[GridpointQuantitativeValueLayer] = None  # the direction of the wind in the mixing layer of the atmosphere. Relevant for fire danger.

    mixing_height: Optional[GridpointQuantitativeValueLayer] = None  # height above the surface where atmospheric mixing occurs. In other words, it's the height where a pollutant such as fire smoke can be dispersed. Relevant for fire danger.
    haines_index: Optional[GridpointQuantitativeValueLayer] = None  # a weather index that quantifies the potential for a dry, unstable air mass to contribute to the development of large or erratic wildfires. Relevant for fire danger.
    lightning_activity_level: Optional[GridpointQuantitativeValueLayer] = None  # abbreviated as LAL. Levels trnage from 1-6, with 1 being no thunderstorms. For more details on the scale, see: https://graphical.weather.gov/definitions/defineLAL.html

    twenty_foot_wind_speed: Optional[GridpointQuantitativeValueLayer] = None  # average sustained wind speed over a ten minute period and measured twenty feet above nearby vegetation. Relevant for fire danger.
    twenty_foot_wind_direction: Optional[GridpointQuantitativeValueLayer] = None  # average sustained wind direction for the twenty foot wind wind standard.

    primary_swell_height: Optional[GridpointQuantitativeValueLayer] = None  #
    primary_swell_direction: Optional[GridpointQuantitativeValueLayer] = None  #
    secondary_swell_height: Optional[GridpointQuantitativeValueLayer] = None  #
    secondary_swell_direction: Optional[GridpointQuantitativeValueLayer] = None  #
    wave_period_2: Optional[GridpointQuantitativeValueLayer] = None  #
    wind_wave_height: Optional[GridpointQuantitativeValueLayer] = None  #

    dispersion_index: Optional[GridpointQuantitativeValueLayer] = None  #
    pressure: Optional[GridpointQuantitativeValueLayer] = None

    probability_of_tropical_storm_winds: Optional[GridpointQuantitativeValueLayer] = None
    probability_of_hurricane_winds: Optional[GridpointQuantitativeValueLayer] = None

    potential_of_15mph_winds: Optional[GridpointQuantitativeValueLayer] = None  # likelihood for sustained wind speeds of 15mph (0-1).
    potential_of_25mph_winds: Optional[GridpointQuantitativeValueLayer] = None  # likelihood for sustained wind speeds of 30mph(0-1).
    potential_of_35mph_winds: Optional[GridpointQuantitativeValueLayer] = None  # similar to above
    potential_of_45mph_winds: Optional[GridpointQuantitativeValueLayer] = None  # similar to above

    potential_of_20mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None  # likelihood for wind gusts of 20mph (0-1.)
    potential_of_30mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None  # similar to above
    potential_of_40mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None  # similar to above
    potential_of_50mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None  # similar to above
    potential_of_60mph_wind_gusts: Optional[GridpointQuantitativeValueLayer] = None  # similar to above

    grassland_fire_danger_index: Optional[GridpointQuantitativeValueLayer] = None  # Relevant to fire danger. An index developed to describe the rate of grassland fire spread. 0 describes a low fire threat, while higher scores (up to 50 and more) describes higher fire threats. See more: https://www.weather.gov/ict/GFDI_FAQ
    davis_stability_index: Optional[GridpointQuantitativeValueLayer] = None  # Relevant for tropical storms. An index developed to describe the stability (or lack thereof) of a weather system. It is a scale that measures the temperature difference between the forecasted max temperature (in C) and the temperature (in C) at the atmospheric level where pressure is 850mb. For more:  https://graphical.weather.gov/definitions/defineDSI.html
    atmospheric_dispersion_index: Optional[GridpointQuantitativeValueLayer] = None  # Relevant to fire danger. Index scale that quantifies the 20 foot wind standard. Quantifies ability for an air-mass to disperse pollutants, primarly fire smoke. For more: https://graphical.weather.gov/definitions/defineADI.html
    low_visibility_occurrence_risk_index: Optional[GridpointQuantitativeValueLayer] = None  # Relevant for visibility. Scale used to quantify likelihood for low visibility conditions to form. See more: https://www.weather.gov/jan/fire_weather_lvori
    stability: Optional[GridpointQuantitativeValueLayer] = None  #
    red_flag_threat_index: Optional[GridpointQuantitativeValueLayer] = None  #

