from inc.http.GridRivalClient import GridRivalClient
from inc.Drivers import Drivers
from inc.Driver import Driver
from inc.Teams import Teams
from inc.Team import Team
from inc.League import League

class GridRival:

    

    def __init__(self, drivers:Drivers, teams:Teams, league:League, raceIds: list[int], nextGameIndex: int) -> None:
        self.raceIds: list[int] = []
        self._nextRaceIndex:int = None
        self.drivers: Drivers = drivers
        self.teams: Teams = teams
        self.league: League = league
        pass
    
    @property
    def nextRaceIndex(self):
        return self._nextRaceIndex
    
    def getDriver(self, driverId)->Driver:
        return self.drivers.getDriver(driverId)
    
    def getTeam(self, teamId)->Team:
        return self.teams.getTeam(teamId)

    def calculateRoundScore(self, round):
        return self.league.calculateRound(round)
    
    def calculateTotalScoreMidRound(self, round):
        return self.league.calculateTotalScoreMidWeek(round)
    