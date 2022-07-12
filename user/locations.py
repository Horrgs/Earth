from dataclasses import dataclass


@dataclass
class Location:
    latitude: float  # latitude of the location.
    longitude: float  # longitude of the location.
    time_zone: str  # time zone of the location.
    name: str  # text description of the Location (e.g. South Buffalo, Niagara Falls, California)
    services: None  # e.g. NWS, tomorrow.io
    cache: None  # cache of congregated data for location - e.g. weather, air quality, fires.
