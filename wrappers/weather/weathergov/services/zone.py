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
    name: str  # description of the area the forecast pertains to (e.g. Northern Erie.)
    effective_date: str  # date time in str format. Date when the zone boundaries were finalized.
    expiration_date: str  # date time in str format. Date when the zone boundaries will expire (do not rely on this.)
    cwa: str  # three letter identifier of a NWS office. For example, BOS for NWS Boston.
    forecast_offices: List[str]  # list of uri strings.
    time_zone: List[str]  # list of time zones of the NWS Zone.
    observation_stations: List[str]  # list of observation stations that contribute to informing the Zone's data.
    radar_station: None = Optional[str]  # Radar station for the Zone. nullable.
    state: Optional[str] = None  # state where the zone is located. Includes 5 US territories, giving 55 possible values. nullable.
    geometry: Optional[str] = None  # GeometryString (nullable: true)


@dataclass
class ZoneForecastPeriod:
    number: int  # sequential number identifier in increasing order. A forecast that is closer in time of occurrence will have a lower number, and forecasts further out will have a higher number.
    name: str  # text description of the time period of the forecast (e.g. This Afternoon, Tomorrow Night)
    detailed_forecast: str  # detailed textual forecast for the relevant period.


@dataclass_json
@dataclass
class ZoneForecast:
    context: JsonLdContext = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time (in ISO8601-str format) this forecast was last updated.
    periods: List[ZoneForecastPeriod]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.
    geometry: Optional[str] = GeometryString  # GeometryString (nullable: true)


@dataclass
class ZoneForecastJsonLd:
    context: JsonLdContext = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    zone: str  # uri (API) link to the zone the forecast pertains to.
    updated: str  # time (in ISO8601-str format) this forecast was last updated.
    periods: List[ZoneForecastPeriod]  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.
    geometry: Optional[str] = GeometryString  # GeometryString (nullable: true)

