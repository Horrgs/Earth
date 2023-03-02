from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Location:
    latitude: float  # latitude of the location.
    longitude: float  # longitude of the location.
    time_zone: str  # time zone of the location.
    title: str  # text description of the Location (e.g. Home)
    formatted_addr: str  # formatted address of the latitude longitude point.

