# API documentation: https://www.weather.gov/documentation/services-web-api


class Alert:  # this class follows the Alert schema published by NWS.

    def __init__(self, alert):
        # creates [NWS] alert object with the respective attribute
        self.alert = alert

        self.id = self.alert['id']  # fetch the unique ID for the specific alert issued by NWS
        self.alert_desc = self.alert['alertDesc']  # description of the area affected by the alert
        self.geocode = self.alert['geocode']  # list of NWS zones & U.S. counties affected by NWS-issued alert, followed by .
        self.affected_zones = self.alert['affectedZones']  # Per NWS, "An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification."
        self.references = self.alert['references']  # list of prior NWS-issued alerts that this alert update or replaces.

        self.sent = self.alert['sentTime']  # time the alert was sent (NOT the time the alert is in effect)
        self.effective = self.alert['effective']  # the time the alert is in effect
        self.onset = self.alert['onset']  # expected time of the beginning of the subject event of the alert message.
        self.expires = self.alert['expires']  # time when the issued alert is set to expire (i.e. alert no longer in affect)
        self.ends = self.alert['ends']  # expected time of the end of the subject event of the alert message.

        self.status = self.alert['status']  # Status of the NWS-issued alert (i.e. Actual [alert], Exercise, Test)
        self.message_type = self.alert['messageType']  # Subject message for the NWS-issued alert (i.e. Update [alert], Cancel [alert])
        self.category = self.alert['category']  # Code denoting the category of the alert message (i.e. Met(eorological), Geo(logical), Fire)
        self.severity = self.alert['severity']  # severity of the NWS-issued alert (e.g. Extreme, Severe)
        self.certainty = self.alert['certainty']  # certainty in the subject event of the NWS-issued alert (i.e. observed [thunder], possible [thunder])
        self.urgency = self.alert['urgency']  # urgency of the the NWS-issued alert (e.g. Immediate, Expected)
        self.event = self.alert['event']  # subject of the NWS alert (e.g. Flood Watch, Severe Thunderstorm Warning)

        self.sender = self.alert['sender']  # email address of NWS webmaster.
        self.senderName = self.alert['senderName']  # author of the original alert message.

        self.headline = self.alert['headline']  # text 'description' indicating nature of the NWS-issued alert, akin to newspaper article headline
        self.description = self.alert['description']  # detailed description of the NWS-issued alert, akin to 'body' of an article.
        self.instruction = self.alert['instruction']  # if given (i.e. not null), a text description of actions to be taken by alert receivers. (i.e. shelter in place, seek higher ground)
        self.response = self.alert['response']  # code denoting the type of action to be taken by target audience (i.e. Shelter, Evacuate). Enum. Corresponds to responseType in CAP specification.

        self.response = self.alert['response']

    # Unsure if the following code snippets are needed.
    # def get_uri(self):  # fetch the URI for the specific alert issued by NWS
    #     return self.alert['properties']['@id']
    #
    # def get_type(self):
    #     return self.alert['properties']['@type']


    """Per NWS - System-specific additional parameters associated with the alert message. 
    The keys in this object correspond to parameter definitions in the NWS CAP specification."""

    def get_parameters(self):
        return self.alert['parameters']


"""
All endpoints of https://api.weather.gov/alerts/active*/* seem to point to their AlertCollectionGeoJson schema. For
coherency, we'll change this structure to improve vector structure. But need to make sure this is safe by checking if 
other schemas do pop up.
"""


class AlertCollection:
    collection = None

    def __init__(self, collection):
        self.collection = collection

    # def get_description(self):
    #     return self.collection['description']

    def get_context(self):
        return self.collection['@context']

    def get_type(self):  # returns enum Feature(Collection)
        return self.collection['type']

    def get_features(self):  # returns array of objects that are GeoJsonFeatures, where each object has a (sub)-object
        # called properties, which is an Alert object.
        return self.collection['features']

    def get_title(self):  # title describing the collection
        return self.collection['title']

    def get_updated_time(self):  # last time a modification was made to the collection.
        return self.collection['updated']

    def get_pagination(self):  # link to next set of alerts.
        return self.collection['pagination']  # this can be None (null.)

# Unsure if the following code snippets are needed.

# def get_alerts(location):
#     url = "https://api.weather.gov/gridpoints/{0}/{1}/alerts{2}"  # station id, grid_loc, addtl. args.
#     url = url.format(location['id'], location['grid_location'], '')
#     req = utils.send(url, utils.RequestMethod.GET, None)
#
#     for item in req['features']:
#         p = Alert(item)

