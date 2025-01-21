from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from config import config
import json
from typing import List
import logging


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Service:
    name: str  # name of the service (i.e. weather.gov)
    endpoint: str  # endpoint for the services' API.
    enabled: bool  # method for enabling/disabling a servce
    api_key: str = None  # api key for the service. None if no API key required.