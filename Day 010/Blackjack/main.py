from Utils import *
from Interactions import *
from Game import Game


if __name__ == "__main__":

    if(not promptPlayGame()):
        exit(0)

    game = Game()
    while True:    
        userPassed = False
        if game.turn > 1:
            answer = promptGetOrPass()
            match answer:
                case "GET":
                    clearScreen()
                    game.addCards(True)
                case "PASS":
                    clearScreen()
                    game.addCards(False)
                    userPassed = True #If the user passes, terminate the game after the computer draws it's cards
                case _:
                    print("Got invalid answer to GET or PASS")
                    exit(1)
        
        game.getHands()
        game.setScores()
        
        if(game.checkOver() or userPassed):
            game.getWinner()
            promptPlayGame()

        
