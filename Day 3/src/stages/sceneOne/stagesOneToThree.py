from utils.terminal import clearScreen
from events.narrator import *

def sceneOneStageOne():
    options = ("left", "right")
    while(True):
        iterCount = 0
        print("\nYou're at a cross road.")
        print("Where do you want to go?")
        userInput = input(f"{" " * 5}Type \"{options[0]}\" or \"{options[1]}\"\n").strip().lower()
        
        if(userInput == options[0]):
                return
        if(userInput == options[1]):
                landDeath()

        else:
            iterCount += 1
            clearScreen()
            getNarratorWrongPath(iterCount, stage=1)   
            
def sceneOneStageTwo():
    options = ("wait", "swim")
    while(True):
        iterCount = 0
        print("\nYou've come to a lake.")
        print("There's an island in the middle of the lake")
        userInput = input(f"{" " * 3}Type \"wait\" to wait for the boat, or type \"swim\" to swim across.\n").strip().lower()

        if(userInput == options[0]):
                return
        if(userInput == options[1]):
                seaDeath()
                    
        else:
            iterCount += 1
            getNarratorWrongPath(iterCount, stage=2)

def sceneOneStageThree():
    options = ("red", "yellow", "blue")
    while(True):
        iterCount = 0
        print("\nYou arrive at the island unharmed.")
        print("There is a house with 3 doors.")
        print(f"{" " * 3}One red, one yellow and one blue;")
        userInput = input(f"{" " * 3}Which colour do you choose?\n").strip().lower()

        if(userInput == options[0]):
            doorDeath()
        if(userInput == options[1]):
            print("You found the treasure! You Win!")
            exit(0)
        if(userInput == options[2]):
            doorDeath()
        else:
            iterCount += 1
            getNarratorWrongPath(iterCount, stage=3)
