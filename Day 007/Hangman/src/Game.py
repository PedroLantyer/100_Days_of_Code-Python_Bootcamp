from datetime import datetime
import random
from utils.util import *


class Game:
    MAX_LIVES: int = 6

    def __init__(self):
        self.lives: int = self.MAX_LIVES
        self.lettersTested: list[str] = []
        self.word: str = ""
        self.currentGuess: list[str] = []
        self.username: str = ""
        self.guessCount: int = 0
        self.gameStart: int = 0
        self.gameEnd: int = 0
        self.gameLength: dict = {"hours": 0, "minutes": 0, "seconds": 0}
        self.set_word()
        self.username = os.getlogin()
        self.gameStart = int(datetime.now().timestamp())

    def set_word(self):
        random.seed(datetime.now().timestamp())
        word_arr = ["RED", "BLACK", "YELLOW"]
        self.word = random.choice(word_arr)
        self.currentGuess = list("_" * len(self.word))

    def check_win_loss(self):
        if self.lives <= 0:
            self.trigger_loss()
            return True
        if not ("_" in self.currentGuess):
            self.trigger_win()
            return True
        return False

    def trigger_win(self):
        clear_screen()
        self.gameEnd = int(datetime.now().timestamp())
        self.set_game_length()

        print()
        print(f"{"YOU WIN!": ^30}")
        print("*" * 30)
        print(f"Player: {self.username}")
        print(f"Guesses: {self.guessCount}")
        print(f"Lives: {self.lives}/{self.MAX_LIVES}")
        print(f"Word: {self.word.upper()}")
        print("*" * 30)

    def trigger_loss(self):
        clear_screen()
        self.gameEnd = int(datetime.now().timestamp())
        self.set_game_length()
        correct_guesses = (len(self.currentGuess) - len(get_matches("_", self.currentGuess)))

        print()
        print(f"{"You lose!": ^30}")
        print("*" * 30)

        print(f"Duration:", end=" ")
        if self.gameLength["hours"] != 0:
            print(f"{self.gameLength["hours"]}h", end="")
        if self.gameLength["minutes"] != 0:
            print(f"{self.gameLength["minutes"]}h", end="")
        print(f"{self.gameLength["seconds"]}s")

        print(f"Correct guesses: {correct_guesses}/{len(self.currentGuess)}")
        print("*" * 30)

    def set_game_length(self):
        time_delta = int((self.gameEnd - self.gameStart))
        if time_delta > 3600:
            hours = int(time_delta / 3600)
            self.gameLength["hours"] = hours
            time_delta -= (hours * 3600)
        if time_delta > 60:
            minutes = int(time_delta / 60)
            self.gameLength["minutes"] = minutes
            time_delta -= (minutes * 60)
        if time_delta > 0:
            self.gameLength["seconds"] = time_delta
