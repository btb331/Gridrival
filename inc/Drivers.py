from inc.Driver import Driver

class Drivers:

    def __init__(self) -> None:
        self.drivers: dict[int, Driver] = {}

    def addDriver(self, driver:Driver):
        self.drivers[driver.id] = driver
    
    def getDriver(self, driverId)->Driver:
        return self.drivers[driverId]