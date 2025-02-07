import os
import secrets

from Data import data
from Rendering import render_versus


class Game:
    def __init__(self):
        self.score: int = 0
        self.username = os.getlogin()

    @staticmethod
    def get_pick():
        """Gets 2 random celebrities from the data set"""
        first_option: dict[str, int, str, str] = secrets.choice(data)
        second_option: dict[str, int, str, str] = secrets.choice(data)
        return [first_option, second_option]

    @staticmethod
    def get_user_play(first_name: str, second_name: str, id_one: int, id_two: int):
        """Returns the ID of the option selected
        by the user"""
        while True:
            user_input = input("Who has more followers? ").strip().lower()
            match user_input:
                case name if name == first_name.lower() or name == "a":
                    return id_one
                case name if name == second_name.lower() or name == "b":
                    return id_two
                case _:
                    print("Couldn't understand")

    def play_turn(self):
        """Plays a turn, returns the string \"DONE\" if the player loses"""
        options = self.get_pick()

        print(f"Compare A: {options[0]["name"]}, a {options[0]["description"]}, from {options[0]["country"]}.")
        render_versus()
        print(f"Against B: {options[1]["name"]}, a {options[1]["description"]}, from {options[1]["country"]}.")

        user_picked = self.get_user_play(options[0]["name"].lower(), options[1]["name"].lower(), options[0]["id"], options[1]["id"])
        options.sort(key=lambda x: x["follower_count"], reverse=True)

        if options[0]["follower_count"] == options[1]["follower_count"] or user_picked == options[0]["id"]:
            self.score += 1
        else:
            return "DONE"



