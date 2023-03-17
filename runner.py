import json
from inc.http.GridRivalClient import GridRivalClient

loginData = json.load(open('login.json'))

client = GridRivalClient(loginData['username'], loginData['password'])
