from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json, LetterCase
from typing import Union

from services.alerts import Alert
from services.gridpoint import Gridpoint, GridpointForecast
from services.zone import Zone, ZoneForecast
from services.point import Point


class QuantitativeValue:
    # NWS schema for quantitative values (e.g. temperature)
    # The NWS QuantitativeValue Schema is a modified version of https://schema.org/QuantitativeValue

    def __init__(self, item):
        self.value = item['value']  # measured value (e.g. temperature)
        self.max_value = item['maxValue']  # maximum value in a set of measurements.
        self.min_value = item['minValue']  # minimum value in a set of measurements.
        self.unit_code = item['unitCode']  # String denoting the unit of measurement. More detail at weather.gov

        self.quality_control = item['qualityControl']  # per NWS, "For values in observation records,
        # the quality control flag from the MADIS system."


# Schema types

class GridpointQuantitativeValueLayer:

    def __init__(self, item):
        self.uom = item['uom']
        self.values = item['values']


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GeoJson:
    """ Class representing data for a weather.gov request to Zone, Gridpoint, etc,. in GeoJson format..
        Follows NWS *GeoJson schema. """

    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    id: str  # uri string. unknown meaning.
    type: str  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry. Need to implement GeoJson library.

    properties: Union[Alert, Gridpoint, GridpointForecast, Zone, ZoneForecast]
    # depending on the request, properties can take the value of Alert, Gridpoint, GridpointForecast, and more.


@dataclass
class JsonLd:
    pass


@dataclass
class Collection:
    context: None  # JsonLdContext.
    type: None  # enum of type string, with only value being FeatureCollection.
    features: None  # unknown.
    title: None   # title describing the collection.
    updated: None  # last time a modification to the collection occurred.
    pagination: None  # more results


# class Foo is labeled as a placeholder, as its unknown how Zone differs from ZoneGeoJson.
"""class Foo:
    pass

"""