import requests
import json


class DataScraper:
    baseUrl = "https://www.thebluealliance.com/api/v3"
    apiKey = "1CQGBNHADuOcI5xDHmLjpIBdQwxTHzZmPpDohm1gNs79gDtN5BrGgIt1bPzAlx2N"
    SVReventKey = ""
    SFeventKey = ""

    def __init__(self):
        self.SVReventKey = self.getEvent("2018", "Silicon Valley Regional")[
            'first_event_id']
        self.SFeventKey = self.getEvent("2018", "San Francisco Regional")[
            'first_event_id']

    def getEvent(self, year, name):
        events = json.loads(requests.get(self.baseUrl + "/events/" +
                                         year + '?X-TBA-Auth-Key='+self.apiKey).text)
        return next((e for e in events if e['name'] == name))

    def getTeamInfo(self, team, year):
        return json.loads(requests.get(self.baseUrl + "/team/frc"+team+"/events/" +
                                       year+"/statuses" + '?X-TBA-Auth-Key='+self.apiKey).text)


print(DataScraper().getEvent("2018", "San Francisco Regional"))
print(DataScraper().getTeamInfo("254", "2018"))
