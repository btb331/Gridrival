from inc.http.GridRivalConnect import GridRivalConnect

class GridRivalClient:

    def __init__(self, username:str, pwd:str) -> None:
        self.connect = GridRivalConnect()
        self.connect.login(username, pwd)
    
    def getGameData(self):
        print("loading game data")
        url = "v1/myleagues/statistics/elements"

        payload = {
            "element_type_k":"DRIVER",
            "league_eid":1020032,
            "season":"F1/23",
            "sport_k":"F1"
        }

        data = self.connect.post(url, payload)

        url = "v1/myleagues/statistics/elements"

        payload = {
            "element_type_k":"CONSTR",
            "league_eid":1020032,
            "season":"F1/23",
            "sport_k":"F1"
        }

        teamData = self.connect.post(url, payload)

        data['teamData'] = teamData['elements']

        url = "v2/myleagues/league/card"

        payload = {
            "league_eid": "1020032"
        }

        cardData = self.connect.post(url, payload)

        data['sports'] = cardData['sports']['F1'] #adding in extra data from other call
        data['leagueData'] = cardData['league']['teams']

        print("success")
        return data
    
    def getPlayerData(self, playerId, stageId):

        url = "v1/myleagues/performance"

        payload = {
            "team_eid":playerId,
            "stage_eid":stageId
        }

        data = self.connect.post(url, payload)

        return data
    
    def getTotalPlayerData(self, playerId):

        url = "v1/myleagues/performance"

        payload = {
            "team_eid":playerId,
            "stage_path":"F1/23/01"
        }

        data = self.connect.post(url, payload)

        return data