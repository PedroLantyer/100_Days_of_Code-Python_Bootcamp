import secrets
import re as regexp
import os


def print_logo():
    # Raw string is often necessary for ascii art
    print(r"""
 _   _                 _                                           _             
| \ | |               | |                                         (_)            
|  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ _ _ __   __ _ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |
| |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ | | | | (_| |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/_|_| |_|\__, |
                                          __/ |                             __/ |
                                         |___/                             |___/ 
 
          """)


def clear_screen():
    """Clears the terminal"""
    os.system("cls") if os.name == "nt" else os.system("clear")


def prompt_replay():
    """
    Ask the user if he wishes to replay the game
    """

    for i in range(5):
        print("Do you want to play again? ")
        user_input = input("Type \"yes\" or \"no\": ").strip().lower()
        match user_input:
            case "yes":
                clear_screen()
                return True
            case "no":
                clear_screen()
                print("Goodbye")
                return False
            case _:
                if i == 4:
                    clear_screen()
                    print("You seem to be having a hard time answering.")
                    print("I'll take that as a no.")
                    print("Goodbye")
                    return False
                else:
                    print("Sorry I couldn't understand, could you please try again?", end="\n" * 2)
    return False


class Game:
    LOWER_LIMIT: int = 1
    UPPER_LIMIT: int = 100

    def __init__(self):
        self.max_lives: int = 0
        self.lives: int = 0
        self.difficulty: str = ""
        self.secret_number: int = 0
        print("Welcome to the Number Guessing Game!")
        self.set_difficulty()
        self.set_number()

    def set_difficulty(self) -> None:
        while True:
            print("Choose a difficulty. Type \"easy\" or \"hard\"")
            user_input = input().strip().lower()
            match user_input:
                case "easy":
                    self.difficulty = "Easy"
                    self.lives = 10
                    self.max_lives = 10
                    clear_screen()
                    return
                case "hard":
                    self.difficulty = "Hard"
                    self.lives = 5
                    self.max_lives = 5
                    clear_screen()
                    return
                case _:
                    print("Sorry, I couldn't understand. Try again", end="\n" * 2)

    def set_number(self):
        self.secret_number = secrets.choice(range(self.LOWER_LIMIT, self.UPPER_LIMIT + 1))

    def trigger_win(self):
        clear_screen()
        print("*" * 30)
        print("YOU WIN!")
        print(f"Lives left: {self.lives}/{self.max_lives}")
        print(f"Number: {self.secret_number}")
        print(f"Difficulty: {self.difficulty}")
        print("*" * 30, end="\n" * 3)

    def trigger_loss(self):
        clear_screen()
        print("*" * 30)
        print("YOU LOSE!")
        print(f"Number: {self.secret_number}")
        print(f"Difficulty: {self.difficulty}")
        print("*" * 30, end="\n" * 3)

    def make_play(self):
        """
        Returns True if the game is over.\n
        Otherwise returns False
        """

        print(f"Guess a number between {self.LOWER_LIMIT} and {self.UPPER_LIMIT}")
        print(f"You have {self.lives} attemps remaining to guess the number.")
        user_input = input("Make a guess: ").strip()

        if regexp.search("[^0-9]", user_input) is not None or len(user_input) == 0:
            print("That's not a number.", end="\n" * 2)
            self.lives -= 1
        else:
            guess = int(user_input)
            if guess == self.secret_number:
                self.trigger_win()
                return True
            else:
                print("Too Low.") if guess < self.secret_number else print("Too High.")
                print("Guess Again.", end="\n" * 2)
                self.lives -= 1

        if self.lives <= 0:
            self.trigger_loss()
            return True
        return False


if __name__ == "__main__":
    while True:
        print_logo()
        gameObj = Game()
        while not gameObj.make_play():
            pass  # Continue playing while the game isn't over
        if not prompt_replay():
            exit(0)
