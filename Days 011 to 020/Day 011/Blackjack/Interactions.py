from Utils import clear_screen


def prompt_play_game(replay_message: bool = False):
    """Asks the user if he wants to play"""
    for i in range(5):
        if not replay_message:
            print("Do you want to play a game of Blackjack? Type \"Yes\" or \"No\"")
        else:
            print("Do you want to play again? Type \"Yes\" or \"No\"")
        user_input = input().strip().lower()

        match user_input:
            case "yes":
                return True
            case "no":
                print("Goodbye :)")
                return False
            case _:
                if i == 4:
                    print("You seem to be having a hard time answering, so I'm going to take that as a no.")
                    return False
                else:
                    clear_screen()
                    print("Sorry I couldn't understand you", end="\n\n")


def prompt_get_or_pass():
    """Asks the user if he wants to get the card or pass"""

    print()
    for i in range(3):
        print("Type 'y' to get another card, type 'n' to pass")
        user_input = input().strip().lower()

        match user_input:
            case "y":
                return "GET"
            case "n":
                return "PASS"
            case _:
                if i == 2:
                    print("Tell you what lad, since you are playing hard to get, it's going to be a pass")
                    return "PASS"
                print("That's not a valid option buddy, answer again")
