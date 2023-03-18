import json
from inc.http.GridRivalClient import GridRivalClient
from GridRivalFactory import GridRivalFactory
from GridRival import GridRival

loginData = json.load(open('login.json'))

client = GridRivalClient(loginData['username'], loginData['password'])

gridRivalFactory = GridRivalFactory(client)
gridRivalFactory.load()

gridRival:GridRival = gridRivalFactory.getGridRival()

roundScores = gridRival.calculateRoundScore(1)

orderRoundScores = {k: v for k, v in sorted(roundScores.items(), key=lambda item: item[1], reverse=True)}

print("Round score")
for name in orderRoundScores:
    print(name, ":",  orderRoundScores[name])

print("")
totalScores = gridRival.calculateTotalScoreMidRound(1)

orderTotalScores = {k: v for k, v in sorted(totalScores.items(), key=lambda item: item[1], reverse=True)}

print("Total Scores")
for name  in orderTotalScores:
    print(name, ":",  orderTotalScores[name])
