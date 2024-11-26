from Game import Game
from Rendering import render_title
from Util import *

if __name__ == "__main__":
    while True:
        render_title()
        game = Game()

        while True:
            if game.play_turn() == "DONE":
                clear_screen()
                render_title()
                print(f"Sorry that's wrong. Final Score: {game.score}", end="\n\n")
                break
            render_title()
            print(f"You're right! Current Score: {game.score}")

        if not get_replay():
            break

    exit(0)
