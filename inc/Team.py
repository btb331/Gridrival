class Team:

    def __init__(self, id, qualiPoints, racePoints) -> None:
        self._id = id
        self._qualiPoints = qualiPoints
        self._racePoints = racePoints
        pass

    @property
    def id(self):
        return self._id
    
    @property
    def qualiPoints(self):
        return self._qualiPoints
    
    @property
    def racePoints(self):
        return self._racePoints
    
    def totalQualiPoints(self):
        return sum(self.qualiPoints)
    
    def totalRacePoints(self):
        return sum(self.racePoints)
    
    def totalPoints(self):
        return self.totalRacePoints() + self.totalQualiPoints()

