from events.Rendering import *
from events.InputHandler import InputHandler
from Game import Game

if __name__ == "__main__":
    render_title()
    gameObj = Game()
    inputHandlerObj = InputHandler()
    while not gameObj.check_win_loss():
        render_current_guess(gameObj.currentGuess)
        inputHandlerObj.get_user_input(gameObj)
