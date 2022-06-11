import json, requests, enum

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


"""
method: send - send HTTP request using specifying parameters. 

parameter: url - the URL string destination for the HTTP request, value of a string (e.g. 'http://www.google.com')
parameter: method - the HTTP method to use in the HTTP request, value of a RequestMethod enum (e.g. RequestMethod.GET)
parameter: payload - 
"""

# TODO: check what data is in request.
# TODO: check if 'try' can end at specified point.
# TODO: see if it's possible to remove first if statement.
def send(url, method: RequestMethod, payload=None):
    try:
        # prepare & send HTTP request.

        # TODO: see if it's possible to remove if statement.
        if payload is not None:  # check if a payload is specified for HTTP request.
            req = requests.request(method.value, url, data=payload)  # valid payload to send with HTTP request.
        else:
            req = requests.request(method.value, url)  # no payload to send, send remaining info.
        print(req.text)
        # TODO: check if try can end here.

        # load response from HTTP request.

        """response = {}  # create empty dict for the response from the request.
        for item in json.loads(req.text):  # loop over each item in the Response from the Request.
            response[item['Text']] = int(item['Value'])  # place item in the response dict.
        response = dict(sorted(response.items(), key=lambda obj: obj[1]))  # sort response dict based on X.
        return response  # return response dict. """

        return req.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except ValueError as e:
        print(e)

# method to check if web API is available. 200 HTTP is 'OK' status.
def check_status(url, method: RequestMethod):
    pass


# TODO: create cache system.