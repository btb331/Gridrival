from inc.http.GridRivalClient import GridRivalClient
from inc.Player import Player

class League:

    def __init__(self) -> None:
        self.players: dict[int, Player] = {}

    def addPlayer(self, player:Player):
        self.players[player.id] = player
    
    def getPlayer(self, driverId)->Player:
        return self.players[driverId]
    
    def calculateRound(self, round):
        result = {}
        for playerId in self.players:
            player:Player = self.players[playerId]
            points = player.roundPoints(round)
            result[player.username] = points
        return result
    
    def calculateTotalScoreMidWeek(self, round):
        result = {}
        for playerId in self.players:
            player:Player = self.players[playerId]
            points = player.roundPoints(round) + player.prevTotalPoints
            result[player.username] = points
        return result
