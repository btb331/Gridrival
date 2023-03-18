from inc.Team import Team

class TeamFactory:


    def __init__(self, teamData) -> None:
        self.teamData = teamData
        self.teamId: int
        self.qualiPoints: list[float] = []
        self.racePoints: list[float] = []
        self._team = self.process()
        

    
    def process(self):
        self.teamId = self.teamData['eid']
        for scoreData in self.teamData['all_stats']['event_scores'].items():
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
        
        team:Team = Team(self.teamId, self.qualiPoints, self.racePoints)
        return team

    @property
    def team(self)->Team:
        return self._team