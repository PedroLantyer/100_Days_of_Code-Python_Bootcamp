import random
from datetime import datetime
import os
from time import sleep

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

class user:
    
    def __init__(self):
        self.play: str = ""
        self.name: str = ""
        self.score: int = 0
        self.name = os.getlogin()

    def setUserPlay(self):
        while True:
            userInput = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n").strip()
            match userInput:
                case "1":
                    self.play = "Rock"
                    break
                case "2":
                    self.play = "Paper"
                    break
                case "3":
                    self.play = "Scissors"
                    break
                case _:
                    print("Couldn't understand, please try again: ", end="\n\n")
                    sleep(3)
                    clearScreen()

class computer:
    def __init__(self):
        self.play: str = ""
        self.score: int = 0
        pass
    
    def setComputerPlay(self):
        random.seed(datetime.now().timestamp())
        play = random.randint(1, 3)
        match play:
            case 1:
                self.play = "Rock"
            case 2:
                self.play = "Paper"
            case 3:
                self.play = "Scissors"

class game:
    def __init__(self):
        pass
    
    def getWinner(self, user: user, computer: computer):
        try:
            if(len(computer.play) == 0):
                raise ValueError("Couldn't get computer play")
            if(len(user.play) == 0):
                raise ValueError("Couldn't get user play")
            
            if(computer.play == user.play):
                clearScreen()
                print("Tie", end="\n\n")
            elif((user.play == "Rock" and computer.play == "Scissors") or (user.play == "Paper" and computer.play == "Rock") or (user.play == "Scissors" and computer.play == "Paper")):
                clearScreen()
                print("User Won", end="\n\n")
                user.score += 1
            else:
                clearScreen()
                print("Computer Won", end="\n\n")
                computer.score += 1
            self.printScore(user.score, computer.score, user.name)

        except ValueError as valueErr:
            print(valueErr)
            return False
        except Exception as err:
            print(err)
            return False
    
    def printScore(self, userScore:int, computerScore: int, userName: str):
        try:
            print("SCORES:")
            print(f"{userName}: {userScore}")
            print(f"Computer: {computerScore}", end="\n\n")
        except Exception as err:
            print(err)
        

    def getContinue(self):
        while True:
            userInput = input("Do you want to continue?\nType Yes or No\n").strip().upper()
            match userInput:
                case "YES":
                    clearScreen()
                    return True
                case "NO":
                    return False
                case _:
                    print("Couldn't understand, please try again: ", end="\n\n")
                    sleep(3)
                    clearScreen()
               
if __name__ == "__main__":
    userObj = user()
    computerObj = computer()
    gameObj = game()

    print(f"Hello {userObj.name}\nWelcome to Rock-Paper-Scissors")
    while True:
        userObj.setUserPlay()
        computerObj.setComputerPlay()
        
        if(gameObj.getWinner(userObj, computerObj) == None):
            if(not gameObj.getContinue()):
                print(f"Goodbye {userObj.name}!")
                exit(0)
