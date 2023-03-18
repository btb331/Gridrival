from inc.Driver import Driver
from inc.Team import Team

class Player:

    def __init__(self, id, team: Team, drivers: list[Driver], prevTotalPoints, username) -> None:
        self._id = id
        self._team:Team = team
        self._drivers: list[Driver] = drivers
        self._prevTotalPoints = prevTotalPoints
        self._username = username
        pass

    @property
    def id(self):
        return self._id
    
    @property
    def team(self)->Team:
        return self._team
    
    @property
    def drivers(self)->list[Driver]:
        return self._drivers
    
    @property
    def prevTotalPoints(self):
        return self._prevTotalPoints

    @property
    def username(self):
        return self._username
    
    def roundPoints(self, round):
        points = 0
        for driver in self.drivers:
            points = points + driver.roundPoint(round)
        points = points + self.team.roundPoint(round)
        return points
