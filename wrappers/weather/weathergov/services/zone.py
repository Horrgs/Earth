from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import List


@dataclass
class Zone:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: str  # GeometryString (nullable: true)
    id_: None = field(metadata=config(field_name='@id'))  # uri string. given key id_ as id also exists in dataclass.
    type_: None = field(metadata=config(field_name='@type'))  # enum of str value Zone.
    id: str  # NWS Zone Id. It is a UGC identifier for a NWS forecast zone or county.
    type: str  # NWS Zone Type. Enum with 8 potential values - land, marine, forecast, offshore, fire, county, and more.
    name: str
    effective_date: str  # date time in str format
    expiration_date: str  # date time in str format.
    state: str  # state where the zone is located. Includes 5 US territories, giving 55 possible values. nullable.
    cwa: str  # three letter identifier of a NWS office. For example, BOS for NWS Boston.
    forecast_offices: List[str]  # list of uri strings.
    time_zone: List[str]  # list of time zones of the NWS Zone.
    observation_stations: List[str]  # list of observation stations that contribute to informing the Zone's data.
    radar_station: str  # Radar station for the Zone. nullable.


@dataclass_json
@dataclass
class ZoneForecast:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: str  # GeometryString (nullable: true)
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time this forecast was published (not updated???) in ISO8601 format.
    periods: List[PLACEHOLDER]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.


@dataclass
class ZoneForecastJsonLd:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: None  # GeometryString (nullable: true)
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time this forecast was published (not updated???) in ISO8601 format.
    periods: List[PLACEHOLDER_2]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.