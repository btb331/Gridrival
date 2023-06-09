import requests
import json

class GridRivalConnect:

    def __init__(self) -> None:
        self.token: str = ""
        self.baseUrl = "https://api.gridrival.com/api/"
        pass

    def login(self, username:str, pwd:str) -> bool:
        print("logging in...")
        url = "https://api.gridrival.com/api/v1/auth/login"

        loginDetail = {
            "email": username,
            "password": pwd
        }
        resp = requests.post(url, headers={"content-type": "application/json;charset=UTF-8"},
                            data= json.dumps(loginDetail))
        
        if resp.status_code != 200:
            print("Error in logging in")
            return False
        
        data = json.loads(resp.content)
        self.token = "Bearer " + data['token']
        print("success")

        return True
    
    def get(self, url:str):
        resp = requests.get(self.baseUrl + url, headers={"content-type": "application/json;charset=UTF-8", "authorization": self.token})

        if resp.status_code != 200:
            print("Error getting ", url)
            return False
        return  json.loads(resp.content)
    
    def post(self, url:str, data: dict):

        url = self.baseUrl+ url
        data = json.dumps(data)


        resp = requests.post(url, headers={"content-type": "application/json;charset=UTF-8", "authorization": self.token}, data= data)

        if resp.status_code != 200:
            print("Error posting to ", url)
            print(resp.content)
            return False
        return  json.loads(resp.content)

