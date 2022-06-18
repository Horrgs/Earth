from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
import json
import typing


class Zone:
    pass


@dataclass_json
@dataclass
class ZoneForecast:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.


@dataclass
class ZoneForecastGeoJson:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    id: None  # unknown meaning.
    type: None  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry.
    properties: None  # ZoneForecast object.


@dataclass
class ZoneForecastJsonLd:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.