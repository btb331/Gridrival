from inc.http.GridRivalClient import GridRivalClient
from inc.Factories.DriverFactory import DriverFactory
from inc.Factories.TeamFactory import TeamFactory
from inc.Drivers import Drivers
from inc.Teams import Teams
from GridRival import GridRival

class GridRivalFactory:


    def __init__(self, client: GridRivalClient) -> None:
        self.client = client
        self.drivers: Drivers = Drivers()
        self.teams: Teams = Teams()
        self.raceIds = []
        self.nextRaceIndex:int
        pass

    def load(self)->None:
        gameData = self.client.getGameData()
        self.processRaces(gameData['sports']['event_map'])
        self.processDriverData(gameData['elements'])
        self.processTeamData(gameData['teamData'])
    
    def processDriverData(self, data:dict):
        print("processing drivers...")
        for driver in data:
            driverFactory = DriverFactory(driver)
            driver = driverFactory.driver
            self.drivers.addDriver(driver)
        print("success")    
    
    def processRaces(self, data):
        print("adding races..")
        foundNext = False
        for race in data:
            self.raceIds.append(race['stage_eid'])
            if race['completed'] is False and foundNext is False:
                self.nextRaceIndex = race['stage_eid']
                foundNext = True
        print("success")

    def processTeamData(self, data):
        print("processing drivers...")
        for team in data:
            teamFactory = TeamFactory(team)
            team = teamFactory.team
            self.teams.addTeam(team)
        print("success")    

    

    def getGridRival(self):
        return GridRival(self.drivers, self.teams, self.raceIds, self.nextRaceIndex)
