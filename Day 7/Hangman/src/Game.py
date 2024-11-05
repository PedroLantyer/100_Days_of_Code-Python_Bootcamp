from datetime import datetime
import random
from utils.util import *

class Game:
    MAX_LIVES: int = 6
    lives:int = MAX_LIVES
    lettersTested:list[str] = []
    word:str = ""
    currentGuess: list[str] = []
    username: str = ""
    guessCount: int = 0
    gameStart: int
    gameEnd: int
    gameLength: dict = {"hours": 0, "minutes": 0, "seconds": 0}
    
    def __init__(self):
        self.setWord()
        self.username = os.getlogin()
        self.gameStart = int(datetime.now().timestamp())

    def setWord(self):
        #WIP
        random.seed(datetime.now().timestamp())
        wordArr = ["RED", "BLACK", "YELLOW"]
        self.word = random.choice(wordArr)
        self.currentGuess = list("_" * len(self.word))

    def checkWinLoss(self):
        if(self.lives <= 0):
            self.triggerLoss()
            return True
        if(not ("_" in self.currentGuess)):
            self.triggerWin()
            return True
        return False

    def triggerWin(self):
        clearScreen()
        self.gameEnd = int(datetime.now().timestamp())
        self.setGameLength()
        
        print()
        print(f"{"YOU WIN!": ^30}")
        print("*" * 30)
        print(f"Player: {self.username}")
        print(f"Guesses: {self.guessCount}")
        print(f"Lives: {self.lives}/{self.MAX_LIVES}")
        print(f"Word: {self.word.upper()}")
        print("*" * 30)

    def triggerLoss(self):
        clearScreen()
        self.gameEnd = int(datetime.now().timestamp())
        self.setGameLength()
        correctGuesses = (len(self.currentGuess) - len(getMatches("_", self.currentGuess)))
        
        print()
        print(f"{"You lose!": ^30}")
        print("*" * 30)

        print(f"Duration:",end=" ")
        if(self.gameLength["hours"] != 0):
            print(f"{self.gameLength["hours"]}h", end="")
        if(self.gameLength["minutes"] != 0):
            print(f"{self.gameLength["minutes"]}h", end="")
        print(f"{self.gameLength["seconds"]}s")

        print(f"Correct guesses: {correctGuesses}/{len(self.currentGuess)}")
        print("*" * 30)

    def setGameLength(self):
        timeDelta = int((self.gameEnd - self.gameStart))
        if(timeDelta > 3600):
            hours = int(timeDelta/3600)
            self.gameLength["hours"] = hours
            timeDelta -= (hours*3600)
        if(timeDelta > 60):
            minutes = int(timeDelta/60)
            self.gameLength["minutes"] = minutes
            timeDelta -= (minutes*60)
        if(timeDelta > 0):
            self.gameLength["seconds"] = timeDelta