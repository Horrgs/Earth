from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from typing import Optional


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Point:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    id: str = field(metadata=config(field_name='@id'))
    type: str = field(metadata=config(field_name='@type'))

    cwa: str  # three letter identifier of the NWS office.
    forecast_office: str  #

    grid_id: str  # three letter identifer of the NWS office.
    grid_x: int  # x-coordinate in the grid from the NWS office
    grid_y: int  # y-coordinate in the grid from the NWS office.

    forecast: str  # uri to the GridpointForecast of the specified point.
    forecast_hourly: str  # uri to the GridpointForecastHourly of the specified point.
    forecast_grid_data: str  # uri to the raw GridpointForecast data of the specified point.

    observation_stations: str  # uri to the relevant observation stations
    relative_location: None
    forecast_zone: str  # uri to the relevant forecast zone

    county: str  # uri to the relevant county zone
    fire_weather_zone: str  # uri to the relevant fire weather zone.

    time_zone: str  # time zone of specified point.
    radar_station: str  # radar provider of specified point.
    geometry: Optional[str] = None  # GeometryString. NULLABLE.


