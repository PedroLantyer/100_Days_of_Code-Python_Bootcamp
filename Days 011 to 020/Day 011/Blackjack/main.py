from Interactions import *
from Game import Game

if __name__ == "__main__":

    if not prompt_play_game():
        exit(0)

    game = Game()
    while True:
        userPassed = False
        if game.turn > 1:
            answer = prompt_get_or_pass()
            match answer:
                case "GET":
                    clear_screen()
                    game.add_cards(True)
                case "PASS":
                    clear_screen()
                    game.add_cards(False)
                    userPassed = True
                    # If the user passes, terminate the game after the computer draws his cards
                case _:
                    print("Got invalid answer to GET or PASS")
                    exit(1)

        game.get_hands()
        game.set_scores()

        if game.check_over() or userPassed:
            game.get_winner()
            prompt_play_game()
