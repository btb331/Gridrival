from inc.http.GridRivalConnect import GridRivalConnect

class GridRivalClient:

    def __init__(self, username:str, pwd:str) -> None:
        self.connect = GridRivalConnect()
        self.connect.login(username, pwd)