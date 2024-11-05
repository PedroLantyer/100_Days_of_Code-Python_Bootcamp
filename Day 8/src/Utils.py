import os

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def getContinue():
    for i in range(5):
        print()
        userInput = input("Do you want to continue? Type \"Yes\" or \"No\" \n").strip().lower()
        match userInput:
            case "yes":
                clearScreen()
                return True
            case "no":
                print("Goodbye!")
                return False
            case _:
                if(i == 4):
                    print("You seem to be having some trouble answering")
                    print("I'll consider that as a no")
                    return False
                print("Sorry I couldn't understand. Try again", end= "\n")