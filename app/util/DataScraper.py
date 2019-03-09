import requests
import json
#import tbapy


class DataScraper:
    baseUrl = "https://www.thebluealliance.com/api/v3"
    apiKey = "1CQGBNHADuOcI5xDHmLjpIBdQwxTHzZmPpDohm1gNs79gDtN5BrGgIt1bPzAlx2N"
    #tba = tbapy.TBA(apiKey)
    SVReventKey = ""
    SFeventKey = ""

    def __init__(self):
        self.SVReventKey = '2018casj'
        self.SFeventKey = '2018casf'

    def getEvent(self, year, name):
        events = json.loads(requests.get(self.baseUrl + "/events/" +
                                         year + '?X-TBA-Auth-Key='+self.apiKey).text)
        return next((e for e in events if e['name'] == name))

    def getTeamInfo(self, team, year):
        return json.loads(requests.get(self.baseUrl + "/team/frc"+team+"/events/" +
                                       year+"/statuses" + '?X-TBA-Auth-Key='+self.apiKey).text)

    def getSecretTeamInfo(self, team):
        return json.loads(requests.get(self.baseUrl + '/team/frc'+team+'?X-TBA-Auth-Key='+self.apiKey).text)

    def getTeams(self, year, id):
        return json.loads(requests.get(self.baseUrl + "/event/" + id + "/teams" + '?X-TBA-Auth-Key=' + self.apiKey).text)

    def getTeamEventStatus(self, team, event_key):
        return json.loads(requests.get(self.baseUrl + '/team/frc'+team+'/event/'+event_key+'/status'+'?X-TBA-Auth-Key='+self.apiKey).text)

    def eventAlliances(self, event_key):
        return json.loads(requests.get(self.baseUrl + '/event/'+event_key+'/alliances'+'?X-TBA-Auth-Key='+self.apiKey).text)

    def getTeamMatches(self, team, event_key):
        return json.loads(requests.get(self.baseUrl + '/team/frc'+team+'/event/'+event_key+'/matches'+'?X-TBA-Auth-Key='+self.apiKey).text)

    def getMatchTeams(self, matchNumber):
        data=json.loads(requests.get(self.baseUrl + '/match/'+matchNumber+'?X-TBA-Auth-Key='+self.apiKey).text)
        print(data)
        try:
            red = [e[3:] for e in data['alliances']['red']['team_keys']]
            blue = [e[3:] for e in data['alliances']['blue']['team_keys']]
        except:
            return None
        return {
            "R1": red[0],
            "R2": red[1],
            "R3": red[2],
            "B1": blue[0],
            "B2": blue[1],
            "B3": blue[2]
        }


datascraper = DataScraper()
# print(datascraper.getEvent("2019", "San Francisco Regional"))
# print(datascraper.getTeamInfo("254", "2018"))
# print(datascraper.eventAlliances(datascraper.SFeventKey))
# print(datascraper.SVReventKey)
# print(datascraper.getTeams("2019", datascraper.SFeventKey))
