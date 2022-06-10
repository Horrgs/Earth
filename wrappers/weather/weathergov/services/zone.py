from dataclasses import dataclass
import json
import typing


class Zone:
    pass


@dataclass
class ZoneForecast:
    context: None  # JsonLdContext.
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.


@dataclass
class ZoneForecastGeoJson:
    context: None  # JsonLdContext.
    id: None  # unknown meaning.
    type: None  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry.
    properties: None  # ZoneForecast object.


@dataclass
class ZoneForecastJsonLd:
    context: None  # JsonLdContext.
    geometry: None  # GeometryString (nullable: true)
    zone: None  # uri (API) link to the zone the forecast pertains to.
    updated: None  # time this forecast was published (not updated???) in ISO8601 format.
    periods: None  # array of (generic?) objects of forecast periods (of type dict) with keys - number, name & detailedForecast.