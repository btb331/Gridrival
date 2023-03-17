import requests
import json

class GridRivalConnect:

    def __init__(self) -> None:
        self.token: str = ""
        self.baseUrl = "https://api.gridrival.com/api/v2/"
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
        self.token = data['token']
        print("success")

        return True

