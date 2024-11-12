import os

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")
def getContinue():
    while(True):
        print("Do you wanna try again?")
        print("If Yes, type YES")
        print("If No, type NO")

        userInput = input()
        match userInput.upper():
            case "YES":
                clearScreen()
                return True
            case "NO":
                return False
            case _:
                print("Sorry I couldn't understand", end="\n\n")

if __name__ == "__main__":
    while(True):
        print("Welcome to the Band Name Generator.", end="\n\n")
        
        city = input("What's the name of the city you grew up in?\n")
        petName = input("What's your pet's name?\n")

        clearScreen()
        print(f"Your band name could be {city} {petName}")

        if(not getContinue()):
            print("Goodbye", end="\n\n")
            exit(0)
    
    