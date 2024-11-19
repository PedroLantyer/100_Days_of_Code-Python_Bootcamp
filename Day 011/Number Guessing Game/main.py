import secrets
import re as regexp
import os

def printLogo():
    #Raw string is often necessary for ascii art
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

def clearScreen():
    """Clears the terminal"""
    os.system("cls") if os.name == "nt" else os.system("clear")

def promptReplay():
    """
    Ask the user if he wishes to replay the game
    """
    
    for i in range(5):
        print("Do you want to play again? ")
        userInput = input("Type \"yes\" or \"no\": ").strip().lower()
        match userInput:
            case "yes":
                clearScreen()
                return True
            case "no":
                clearScreen()
                print("Goodbye")
                return False
            case _:
                if(i == 4):
                    clearScreen()
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
        print("Welcome to the Number Guessing Game!")
        self.setDifficulty()
        self.setNumber()

    def setDifficulty(self) -> None:
        while True:
            print("Choose a difficulty. Type \"easy\" or \"hard\"")
            userInput = input().strip().lower()
            match userInput:
                case "easy":
                    self.difficulty = "Easy"
                    self.lives = 10
                    self.MAX_LIVES = 10
                    clearScreen()
                    return
                case "hard":
                    self.difficulty = "Hard"
                    self.lives = 5
                    self.MAX_LIVES = 5
                    clearScreen()
                    return
                case _:
                    print("Sorry, I couldn't understand. Try again", end="\n" * 2)

    def setNumber(self):
        self.secretNumber = secrets.choice(range(self.LOWER_LIMIT,self.UPPER_LIMIT))

    def triggerWin(self):
        clearScreen()
        print("*" * 30)
        print("YOU WIN!")
        print(f"Lives left: {self.lives}/{self.MAX_LIVES}")
        print(f"Number: {self.secretNumber}")
        print(f"Difficulty: {self.difficulty}")
        print("*" * 30, end="\n" * 3)

    def triggerLoss(self):
        clearScreen()
        print("*" * 30)
        print("YOU LOSE!")
        print(f"Number: {self.secretNumber}")
        print(f"Difficulty: {self.difficulty}")
        print("*" * 30, end="\n" * 3)


    def makePlay(self):
        """
        Returns True if the game is over.\n
        Otherwise returns False
        """

        print(f"Guess a number between {self.LOWER_LIMIT} and {self.UPPER_LIMIT}")
        print(f"You have {self.lives} attemps remaining to guess the number.")
        userInput = input("Make a guess: ").strip()
        
        if(regexp.search("[^0-9]", userInput) != None or len(userInput) == 0):
            print("That's not a number.", end="\n" * 2)
            self.lives -= 1
        else:
            guess = int(userInput)
            if(guess == self.secretNumber):
                self.triggerWin()
                return True
            else:
                print("Too Low.") if guess < self.secretNumber else print("Too High.")
                print("Guess Again.", end="\n" * 2)
                self.lives -= 1
        
        if(self.lives <= 0):
            self.triggerLoss()
            return True
        return False
                


if __name__ == "__main__":
    while True:
        printLogo()
        gameObj = Game()
        while(not gameObj.makePlay()):
            pass #Continue playing while the game isn't over
        if(not promptReplay()):
            exit(0)