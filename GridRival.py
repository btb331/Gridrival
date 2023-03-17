from inc.http.GridRivalClient import GridRivalClient
from inc.Drivers import Drivers
from inc.Driver import Driver
from inc.Teams import Teams
from inc.Team import Team

class GridRival:

    

    def __init__(self, drivers:Drivers, teams:Teams, raceIds: list[int], nextGameIndex: int) -> None:
        self.raceIds: list[int] = []
        self._nextRaceIndex:int = None
        self.drivers: Drivers = drivers
        self.teams: Teams = teams
        pass
    
    @property
    def nextRaceIndex(self):
        return self._nextRaceIndex
    
    def getDriver(self, driverId)->Driver:
        return self.drivers.getDriver(driverId)
    
    def getTeam(self, teamId)->Team:
        return self.teams.getTeam(teamId)
    
    