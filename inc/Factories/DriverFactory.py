from inc.Driver import Driver

class DriverFactory:


    def __init__(self, driverData) -> None:
        self.driverData = driverData
        self.driverId: int
        self.qualiPoints: list[float] = []
        self.racePoints: list[float] = []
        self._driver = self.process()
        

    
    def process(self):
        self.driverId = self.driverData['eid']
        for scoreData in self.driverData['all_stats']['event_scores'].items():
            if len(scoreData[1]) == 0:
                continue
            self.qualiPoints.append(float(scoreData[1][0]['data'][0]['points']))
            racePoints = 0
            if 'data' not in scoreData[1][1]:
                self.racePoints.append(0)
                continue
            for racePoint in scoreData[1][1]['data']:
                racePoints = racePoints +  float(racePoint['points'])
            self.racePoints.append(racePoints)
        
        driver:Driver = Driver(self.driverId, self.qualiPoints, self.racePoints)
        return driver

    @property
    def driver(self)->Driver:
        return self._driver