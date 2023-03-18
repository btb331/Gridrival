from inc.Drivers import Drivers
from inc.Teams import Teams
from inc.Team import Team
from inc.Driver import Driver
from inc.Player import Player


class PlayerFactory:


    def __init__(self, playerData, drivers: Drivers, teams: Teams, id) -> None:
        self._player: Player
        self.id = id
        self.allDrivers = drivers
        self.allTeams = teams
        self.playerData = playerData
        self.selectedDrivers: Drivers = Drivers
        self.selectTeam: Team
        
        self.previousPoints: int
        self.drivers = []
        self.team:int
        self.userName:str
        self.process()

    def process(self):
        self.previousPoints = self.playerData['total']['team_total_fp']
        self.userName = self.playerData['info']['name']
        for contracts in self.playerData['stage']['previous_team']['bought_contracts']:
            contractType = contracts['contract_type_k']
            id = contracts['element_party_eid']
            if contractType == "DRIVER":
                self.drivers.append(self.allDrivers.getDriver(id))
            if contractType == "CONSTR":
                self.team = self.allTeams.getTeam(id)
            if contractType == "TALENT":
                self.drivers.append(self.allDrivers.getDriver(id))
        
        self._player = Player(self.id, self.team, self.drivers, self.previousPoints, self.userName)
        
    
    @property
    def player(self):
        return self._player
