from events.Rendering import *
from utils.util import *
from events.InputHandler import InputHandler
from Game import Game

if __name__ == "__main__":
    renderTitle()
    gameObj = Game()
    inputHandlerObj = InputHandler()
    while((not gameObj.checkWinLoss())):
        renderCurrentGuess(gameObj.currentGuess)
        inputHandlerObj.getUserInput(gameObj)