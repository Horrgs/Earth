import json, requests, enum
from wrappers.weather.weathergov.services.gridpoint import GridpointForecastGeoJson

# module for request & request-adjacent methods.




"""
RequestMethod - the Hypertext Transfer Protocol (HTTP) has a number of methods - GET, HEAD, CONNECT, POST, etc,. 

The library responsible for initiating HTTP requests uses methods (e.g. requests.get() ) or 
strings (requests.request('GET') ) to specify the HTTP method. Here, we create an Enum class to specify the request type,
and pass that value to the library.

Note: there are HTTP methods not supplied by the Enum class (e.g. HEAD)
"""


class RequestMethod(enum.Enum):
    GET = "GET"  # send HTTP request via GET method.
    POST = "POST"  # send HTTP request via POST method.
    PUT = "PUT"  # send HTTP request via PUT method.
    DELETE = "DELETE"  # send HTTP request via DELETE method.


# method to check if web API is available. 200 HTTP is 'OK' status.
def check_status(url, method: RequestMethod):
    pass


# TODO: check what data is in request.
# TODO: check if 'try' can end at specified point.
# TODO: see if it's possible to remove first if statement.
def get(url, method: RequestMethod, payload=None):
    headers = {
        'User-Agent': 'https://www.github.com/Horrgs/Earth',
        'Feature-Flag': 'forecast_temperature_qv'
    }
    try:
        if payload is not None:  # check if a payload is specified for HTTP request.
            req = requests.request(method=method.value, url=url, headers=headers, data=payload)  # valid payload to send with HTTP request.
        else:
            req = requests.request(method.value, headers=headers, url=url)  # no payload to send, send remaining info.
        # TODO: check if try can end here.

        if req.status_code != 200:
            pass  # raise error of bad response.
        return req.json()  # returns json (dict) formatted response of request.
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except ValueError as e:
        print(e)


# TODO: create cache system.