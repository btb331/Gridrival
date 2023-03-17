from inc.http.GridRivalClient import GridRivalClient
from inc.Drivers import Drivers
from inc.Driver import Driver

class GridRival:

    

    def __init__(self, drivers:Drivers, raceIds: list[int], nextGameIndex: int) -> None:
        self.raceIds: list[int] = []
        self._nextRaceIndex:int = None
        self.drivers: Drivers = drivers
        pass
    
    @property
    def nextRaceIndex(self):
        return self._nextRaceIndex
    
    def getDriver(self, driverId)->Driver:
        return self.drivers.getDriver(driverId)    
    
    