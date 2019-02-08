import requests
import json


class DataScraper:
    baseUrl = "https://www.thebluealliance.com/api/v3"
    apiKey = "1CQGBNHADuOcI5xDHmLjpIBdQwxTHzZmPpDohm1gNs79gDtN5BrGgIt1bPzAlx2N"
    SVReventKey = ""

    def __init__(self):
        self.SVReventKey = self.getEvent("2018", "Silicon Valley Regional")[
            'first_event_id']

    def getEvent(self, year, name):
        events = json.loads(requests.get(self.baseUrl + "/events/" +
                                         year + '?X-TBA-Auth-Key='+self.apiKey).text)
        return next((e for e in events if e['name'] == name))


print(DataScraper().getEvent("2018", "San Francisco Regional"))
