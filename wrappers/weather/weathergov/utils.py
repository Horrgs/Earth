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
