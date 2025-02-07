import random
from utils.terminal import clearScreen
from datetime import *
from events.deathEvents import *
from stages.sceneOne.stagesOneToThree import *

if __name__ == "__main__":
    while(True):
        clearScreen()
        drawChest()
        print("Welcome to Treasure Island")
        print("Your mission is to find the treasure.")
    
        sceneOneStageOne()
        clearScreen()
        sceneOneStageTwo()
        clearScreen()
        sceneOneStageThree()
