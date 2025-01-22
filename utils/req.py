import enum
import requests
import json

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


# TODO: check what data is in request.
# TODO: check if 'try' can end at specified point.
# TODO: see if it's possible to remove first if statement.
def req(url, method: RequestMethod, payload=None):
    print(url)

    headers = {  # TODO: currently manually building headers, and doesn't handle multiple services. needs to handle each service & automatically built.
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'en-US,en;q = 0.5',
        'Connection': 'keep-alive',
        'Feature-Flag': 'forecast_temperature_qv',
        'Host': 'api.weather.gov',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q = 0.8'
    }

    try:
        req = requests.request(method=method.value, url=url, headers=headers, data=payload)  # valid payload to send with HTTP request.
        # TODO: check if try can end here.

        if req.status_code != 200:
            pass  # raise error of bad response.
        print(json.loads(req.content))
        return req  # returns the request object.
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except ValueError as e:
        print(e)


# TODO: create cache system.

