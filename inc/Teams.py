from inc.Team import Team

class Teams:

    def __init__(self) -> None:
        self.teams: dict[int, Team] = {}

    def addTeam(self, team:Team):
        self.teams[team.id] = team
    
    def getTeam(self, teamId)->Team:
        return self.teams[teamId]