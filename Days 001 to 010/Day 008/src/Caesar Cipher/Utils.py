import os


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")


def get_continue():
    for i in range(5):
        print()
        user_input = input("Do you want to continue? Type \"Yes\" or \"No\" \n").strip().lower()
        match user_input:
            case "yes":
                clear_screen()
                return True
            case "no":
                print("Goodbye!")
                return False
            case _:
                if i == 4:
                    print("You seem to be having some trouble answering")
                    print("I'll consider that as a no")
                    return False
                print("Sorry I couldn't understand. Try again", end="\n")
