import os


def clear_screen():
    """Clears the terminal."""
    os.system('cls') if os.name == 'nt' else os.system('clear')


def get_replay():
    """Asks the user if he wants to play again"""
    for i in range(5):
        print("Do you wanna play again?", end=" ")
        user_input = input("Type \"Yes\" or \"No\".\n").strip().lower()
        match user_input:
            case "yes":
                clear_screen()
                return True
            case "no":
                clear_screen()
                print("Thank you for playing!")
                return False
            case _:
                if i == 4:
                    clear_screen()
                    print("You seem to be having some trouble")
                    print("I'm going to take that as a no.")
                    print("Thank you for playing!")
                    return False
                print("\nSorry I couldn't understand.")
