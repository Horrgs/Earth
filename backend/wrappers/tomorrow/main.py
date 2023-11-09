from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from typing import Optional


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Core:

    temperature: float  # temperature at 2m
    temperature_apparent: float  # perceived (human) temperature, combining air temp, rel. humidity, and wind speed @ 2m
    dew_point: float  # temperature at which the air would become saturatedd (at 2m.)
    humidity: float  # concentration of water vapor as a percent (relative humidity)
    wind_speed: float  #
    wind_direction: Optional[float]  # direction of the wind, measured in degrees. Can be null.
    wind_gust: float  # maximum burst speed of the wind, "usually less than 20 seconds" (@ 10m.)
    pressure_surface_level: float  # atmospheric pressure as recorded at surface elevation
    pressure_sea_level: float  # atmospheric pressure as recorded at sea level.
    precipitation_intensity: float  # "instantatn
    rain_intensity: float
    freezing_rain_intensity: float
    snow_intensity: float
    sleet_intensity: float
    precipitation_probability: float
    precipitation_type: int
    rain_accumulation: float
    snow_accumulation: float
    snow_accumulation_lwe: float
    snow_depth: float
    sleet_accumulation: float
    sleet_accumulation_lwe: float
    ice_accumulation: float
    ice_accumulation_lwe: float
    sunrise_time: None
    sunset_time: None
    visibility: float
    cloud_cover: float
    cloud_base: Optional[float]
    cloud_ceiling: Optional[float]
    moon_phase: int
    uv_index: int
    uv_health_concern: int
    gdd_10_to_30: float
    gdd_10_to_31: float
    gdd_08_to_30: float
    gdd_03_to_25: float
    evapotranspiration: float
    weather_code_full_day: int
    weather_code_day: int
    weather_code_night: int
    weather_code: int