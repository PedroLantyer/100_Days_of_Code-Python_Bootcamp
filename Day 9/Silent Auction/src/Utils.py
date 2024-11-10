import os

def promptContinueGettingBidders():
    """Ask the user if there are any other bidders to be added"""
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
    """Clear the Terminal"""
    os.system("cls") if os.name == "nt" else os.system("clear")