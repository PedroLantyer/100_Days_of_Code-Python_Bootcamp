from Utils import clearScreen

def promptPlayGame():
    """Asks the user if he wants to play"""
    
    for i in range(5):
        print("Do you want to play a game of Blackjack? Type \"Yes\" or \"No\"")
        userInput = input().strip().lower()
        
        match userInput:
            case "yes":
                return True
            case "no":
                print("Goodbye :)")
                return False
            case _:
                if(i == 4):
                    print("You seem to be having a hard time answering, so I'm going to take that as a no.")
                    return False
                else:
                    clearScreen()
                    print("Sorry I couldn't understand you", end="\n\n")

def promptGetOrPass():
    """Asks the user if he wants to get the card or pass"""

    print()
    for i in range(3):
        print("Type 'y' to get another card, type 'n' to pass")
        userInput = input().strip().lower()
        
        match userInput:
            case "y":
                return "GET"
            case "n":
                return "PASS"
            case _:
                if(i == 2):
                    print("Tell you what lad, since you are playing hard to get, it's going to be a pass")
                    return "PASS"
                print("That's not a valid option buddy, answer again")
