import json
from inc.http.GridRivalClient import GridRivalClient
from GridRivalFactory import GridRivalFactory
from GridRival import GridRival

loginData = json.load(open('login.json'))

client = GridRivalClient(loginData['username'], loginData['password'])

gridRivalFactory = GridRivalFactory(client)
gridRivalFactory.load()

gridRival:GridRival = gridRivalFactory.getGridRival()

driver = gridRival.getDriver(937219)

print(driver.totalPoints())