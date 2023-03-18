from inc.http.GridRivalClient import GridRivalClient
from inc.Factories.DriverFactory import DriverFactory
from inc.Factories.TeamFactory import TeamFactory
from inc.Factories.playerFactory import PlayerFactory
from inc.Drivers import Drivers
from inc.Teams import Teams
from inc.League import League
from GridRival import GridRival

class GridRivalFactory:


    def __init__(self, client: GridRivalClient) -> None:
        self.client = client
        self.drivers: Drivers = Drivers()
        self.teams: Teams = Teams()
        self.league: League = League()

        self.raceIds = []
        self.nextRaceId:int
        pass

    def load(self)->None:
        gameData = self.client.getGameData()
        self.processRaces(gameData['sports']['event_map'])
        self.processDriverData(gameData['elements'])
        self.processTeamData(gameData['teamData'])
        self.processLeagueData(gameData['leagueData'])
    
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
                self.nextRaceId = race['stage_eid']
                foundNext = True
        print("success")

    def processTeamData(self, data):
        print("processing teams...")
        for team in data:
            teamFactory = TeamFactory(team)
            team = teamFactory.team
            self.teams.addTeam(team)
        print("success")
    
    def processLeagueData(self, data):
        print("processing player data...")
        for player in data:
            playerId = player['eid']
            print("Processing player: ", playerId)
            stagePlayerData = self.client.getPlayerData(playerId, self.nextRaceId)
            totalPlayerData = self.client.getTotalPlayerData(playerId)
            data = {"stage": stagePlayerData, "total": totalPlayerData, "info":player}
            playerFactory = PlayerFactory(data , self.drivers, self.teams, playerId)
            player = playerFactory.player
            self.league.addPlayer(player)
        print("success")

    

    def getGridRival(self):
        return GridRival(self.drivers, self.teams, self.league, self.raceIds, self.nextRaceId)
