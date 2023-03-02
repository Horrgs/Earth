from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json, LetterCase
from typing import Union, List

# from .services.alerts import Alert
# from .services.gridpoint import Gridpoint, GridpointForecast
# from services.zone import Zone, ZoneForecast


class QuantitativeValue:
    # NWS schema for quantitative values (e.g. temperature)
    # The NWS QuantitativeValue Schema is a modified version of https://schema.org/QuantitativeValue

    def __init__(self, item):
        self.value = item['value']  # measured value (e.g. temperature)
        self.max_value = item['maxValue']  # maximum value in a set of measurements.
        self.min_value = item['minValue']  # minimum value in a set of measurements.
        self.unit_code = item['unitCode']  # String denoting the unit of measurement. More detail at weather.gov

        self.quality_control = item['qualityControl']  # per NWS, "For values in observation records,
        # the quality control flag from the MADIS system.


# Schema types

class GridpointQuantitativeValueLayer:

    def __init__(self, item):
        self.uom = item['uom']
        self.values = item['values']


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GeoJsonFeature:
    """ Class representing data for a weather.gov request to Zone, Gridpoint, etc,. in GeoJson format..
        Follows NWS *GeoJson schema. """

    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext. ['@context']
    id: str  # uri string. unknown meaning.
    type: str  # unknown meaning. Only one possible value: "Feature."
    geometry: None  # GeoJsonGeometry. Need to implement GeoJson library.

    # properties: None
    # properties: Union[Alert, Gridpoint, GridpointForecast, Zone, ZoneForecast]
    # depending on the request, properties can take the value of Alert, Gridpoint, GridpointForecast, and more.


@dataclass
class CollectionGeoJson:
    context: None = field(metadata=config(field_name='@context'))  # JsonLdContext ['@context']
    type: str  # unknown meaning. Only one possible value: "FeatureCollection"
    features: List[GeoJsonFeature]  # list of GeoJsonFeatures forming a collection.


@dataclass
class AlertCollection:
    title: str  # title describing the Alert collection.
    updated: str  # last time a change was made to the collection (date time in string format)
    pagination: None  # links for retrieving more data.


@dataclass  # it's unknown at this time how/if to implement JsonLd.
class JsonLd:
    pass