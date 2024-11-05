import re as regexp
from Game import Game
from utils.util import *


class InputHandler:
    def __init__(self):
        pass

    def checkInputIsValid(self, userInput: str):
        nonAlphaFound = regexp.search("[^A-Za-z]", userInput)
        if(nonAlphaFound != None):
            return False
        return True

    def getUserInput(self, gameObj: Game):
        userInput = input("Please type a letter: ").upper().strip()
        
        if(len(userInput) != 1 or (not self.checkInputIsValid(userInput))):
            print("Oh, that's not an option, bad luck buddy.")
            gameObj.lives -= 1
        
        elif(userInput in gameObj.lettersTested):
            print("You already tried that letter")
            gameObj.lives -= 1
        
        else:
            matches = getMatches(userInput, gameObj.word)
            if(len(matches) == 0):
                gameObj.lives -= 1
                print(f"The letter {userInput} is not in the word")
            else:
                for index in matches:
                    gameObj.currentGuess[index] = userInput
            gameObj.lettersTested.append(userInput)
            
        gameObj.guessCount += 1