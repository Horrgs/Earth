import dataclasses
import json
import typing


class Zone:
    pass


class ZoneForecast:

    def __init__(self, response):
        self.context = response['@context']
        self.geometry = response['geometry']
        self.zone = response['zone']
        self.updated = response['updated']
        self.periods = response['periods']


class ZoneForecastGeoJson:

    def __init__(self, response):
        self.context = response['@context']
        self.id = response['id']
        self.type = response['type']
        self.geometry = response['geometry']
        self.properties = response['properties']


class ZoneForecastJsonLd:

    def __init__(self, response):
        self.context = response['@context']
        self.geometry = response['geometry']
        self.zone = response['zone']
        self.updated = response['updated']
        self.periods = response['periods']