import os


class User:
    def __init__(self, username: str = os.getlogin()):
        self.username: str = username
        self.score: int = 0
