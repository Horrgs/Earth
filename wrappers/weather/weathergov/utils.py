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

class Collection:

    def __init__(self, response):
        self.context = response['@context']  # JsonLdContext.
        self.type = response['type']  # enum of type string, with only value being FeatureCollection.
        self.features = response['features']  # unkown.
        self.title = response['title']  # title describing the collection.
        self.updated = response['updated']  # last time a modification to the collection occurred.
        self.pagination = response['pagination']  # more results


class GeoJson:

    def __init__(self, response):
        self.context = response['@context']  # JsonLdContext.
        self.id = response['id']  # string uri
        self.type = response['type']  # enum of type string, with only value being 'Feature'.

        self.geometry = response['geometry']  # GeoJsonGeometry.
        # self.properties = response['properties']
        # technically in schema, but unsure how we'll incorporate it in class inheritances
        # bc for alerts/geo+json, properties is of type Alert, whereas for forecast it is of type
        # GridpointForecast, etc,.


class JsonLd:

    def __init__(self):
        pass


# class Foo is labeled as a placeholder, as its unknown how Zone differs from ZoneGeoJson.
"""class Foo:
    pass

"""