from Utils import *
from Interactions import *
from Game import Game


if __name__ == "__main__":

    if(promptPlayGame() == False):
        exit(0)

    game = Game()
    while True:    
        if game.turn > 1:
            answer = promptGetOrPass()
            match answer:
                case "GET":
                    clearScreen()
                    game.addCards(True)
                case "PASS":
                    clearScreen()
                    game.addCards(False)
                case _:
                    print("Got invalid answer to GET or PASS")
                    exit(1)
        
        game.getHands()
        game.setScores()
        
        if(game.checkOver()):
            game.getWinner()
            break

        
