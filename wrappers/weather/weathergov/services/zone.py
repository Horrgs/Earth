from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json


@dataclass
class Zone:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: str
    id_: None = field(metadata=config(field_name='@io'))  #
    type_: None = field(metadata=config(field_name='@type'))  #
    id: str  # NWS Zone Id. It is a UGC identifier for a NWS forecast zone or county.
    type: str  # NWS Zone Type. Enum with 8 potential values - land, marine, forecast, offshore, fire, county, and more.
    name: str
    effective_date: str
    expiration_date: str
    state: None
    cwa: None
    forecast_offices: None
    time_zone: None
    observation_stations: None
    radar_station: str  # nullable.


@dataclass_json
@dataclass
class ZoneForecast:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.


@dataclass
class ZoneForecastJsonLd:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.