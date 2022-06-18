from dataclasses import dataclass
from utils.req import send, RequestMethod

@dataclass
class Point:
    pass


def get_grid_info(point):
    url = "https://api.weather.gov/points/{0},{1}"
    point = [str(p).strip() for p in point]
    url = url.format(*point)
    push_req = send(url, RequestMethod.GET)
    push_req = push_req['properties']
    response = {
        'gridId': push_req['gridId'],
        'gridX': push_req['gridX'],
        'gridY': push_req['gridY']
    }
    return response


def get_weather(point):
    url = "https://api.weather.gov/gridpoints/{0}/{1},{2}/forecast"
    grid_info = get_grid_info(point)
    url = url.format(grid_info['gridId'], grid_info['gridX'], grid_info['gridY'])
    push_req = send(url, RequestMethod.GET)
    print(push_req)


get_weather([42.8864, -78.8784])

