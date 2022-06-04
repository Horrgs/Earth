from needaname import req
from needaname import QuantitativeValue


"""
Get forecast for given NWS station (station ID, 0). Specify the 2.5km x 2.5km grid point for station.
additional args available.

def get_forecast(location):
    url = "https://api.weather.gov/gridpoints/{0}/{1}/forecast{2}"  # station id, grid_loc, additional args.
    url = url.format(location['id'], location['grid_location'], '')
    fetch_forecast = req.send(url, req.RequestMethod.GET, None)
    for item in fetch_forecast['periods']:
        p = Period(item)"""