from dataclasses import dataclass
from typing import List, Optional

# API documentation: https://www.weather.gov/documentation/services-web-api


@dataclass
class Alert:
    """ Class representing Alert schema from NWS. Contains details on an issued alert."""
    id: str  # (id)entifier of the NWS issued alert.
    area_desc: str  # description of the area affected by the NWS Alert.
    geocode: PLACEHOLDER_  # per NWS, "Lists of codes for NWS public zones and counties affected by the alert."
    affected_zones: List[str]  # list of links for all the affected zones for the NWS alert of interest.
    references: List[PLACEHOLD]  # list of prior NWS-issued alerts that this alert update or replaces.

    sent: str  # ISO8601 timestamp. time the alert was sent (NOT the time the alert is in effect.)
    effective: str  # ISO8601 timestamp. the time the alert is in effect.
    expires: str  # ISO8601 timestamp. time when the issued alert is set to expire (i.e. alert no longer in affect.)

    status: str  # Status of the NWS-issued alert (i.e. Actual [alert], Exercise, Test)
    message_type: str  # Subject message for the NWS-issued alert (i.e. Update [alert], Cancel [alert])
    category: str  # Code denoting the category of the alert message (i.e. Met(eorological), Geo(logical), Fire)
    severity: str  # severity of the NWS-issued alert (e.g. Extreme, Severe)
    certainty: str  # certainty in the subject event of the NWS-issued alert (i.e. observed [thunder], possible [thunder])
    urgency: str  # urgency of the NWS-issued alert (e.g. Immediate, Expected)
    event: str  # subject of the NWS alert (e.g. Flood Watch, Severe Thunderstorm Warning)

    sender: str  # email address of NWS webmaster.
    sender_name: str  # author of the original alert message.

    description: str  # detailed description of the NWS-issued alert, akin to 'body' of an article.

    response: str  # code denoting the type of action to be taken by target audience (i.e. Shelter, Evacuate). Enum. Corresponds to responseType in CAP specification.
    instruction: Optional[str] = None  # if given (i.e. not null), a text description of actions to be taken by alert receivers. (i.e. shelter in place, seek higher ground)
    headline: Optional[str] = None  # text 'description' indicating nature of the NWS-issued alert, akin to newspaper article headline
    onset: Optional[str] = None  # ISO8601 timestamp. expected time of the beginning of the subject event of the alert message.
    ends: Optional[str] = None  # ISO8601 timestamp. expected time of the end of the subject event of the alert message.
