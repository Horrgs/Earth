from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from typing import Optional, Dict


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Point:
    id: str = field(metadata=config(field_name='@id'))  # uri for the requested point (e.g. https://api.weather.gov/points/42.85,-78.84
    type: str = field(metadata=config(field_name='@type'))  # enum with only one type: Feature.

    cwa: str  # three letter identifier of the NWS office.
    forecast_office: str  # uri to the NWS office that issues the forecasts. e.g. https://api.weather.gov/offices/BOS

    grid_id: str  # three letter identifer of the NWS office.
    grid_x: int  # x-gridpoint of specified point within the local NWS grid.
    grid_y: int  # y-gridpoint of specified point within the local NWS grid.

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

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PointGeoJson:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    type: str  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry. Need to implement GeoJson library.
    properties: Point  # returns GridpointForecast object.

    id: Optional[str] = None  # unknown meaning.