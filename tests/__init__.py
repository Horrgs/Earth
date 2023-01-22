weather = main.get_weather(point=[42.9638, -58.9382])

twelve_hr = weather.basic
hourly = weather.hourly

temp = hourly[0].temperature
apparent = hourly[0].apparent
humidity = hourly[0].humidity
fire_index = hourly[0].fire_index  # hm. fire data from weather service when we have fire service.

weather = main.get_weather(address=['1600 Amphitheatre parkway'])  # convert to lat/lng (basically Point)
temp = weather.hourly[0].temperature

weather = main.get_weather(region=['NY'])
weather = main.get_weather(region=['Buffalo, NY'])

alerts = main.get_alerts(point=[42.95, 27.82], active=True)  # make sure that non-active but future alerts are included.

fire = main.get_fires(region=['CA', 'CO'], active=True)  # returns active fires in CA & CO.


def weather_test(service, location):
    if service.equals('forecast'):
        if location.equals('raw'):
            fetch = get('forecast', 'raw', '80,20')  # return GridpointForecast
            fetch = get('forecast', 'raw', '80,20', 'hourly')  # return GridpointForecastHourly
            pass
        elif location.equals('zone'):
            pass  # return ZoneForecast
        elif location.equals('gridpointraw'):  # will need an actual name.
            pass # return Gridpoint
        else:
            pass
    elif service.equals('alerts'):
        pass
    pass


def get_weather(**kwargs):
    if any(['point']) in kwargs:
        pass
    else:
        pass  # throw error as no location is specified.


main.get_weather(address='1600 Amphitheatre Pkwy, Mountain View, CA 94043')  # convert to lat/lng, use NWS Point, find Gridpoint.



main.get_weather(region='NY')  # ?
main.get_weather(region='Buffalo, NY')  # ?
main.get_weather(region='New York City, NY')  # ?
