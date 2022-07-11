from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import List, Optional


@dataclass
class Zone:
    context: JsonLdContext = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    id_: str = field(metadata=config(field_name='@id'))  # uri string. given key id_ as id also exists in dataclass.
    type_: str = field(metadata=config(field_name='@type'))  # enum of str value Zone.
    id: str  # NWS Zone Id. It is a UGC identifier for a NWS forecast zone or county.
    type: str  # NWS Zone Type. Enum with 8 potential values - land, marine, forecast, offshore, fire, county, and more.
    name: str
    effective_date: str  # date time in str format
    expiration_date: str  # date time in str format.
    cwa: str  # three letter identifier of a NWS office. For example, BOS for NWS Boston.
    forecast_offices: List[str]  # list of uri strings.
    time_zone: List[str]  # list of time zones of the NWS Zone.
    observation_stations: List[str]  # list of observation stations that contribute to informing the Zone's data.
    radar_station: None = Optional[str]  # Radar station for the Zone. nullable.
    state: Optional[str] = None  # state where the zone is located. Includes 5 US territories, giving 55 possible values. nullable.
    geometry: Optional[str] = None  # GeometryString (nullable: true)


@dataclass_json
@dataclass
class ZoneForecast:
    context: JsonLdContext = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time this forecast was published (not updated???) in ISO8601 format.
    periods: List[PLACEHOLDER]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.
    geometry: Optional[str] = GeometryString  # GeometryString (nullable: true)


@dataclass
class ZoneForecastJsonLd:
    context: JsonLdContext = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time this forecast was published (not updated???) in ISO8601 format.
    periods: List[PLACEHOLDER_2]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.
    geometry: Optional[str] = GeometryString  # GeometryString (nullable: true)
