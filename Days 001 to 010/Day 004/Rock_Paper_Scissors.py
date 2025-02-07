import random
from datetime import datetime
import os
from time import sleep


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")


class User:

    def __init__(self):
        self.play: str = ""
        self.name: str = ""
        self.score: int = 0
        self.name = os.getlogin()

    def set_user_play(self):
        while True:
            user_input = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n").strip()
            match user_input:
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
                    clear_screen()


class Computer:
    def __init__(self):
        self.play: str = ""
        self.score: int = 0
        pass

    def set_computer_play(self):
        random.seed(datetime.now().timestamp())
        play = random.randint(1, 3)
        match play:
            case 1:
                self.play = "Rock"
            case 2:
                self.play = "Paper"
            case 3:
                self.play = "Scissors"


class Game:
    def __init__(self):
        pass

    def get_winner(self, user: User, computer: Computer):
        try:
            if len(computer.play) == 0:
                raise ValueError("Couldn't get computer play")
            if len(user.play) == 0:
                raise ValueError("Couldn't get user play")

            if computer.play == user.play:
                clear_screen()
                print("Tie", end="\n\n")
            elif (user.play == "Rock" and computer.play == "Scissors") or (
                    user.play == "Paper" and computer.play == "Rock") or (
                    user.play == "Scissors" and computer.play == "Paper"):
                clear_screen()
                print("User Won", end="\n\n")
                user.score += 1
            else:
                clear_screen()
                print("Computer Won", end="\n\n")
                computer.score += 1
            self.print_score(user.score, computer.score, user.name)

        except ValueError as valueErr:
            print(valueErr)
            return False
        except Exception as err:
            print(err)
            return False

    @staticmethod
    def print_score(user_score: int, computer_score: int, user_name: str):
        try:
            print("SCORES:")
            print(f"{user_name}: {user_score}")
            print(f"Computer: {computer_score}", end="\n\n")
        except Exception as err:
            print(err)

    @staticmethod
    def get_continue():
        while True:
            user_input = input("Do you want to continue?\nType Yes or No\n").strip().upper()
            match user_input:
                case "YES":
                    clear_screen()
                    return True
                case "NO":
                    return False
                case _:
                    print("Couldn't understand, please try again: ", end="\n\n")
                    sleep(3)
                    clear_screen()


if __name__ == "__main__":
    userObj = User()
    computerObj = Computer()
    gameObj = Game()

    print(f"Hello {userObj.name}\nWelcome to Rock-Paper-Scissors")
    while True:
        userObj.set_user_play()
        computerObj.set_computer_play()

        if gameObj.get_winner(userObj, computerObj) is None:
            if not gameObj.get_continue():
                print(f"Goodbye {userObj.name}!")
                exit(0)
