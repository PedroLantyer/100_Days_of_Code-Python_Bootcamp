import os.path
import re as regexp

from Game import Game
from utils.util import get_matches


class InputHandler:
    def __init__(self):
        pass

    @staticmethod
    def check_input_is_valid(user_input: str):
        non_alpha_found = regexp.search("[^A-Za-z]", user_input)
        if non_alpha_found is not None:
            return False
        return True

    def get_user_input(self, game_obj: Game):
        user_input: str = input("Please type a letter: ").upper().strip()

        if len(user_input) != 1 or not self.check_input_is_valid(user_input):
            print("Oh, that's not an option, bad luck buddy.")
            game_obj.lives -= 1

        elif user_input in game_obj.lettersTested:
            print("You already tried that letter")
            game_obj.lives -= 1

        else:
            matches = get_matches(user_input, game_obj.word)
            if len(matches) == 0:
                game_obj.lives -= 1
                print(f"The letter {user_input} is not in the word")
            else:
                for index in matches:
                    game_obj.currentGuess[index] = user_input
            game_obj.lettersTested.append(user_input)

        game_obj.guessCount += 1
