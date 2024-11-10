import os

def promptContinueGettingBidders():
    while True:
        print()
        print("Are there any other bidders? Type \"yes\" or \"no\".")
        userInput = input().strip().lower()
        match userInput:
            case "yes":
                return True
            case "no":
                return False
            case _:
                print("Sorry, I couldn't understand")

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")